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
import copy
import functools
from datetime import datetime
from typing import Any, Callable, Iterable, List, TypeVar

from config import PikaAppConfig
from custard.time import Moment
from dictdiffer import diff
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.handler.asyncsql import AsyncDbSession
from app.core.handler.jsonres import PikaJsonEncoder, PikaResponse
from app.core.handler.logger import PikaLogger
from app.enums.OperationEnum import SqlOperationTypeEnum
from app.enums.SysVarEnum import ValidTimeEnum
from app.exceptions import DbDeleteError, DbException, DbUpdateError
from app.middleware.xredis import RedisHelper
from app.models import async_db_session_generator, async_session
from app.models.basic import LargeBaseModel
from app.models.system import OperationLogModel

Transaction = TypeVar("Transaction", bool, Callable)


class PikaMdWrapper:
    def __init__(self, model, log=None):
        self.__model__ = model
        if log is None:
            self.__log__ = PikaLogger(f"{model.__name__}")
        else:
            self.__log__ = log

    def __call__(self, cls):
        cls.__model__ = self.__model__
        cls.__log__ = self.__log__
        return cls

    @classmethod
    def obj_to_dic(cls, obj):
        """
        Object转型为dict
        Args:
            obj:

        Returns:
        """
        dic = {}
        for field_key in dir(obj):
            field_value = getattr(obj, field_key)
            if not field_key.startswith("__") and not callable(field_value) and not field_key.startswith("_"):
                dic[field_key] = field_value
        return dic


def db_connect(transaction: Transaction = False):
    """
    装饰器,支持自动创建session,支持事务 自动获取session连接,简化model相关操作
    Args:
        transaction: 是否开启事务,开启则会被session.begin包裹

    Returns:

    """
    if callable(transaction):
        # 说明装饰器非参数模式
        @functools.wraps(transaction)
        async def wrap(cls, *args, **kwargs):
            try:
                session: AsyncSession = kwargs.pop("session", None)
                if session is not None:
                    return await transaction(cls, *args, session=session, **kwargs)
                async with async_db_session_generator() as session_:
                    return await transaction(cls, *args, session=session_, **kwargs)
            except Exception as e:
                # 这边调用cls本身的log参数,写入日志+抛出异常
                cls.__log__.error(f"操作{cls.__model__.__name__}失败: {e}")
                raise DbException(f"操作数据库失败: {e}")

        return wrap

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(cls, *args, **kwargs):
            try:
                session: AsyncSession = kwargs.pop("session", None)
                nb = kwargs.get("not_begin")
                if session is not None:
                    if transaction and nb:
                        async with session.begin():
                            return await func(cls, *args, session=session, **kwargs)
                    return await func(cls, *args[1:], session=session, **kwargs)
                async with async_db_session_generator() as session_generator:
                    if transaction and nb:
                        async with session_generator.begin():
                            return await func(cls, *args, session=session_generator, **kwargs)
                    return await func(cls, *args, session=session_generator, **kwargs)
            except Exception as e:
                cls.__log__.error(f"操作{cls.__model__.__name__}失败: {e}")
                raise DbException(f"操作数据库失败: {e}")

        return wrapper

    return decorator


