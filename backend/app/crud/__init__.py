# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import asyncio
import json
from copy import deepcopy
from datetime import datetime
from typing import List, Tuple

from sqlalchemy import select, update

from app.enums.operation import SqlOperationTypeEnum
from app.middleware.xredis import RedisHelper
from app.models import async_session, DatabaseHelper
from app.models.basic import PikaRelationField
from app.models.system import PikaOperationLog
from config import PikaAppConfig


class PikaMapper(object):
    log = None
    model = None

    @classmethod
    @RedisHelper.cache("dao")
    async def list_record(cls, condition=None, **kwargs):
        """
        通过查询条件获取数据，kwargs的key为参数名, value为参数值
        Args:
            condition:
            **kwargs:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = cls.query_wrapper(condition, **kwargs)
                result = await session.execute(sql)
                return result.scalars().all()
        except Exception as e:
            # 这边调用cls本身的log参数，写入日志+抛出异常
            cls.log.error(f"获取{cls.model}列表失败, error: {e}")
            raise Exception(f"获取数据失败")

    @classmethod
    @RedisHelper.cache("dao")
    async def list_record_with_pagination(cls, page, size, **kwargs):
        """
        通过分页获取数据
        Args:
            page:
            size:
            **kwargs:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = cls.query_wrapper(**kwargs)
                return await DatabaseHelper.pagination(page, size, session, sql)
        except Exception as e:
            cls.log.error(f"获取{cls.model}列表失败, error: {e}")
            raise Exception(f"获取数据失败")

    @classmethod
    def query_wrapper(cls, condition=None, **kwargs):
        conditions = condition if condition else list()
        if getattr(cls.model, "is_delete", None):
            conditions.append(getattr(cls.model, "is_delete") == 0)
        _sort = kwargs.get("_sort")
        if _sort is not None:
            # 需要去掉desc，不然会影响之前的sql执行
            kwargs.pop("_sort")
        # 遍历参数，当参数不为None的时候传递
        for k, v in kwargs.items():
            # 判断是否是like的情况
            like = isinstance(v, str) and (v.startswith("%") or v.endswith("%"))
            if like and len(v) == 2:
                continue
            # 如果是like模式，则使用Model.字段.like 否则用 Model.字段 等于
            DatabaseHelper.where(v, getattr(cls.model, k).like(v) if like else getattr(cls.model, k) == v,
                                 conditions)
        sql = select(cls.model).where(*conditions)
        if _sort and isinstance(_sort, tuple):
            for d in _sort:
                sql = getattr(sql, "order_by")(d)
        return sql

    @classmethod
    @RedisHelper.cache("dao")
    async def query_record(cls, session=None, **kwargs):
        try:
            if session:
                sql = cls.query_wrapper(**kwargs)
                result = await session.execute(sql)
                return result.scalars().first()
            async with async_session() as session:
                sql = cls.query_wrapper(**kwargs)
                result = await session.execute(sql)
                return result.scalars().first()
        except Exception as e:
            cls.log.error(f"查询{cls.model}失败, error: {e}")
            raise Exception(f"查询记录失败")

    @classmethod
    @RedisHelper.up_cache("dao")
    async def insert_record(cls, model, log=False, ss=None):
        try:
            if ss is None:
                async with async_session() as session:
                    async with session.begin():
                        session.add(model)
                        await session.flush()
                        session.expunge(model)
                    if log:
                        async with session.begin():
                            await asyncio.create_task(
                                cls.insert_log(session, model.operator, SqlOperationTypeEnum.ONLY_INSERT, model,
                                               key=model.id))
                    # 这里直接return了，不会继续走下面的add
                    return model
            ss.add(model)
            await ss.flush()
            ss.expunge(model)
            if log:
                await asyncio.create_task(
                    cls.insert_log(ss, model.operator, SqlOperationTypeEnum.ONLY_INSERT, model,
                                   key=model.id))
            return model
        except Exception as e:
            cls.log.error(f"添加{cls.model}记录失败, error: {e}")
            raise Exception(f"添加记录失败")

    @classmethod
    @RedisHelper.up_cache("dao")
    async def update_by_map(cls, emp_no, *condition, **kwargs):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = update(cls.model).where(*condition).values(**kwargs, update_date=datetime.now(),
                                                                     update_emp_no=emp_no)
                    await session.execute(sql)
        except Exception as e:
            cls.log.error(f"更新数据失败: {e}")
            raise Exception("更新数据失败")

    @classmethod
    @RedisHelper.up_cache("dao")
    async def update_record_by_id(cls, operator: int, model, not_null=False, log=False):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = cls.query_wrapper(id=model.id)
                    result = await session.execute(query)
                    now = result.scalars().first()
                    if now is None:
                        raise Exception("数据不存在")
                    old = deepcopy(now)
                    changed = DatabaseHelper.update_model(now, model, operator, not_null)
                    await session.flush()
                    session.expunge_all()
                if log:
                    async with session.begin():
                        await asyncio.create_task(
                            cls.insert_log(session, operator, SqlOperationTypeEnum.ONLY_UPDATE, now, old, model.id,
                                           changed=changed))
                return now
        except Exception as e:
            cls.log.error(f"更新{cls.model}记录失败, error: {e}")
            raise Exception(f"更新数据失败")

    @classmethod
    async def _inner_delete(cls, session, operator, value, log, key, exists):
        query = cls.query_wrapper(**{key: value})
        result = await session.execute(query)
        original = result.scalars().first()
        if original is None:
            if exists:
                raise Exception("记录不存在")
            return None
        DatabaseHelper.delete_model(original, operator)
        await session.flush()
        session.expunge(original)
        if log:
            await asyncio.create_task(
                cls.insert_log(session, operator, SqlOperationTypeEnum.ONLY_DELETE, original, key=value))
            return original

    @classmethod
    @RedisHelper.up_cache("dao")
    async def delete_record_by_id(cls, session, operator: int, value: int, log=True, key='id', exists=True,
                                  session_begin=False):
        """
        逻辑删除
        Args:
            session:
            operator:
            value:
            log:
            key:
            exists:
            session_begin:

        Returns:

        """
        try:
            if session_begin:
                # 说明在外面已经开启了session
                return await cls._inner_delete(session, operator, value, log, key, exists)
            async with session.begin():
                return await cls._inner_delete(session, operator, value, log, key, exists)
        except Exception as e:
            cls.log.exception(f"删除{cls.model.__name__}记录失败: \n{e}")
            raise Exception(f"删除失败")

    @classmethod
    @RedisHelper.up_cache("dao")
    async def delete_records(cls, session, operator, id_list: List[int], column="id", log=True):
        try:
            for id_ in id_list:
                query = cls.query_wrapper(**{column: id_})
                result = await session.execute(query)
                original = result.scalars().first()
                if original is None:
                    continue
                    # raise Exception("记录不存在")
                DatabaseHelper.delete_model(original, operator)
                await session.flush()
                session.expunge(original)
                if log:
                    await asyncio.create_task(
                        cls.insert_log(session, operator, SqlOperationTypeEnum.ONLY_DELETE, original, key=id_))
        except Exception as e:
            cls.log.exception(f"删除{cls.model}记录失败, error: {e}")
            raise Exception(f"删除记录失败")

    @classmethod
    async def insert_log(cls, session, operator, mode, now, old=None, key=None, changed=None):
        """
        根据relation插入日志
        Args:
            session:
            operator:
            mode:
            now:
            old:
            key:
            changed:

        Returns:

        """
        diff, title = await cls.get_diff(session, mode, now, old, changed)
        tag = getattr(now, PikaAppConfig.TABLE_TAG, '未设置')
        diff_data = json.dumps(diff, ensure_ascii=False)
        model = PikaOperationLog(operator, mode, "&".join(title), tag, diff_data, key)
        session.add(model)

    @classmethod
    async def get_diff(cls, session, mode, now, old, changed):
        """
        根据新旧model获取2者的diff
        Args:
            session:
            mode:
            now:
            old:
            changed:

        Returns:

        """
        fields = getattr(now, PikaAppConfig.FIELD, None)
        # 根据要展示的字段数量(__show__)获取title数据
        fields_number = getattr(now, PikaAppConfig.SHOW_FIELD, 1)
        if fields:
            # 必须要展示至少1个字段
            fields = [f.name for f in fields[:fields_number]]
        else:
            fields = ['id']
        if not changed:
            if mode == SqlOperationTypeEnum.ONLY_INSERT:
                changed_fields = await cls.get_fields(now)
            else:
                changed_fields = []
        else:
            changed_fields = changed
        detail_fields = [c for c in changed_fields if
                         c not in fields] if mode != SqlOperationTypeEnum.ONLY_UPDATE else changed_fields
        result, title = [], []
        for f in detail_fields:
            item = await cls.get_field_alias(session, getattr(now, PikaAppConfig.RELATION, None), f, now, old)
            result.append(item)
        for d in fields:
            item = await cls.get_field_alias(session, getattr(now, PikaAppConfig.RELATION, None), d, now, old)
            title.append(f"{item.get('name')}={item.get('now')}")
        return result, title

    @classmethod
    async def get_id_list(cls, ids):
        if ids == "":
            return []
        if isinstance(ids, int):
            # 说明是多个id
            id_list = [ids]
        else:
            id_list = list(map(int, ids.split(",")))
        return id_list

    @classmethod
    async def fetch_id_with_name(cls, session, id_field, name_field, old_id, new_id):
        """
        通过id查询name等字段数据
        Args:
            session:
            id_field:
            name_field:
            old_id:
            new_id:

        Returns:

        """
        cls_ = id_field.parent.class_
        if old_id is None:
            id_list = await cls.get_id_list(new_id)
            data = await session.execute(select(cls_).where(getattr(cls_, id_field.name).in_(id_list)))
            result = data.scalars().all()
            if result is None:
                return new_id, None
            ans = []
            for r in result:
                ans.append(getattr(r, name_field.name, new_id))
            return ",".join(map(str, ans)), None
        new_list = await cls.get_id_list(new_id)
        old_list = await cls.get_id_list(old_id)
        id_list = old_list + new_list
        data = await session.execute(select(cls_).where(getattr(cls_, id_field.name).in_(id_list)))
        # old_value, new_value = old_id, new_id
        old_ans, new_ans = [], []
        mp = dict()
        for d in data.scalars():
            mp[getattr(d, id_field.name, None)] = getattr(d, name_field.name, None)
        for t in old_list:
            old_ans.append(mp.get(t, t))
        for i in new_list:
            new_ans.append(mp.get(i, i))
        return ",".join(map(str, new_ans)), ",".join(map(str, old_ans))

    @classmethod
    def get_json_field(cls, field):
        """
        遇到datetime等类型，进行转换
        Args:
            field:

        Returns:

        """
        if isinstance(field, datetime):
            return field.strftime("%Y-%m-%d %H:%M:%S")
        return field

    @classmethod
    async def get_field_alias(cls, session, relation: Tuple[PikaRelationField], name, now, old=None):
        """
        获取别名操作，如果字段是别的表的主键，则还需要根据此字段查询别的表的对应字段
        Args:
            session:
            relation: relation有2个值，第一个值是别的表对应的主键，第二个值是要显示的字段
            name:
            now:
            old:

        Returns:
        """
        alias = getattr(now, PikaAppConfig.ALIAS, {})
        current_value = getattr(now, name, None)
        current_value = cls.get_json_field(current_value)
        old_value = getattr(old, name, None) if old is not None else None
        old_value = cls.get_json_field(old_value)
        if relation is not None:
            for r in relation:
                if r.field.name == name:
                    # 说明是id类型，需要转换为中文
                    if r.foreign is None:
                        return dict(name=alias.get(name, name), old=old_value, now=current_value)
                    if callable(r.foreign):
                        # foreign支持方法和数据库其他表，如果callable为True 说明是function
                        # 参考 ProjectRoleEnum.name方法 里面将int转为具体角色的方法
                        real_value = r.foreign(current_value)
                        real_old_value = r.foreign(old_value)
                        return dict(name=alias.get(name, name), old=real_old_value, now=real_value)
                    # 更新字段
                    id_field, name_field = r.foreign
                    current, old = await cls.fetch_id_with_name(session, id_field, name_field, old_value, current_value)
                    return dict(name=alias.get(name, name), old=old, now=current)
        return dict(name=alias.get(name, name), old=old_value, now=current_value)

    @classmethod
    async def get_fields(cls, model):
        """
        遍历字段，排除掉被忽略的字段
        Args:
            model:

        Returns:

        """
        ans = []
        fields = getattr(model, PikaAppConfig.FIELD, None)
        fields = [x.name for x in fields] if fields else list()
        for c in model.__table__.columns:
            if c.name in PikaAppConfig.IGNORE_FIELDS or (fields and c.name not in fields):
                continue
            ans.append(c.name)
        return ans

    @classmethod
    @RedisHelper.up_cache("dao")
    async def delete_by_id(cls, id):
        """
        物理删除
        Args:
            id:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    query = cls.query_wrapper(id=id)
                    result = await session.execute(query)
                    original = result.scalars().first()
                    if original is None:
                        raise Exception("记录不存在")
                    session.delete(original)
        except Exception as e:
            cls.log.error(f"逻辑删除{cls.model}记录失败, error: {e}")
            raise Exception(f"删除记录失败")
