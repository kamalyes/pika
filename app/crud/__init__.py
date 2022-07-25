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
from typing import List

from dictdiffer import diff, swap
from sqlalchemy import select, update

from app.core.handler.execres import ValidException
from app.enums.OperationEnum import SqlOperationTypeEnum
from app.middleware.xredis import RedisHelper
from app.models import async_session, DatabaseHelper
from app.models.system import OperationLogModel
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
        if getattr(cls.model, "delete_flag", None):
            conditions.append(getattr(cls.model, "delete_flag") == 0)
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
            DatabaseHelper.where(v, getattr(cls.model, k).like(v) if like else getattr(cls.model,
                                                                                       k) == v,
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
    async def insert_record(cls, model, log=False, session=None, title=None):
        try:
            if session is None:
                async with async_session() as session:
                    async with session.begin():
                        session.add(model)
                        await session.flush()
                        session.expunge(model)
                    if log:
                        async with session.begin():
                            await asyncio.create_task(
                                cls.insert_log(session=session, operator=model.create_emp_no,
                                               mode=SqlOperationTypeEnum.ONLY_INSERT, changed=model,
                                               key=model.id, title=title))
                    # 这里直接return了，不会继续走下面的add
                    return model
            session.add(model)
            await session.flush()
            session.expunge(model)
            if log:
                await asyncio.create_task(
                    cls.insert_log(session=session, operator=model.create_emp_no,
                                   mode=SqlOperationTypeEnum.ONLY_INSERT, changed=model,
                                   key=model.id, title=title))
            return model
        except Exception as e:
            cls.log.error(f"添加{cls.model}记录失败, error: {e}")
            raise Exception(f"添加记录失败")

    @classmethod
    @RedisHelper.up_cache("dao")
    async def update_by_map(cls, operator, *condition, **kwargs):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = update(cls.model).where(*condition).values(**kwargs,
                                                                     update_date=datetime.now(),
                                                                     update_emp_no=operator)
                    await session.execute(sql)
        except Exception as e:
            cls.log.error(f"更新数据失败: {e}")
            raise Exception("更新数据失败")

    @classmethod
    @RedisHelper.up_cache("dao")
    async def update_record_by_id(cls, operator: str, model, not_null=False, log=False, title=None):
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
                            cls.insert_log(session=session, operator=operator,
                                           mode=SqlOperationTypeEnum.ONLY_UPDATE, before=old, changed=changed,
                                           key=model.id, title=title))
                return now
        except Exception as e:
            cls.log.error(f"更新{cls.model}记录失败, error: {e}")
            raise Exception(f"更新数据失败")

    @classmethod
    async def _inner_delete(cls, session, operator, value, log, key, exists, title=None):
        query = cls.query_wrapper(**{key: value})
        result = await session.execute(query)
        original = result.scalars().first()
        if original is None:
            if exists:
                raise ValidException(detail="记录不存在")
            return None
        DatabaseHelper.delete_model(original, operator)
        await session.flush()
        session.expunge(original)
        if log:
            await asyncio.create_task(
                cls.insert_log(session=session, operator=operator,
                               mode=SqlOperationTypeEnum.ONLY_DELETE, before=original, changed={},
                               key=value, title=title))
            return original

    @classmethod
    @RedisHelper.up_cache("dao")
    async def delete_record_by_id(cls, session, operator: str, value: int, log=True, key='id',
                                  exists=True,
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
            raise ValidException(detail=f"删除失败,\n{e}")

    @classmethod
    @RedisHelper.up_cache("dao")
    async def delete_records(cls, session, operator, id_list: List[int], column="id", title=None, log=True):
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
                        cls.insert_log(session=session, operator=operator,
                                       mode=SqlOperationTypeEnum.ONLY_DELETE, before=original, changed={},
                                       key=id_, title=title))
        except Exception as e:
            cls.log.exception(f"删除{cls.model}记录失败, error: {e}")
            raise Exception(f"删除记录失败")

    @classmethod
    async def insert_log(cls, session, operator, mode, before=None, changed=None, key=None, title=None):
        """
        根据relation插入日志
        Args:
            session:
            operator:
            mode:
            before:
            changed:
            key:
            title:
        Returns:

        """
        diff = await cls.get_diff(before, changed)
        table = before if before else changed
        table_args = getattr(table, PikaAppConfig.TABLE_TAG, [])
        diff_data = json.dumps(diff, ensure_ascii=False)
        tag = [tb_arg.get("comment") for tb_arg in table_args if isinstance(tb_arg, dict)]
        model = OperationLogModel(operator=operator, mode=mode, title=title,
                                  tag=tag[0], description=diff_data, key=key)
        session.add(model)

    @classmethod
    async def get_diff(cls, before, changed):
        """
        根据新旧model获取2者的diff
        Args:
            before:
            changed:

        Returns:

        """
        result = {}
        if before and changed:
            result = diff(**before.__dict__, **changed.__dict__)
        elif not before and changed:
            result = diff({}, **changed.__dict__)
        elif before and not changed:
            result = diff({}, **before.__dict__)
        swapped = swap(result)
        print("swapped", swapped)
        return swapped

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