# Mapper单表类,类似mybatis-plus
class PikaWrapper(object):
    __log__ = PikaLogger("LargeBaseModel")
    __model__ = LargeBaseModel

    @classmethod
    async def opt_exec_err(cls, __log__, detail, exc=Exception):
        await __log__(detail)
        raise exc if exc else True

    @classmethod
    @RedisHelper.cache("dao", expired_time=ValidTimeEnum.GLOBAL_SELECT_LIST_TIME.value)
    @db_connect
    async def select_list(cls, *, session: AsyncSession = None, condition: list = None, **kwargs):
        """
        基础model查询条件
        Args:
            session:
            condition: 自定义查询条件
            **kwargs: 普通查询条件

        Returns:

        """
        sql = cls.query_wrapper(condition, **kwargs)
        result = await session.execute(sql)
        return result.scalars().all()

    @staticmethod
    def like(s: str):
        if s:
            return f"%{s}%"
        return s

    @staticmethod
    def right_like(s: str):
        if s:
            return f"{s}%"
        return s

    @staticmethod
    def left_like(s: str):
        if s:
            return f"%{s}"
        return s

    @staticmethod
    async def pagination(page_index: int, page_size: int, session, sql: str, scalars=True, **kwargs):
        """
        分页查询
        Args:
            page_index:
            page_size:
            session:
            sql:
            scalars:

        Returns:

        """
        data = await session.execute(sql)
        total = data.raw.rowcount
        if total == 0:
            return [], 0
        sql = sql.offset((page_index - 1) * page_size).limit(page_size)
        data = await session.execute(sql)
        if scalars and kwargs.get("_join") is None:
            return data.scalars().all(), total
        return data.all(), total

    @staticmethod
    def update_model(dist, source, operator=None, not_null=False):
        """
        更新model
        Args:
            dist:
            source:
            operator:
            not_null:

        Returns:

        """
        changed = []
        for var, value in vars(source).items():
            if not_null:
                if value is None:
                    continue
                if isinstance(value, (bool, int)) or value:
                    # 如果是bool值或者int, false和0也是可以接受的
                    if not hasattr(dist, var):
                        continue
                    if getattr(dist, var) != value:
                        changed.append(var)
                        setattr(dist, var, value)
            else:
                if getattr(dist, var) != value:
                    changed.append(var)
                    setattr(dist, var, value)
        if operator:
            dist.update_emp_no = operator
        dist.updated_date = Moment.get_now_time()
        return changed

    @staticmethod
    def delete_model(dist, operator):
        """
        删除数据,兼容老的deleted_at
        :param dist:
        :param operator:
        :return:
        """
        if str(dist.__class__.delete_date.property.columns[0].type) == "DATETIME":
            dist.delete_date = Moment.get_now_time()
        else:
            dist.delete_date = Moment.get_now_time("13timestamp")
        dist.update_date = datetime.now()
        dist.delete_flag = 1
        dist.update_emp_no = operator

    @classmethod
    @RedisHelper.cache("dao")
    @db_connect
    async def list_with_pagination(cls, paging, *, session=None, **kwargs):
        """
        通过分页获取数据
        Args:
            session:
            paging:
            **kwargs:

        Returns:

        """
        return await cls.pagination(paging.page_index, paging.page_size, session, cls.query_wrapper(**kwargs), **kwargs)

    @classmethod
    def where(cls, param: Any, sentence, condition: list):
        """
        根据where语句的内容,决定是否生成对应的sql
        Args:
            param:
            sentence:
            condition:

        Returns:

        """
        if param is None:
            return cls
        if isinstance(param, bool):
            condition.append(sentence)
            return cls
        if isinstance(param, int):
            condition.append(sentence)
            return cls
        if param:
            condition.append(sentence)
        return cls

    @classmethod
    def query_wrapper(cls, condition=None, **kwargs):
        """
        包装查询条件,支持like, == 和自定义条件(condition)
        Args:
            condition:
            **kwargs:

        Returns:

        """
        conditions = condition if condition else []
        if getattr(cls.__model__, "delete_flag", None):
            conditions.append(cls.__model__.delete_flag == 0)
        _sort = kwargs.pop("_sort", None)
        _select = kwargs.pop("_select", [])
        _join = kwargs.pop("_join", None)
        # 遍历参数,当参数不为None的时候传递
        for k, v in kwargs.items():
            # 判断是否是like的情况
            like = isinstance(v, str) and (v.startswith("%") or v.endswith("%"))
            if like and v == "%%":
                continue
            # 如果是like模式,则使用Model.字段.like 否则用 Model.字段 等于
            cls.where(v, getattr(cls.__model__, k).like(v) if like else getattr(cls.__model__, k) == v, conditions)
        sql = select(cls.__model__, *_select)
        if isinstance(_join, Iterable):
            for j in _join:
                sql = sql.outerjoin(*j)
        where = sql.where(*conditions)
        if _sort and isinstance(_sort, Iterable):
            for d in _sort:
                where = where.order_by(d)
        return where

    @classmethod
    @db_connect
    async def query_record(cls, session: AsyncSession = None, **kwargs):
        sql = cls.query_wrapper(**kwargs)
        result = await session.execute(sql)
        return result.scalars().first()

    @classmethod
    @RedisHelper.up_cache("dao")
    @db_connect(transaction=True)
    async def insert(cls, *, model: LargeBaseModel, session: AsyncSession = None, log=False, description=None):
        changed = PikaResponse.model_to_dict(model)
        session.add(model)
        await session.flush()
        session.expunge(model)
        if log:
            await asyncio.create_task(
                cls.insert_log(
                    session=session,
                    operator=model.create_emp_no,
                    mode=SqlOperationTypeEnum.ONLY_INSERT,
                    before={},
                    changed=changed,
                    description=description,
                ),
            )
        return model

    @classmethod
    @RedisHelper.up_cache("dao")
    async def update_by_map(cls, operator, *condition, **kwargs):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = (
                        update(cls.__model__)
                        .where(*condition)
                        .values(**kwargs, update_date=datetime.now(), update_emp_no=operator)
                    )
                    await session.execute(sql)
        except Exception as e:
            err_detail = f"更新数据失败: {e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, DbUpdateError)

    @classmethod
    @RedisHelper.up_cache("dao")
    @db_connect(transaction=True)
    async def update_record_by_id(cls, operator: str, model, not_null=False, log=False, session=None, description=None):
        try:
            query = cls.query_wrapper(id=model.id)
            result = await session.execute(query)
            now = result.scalars().first()
            if now is None:
                raise Exception("数据不存在")
            cls.update_model(now, model, operator, not_null)
            await session.flush()
            session.expunge_all()
            if log:
                before, changed = PikaResponse.model_to_dict(now), dict(model)
                await asyncio.create_task(
                    cls.insert_log(
                        session=session,
                        operator=operator,
                        mode=SqlOperationTypeEnum.ONLY_UPDATE,
                        before=before,
                        changed=changed,
                        key=model.id,
                        description=description,
                    ),
                )
            return now
        except Exception as e:
            err_detail = f"更新{cls.__model__.__name__}记录失败: \n{e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, DbUpdateError)

    @classmethod
    async def _inner_delete(cls, *, session, operator, value, key, log=False, description=None):
        """

        Args:
            session:
            operator:
            value:
            key:
            log:
            description:

        Returns:

        """
        try:
            query = cls.query_wrapper(**{key: value})
            result = await session.execute(query)
            original = result.scalars().first()
            if original is None:
                return None
            changed = copy.copy(original)
            cls.delete_model(original, operator)
            await session.flush()
            session.expunge(original)
            if log:
                await asyncio.create_task(
                    cls.insert_log(
                        session=session,
                        operator=operator,
                        changed=changed,
                        mode=SqlOperationTypeEnum.ONLY_DELETE,
                        key=value,
                        description=description,
                    ),
                )
                return original
        except Exception as e:
            err_detail = f"删除{cls.__model__.__name__}记录失败: \n{e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, DbDeleteError)

    @classmethod
    @RedisHelper.up_cache("dao")
    async def delete_record_by_id(
        cls, session, operator: str, value: str, key="id", log=False, description=None, session_begin=False,
    ):
        """
        逻辑删除
        Args:
            session:
            operator:
            value:
            key:
            log:
            description:
            session_begin:

        Returns:

        """
        try:
            mode = {
                "session": session,
                "operator": operator,
                "value": value,
                "key": key,
                "log": log,
                "description": description,
            }
            if session_begin:
                # 说明在外面已经开启了session
                return await cls._inner_delete(**mode)
            async with session.begin():
                return await cls._inner_delete(**mode)
        except Exception as e:
            err_detail = f"删除{cls.__model__.__name__}记录失败: \n{e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, DbDeleteError)

    @classmethod
    @RedisHelper.up_cache("dao")
    async def delete_records(cls, session, operator, id_list: List[str], column="id", description=None, log=True):
        try:
            for id_ in id_list:
                query = cls.query_wrapper(**{column: id_})
                result = await session.execute(query)
                original = result.scalars().first()
                if original is None:
                    continue
                    # raise DbException("记录不存在")
                cls.delete_model(original, operator)
                await session.flush()
                session.expunge(original)
                if log:
                    await asyncio.create_task(
                        cls.insert_log(
                            session=session,
                            operator=operator,
                            mode=SqlOperationTypeEnum.ONLY_DELETE,
                            before=original,
                            changed={},
                            key=id_,
                            description=description,
                        ),
                    )
        except Exception as e:
            err_detail = f"删除{cls.__model__.__name__}记录失败: \n{e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, DbDeleteError)

    @classmethod
    async def insert_log(cls, session, operator, mode, before=None, changed=None, key=None, description=None):
        """
        根据relation插入日志
        Args:
            session:
            operator:
            mode:
            before:
            changed:
            key:
            description:
        Returns:

        """
        model = OperationLogModel(operator=operator, mode=mode, description=description, key=key)
        if mode == SqlOperationTypeEnum.ONLY_UPDATE:
            diff_data = await cls.diff_data(before, changed)
        elif mode in (SqlOperationTypeEnum.ONLY_INSERT, SqlOperationTypeEnum.ONLY_DELETE):
            diff_data = changed
        model.key = model.id if key is None else key
        table_tag = getattr(model, PikaAppConfig.TABLE_TAG, False)
        model.tag = table_tag.get("comment", "") if table_tag else "未设置"
        model.diff_data = str(diff_data)
        session.add(model)

    @classmethod
    async def diff_data(cls, before, changed):
        """
        对比数据
        Args:
            before:
            changed:

        Returns:

        """
        (
            change,
            add,
            remove,
        ) = (
            {},
            {},
            {},
        )
        diff_result = list(diff(before, changed))
        for index in diff_result:
            left, middle, right = index[0], index[1], index[2]
            if left == "change":
                change[middle] = {"before": right[0], "changed": right[1]}
            elif left == "add":
                for item in right:
                    add[item[0]] = item[1]
            elif left == "remove":
                for item in right:
                    remove[item[0]] = item[1]
        diff_data = {"change": change, "add": add, "remove": remove}
        try:
            diff_data = PikaJsonEncoder.safe_json_dumps(diff_data, ensure_ascii=False)
        except Exception as e:
            err_detail = f"changed参数转换失败,model={cls.__model__}\tdiff_data={diff_data}, error: {e}"
            cls.opt_exec_err(cls.__log__.warning, err_detail, False)
        return diff_data

    @classmethod
    async def delete_by_id(cls, model, ids):
        """
        物理删除
        Args:
            model:
            ids:

        Returns:

        """
        del_sql = delete(model).where(model.id.in_(ids))
        return await AsyncDbSession.delete(ids=ids, do_sql=del_sql)
