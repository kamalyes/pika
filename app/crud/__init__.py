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
import functools
import json
from copy import deepcopy
from datetime import datetime
from typing import List, TypeVar, Callable, Any, Iterable

from dictdiffer import diff, swap
from hutools.time import Moment
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.handler.execres import ValidException
from app.core.handler.logger import PikaLogger
from app.enums.OperationEnum import SqlOperationTypeEnum
from app.excpetions.thirdparty.DbException import DbException
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.basic import LargeBaseModel
from app.models.system import OperationLogModel
from config import PikaAppConfig

Transaction = TypeVar("Transaction", bool, Callable)


class PikaMdWrapper:

    def __init__(self, model, log=None):
        self.__model__ = model
        if log is None:
            self.__log__ = PikaLogger(f"{model.__name__}")
        else:
            self.__log__ = log

    def __call__(self, cls):
        setattr(cls, "__model__", self.__model__)
        setattr(cls, "__log__", self.__log__)
        return cls


def db_connect(transaction: Transaction = False):
    """
    装饰器，支持自动创建session，支持事务 自动获取session连接，简化model相关操作
    Args:
        transaction: 是否开启事务，开启则会被session.begin包裹

    Returns:

    """
    if callable(transaction):
        # 说明装饰器非参数模式
        @functools.wraps(transaction)
        async def wrap(cls, *args, **kwargs):
            try:
                session = kwargs.get("session")
                if session is not None:
                    return await transaction(cls, *args, session=session, **kwargs)
                async with async_session() as session_:
                    return await transaction(cls, *args, session=session_, **kwargs)
            except Exception as e:
                # 这边调用cls本身的log参数，写入日志+抛出异常
                cls.__log__.error(f"操作Model: {cls.__model__.__name__}失败: {e}")
                raise DbException(f"操作数据库失败: {e}")

        return wrap

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(cls, *args, **kwargs):
            try:
                session: AsyncSession = kwargs.get("session")
                if session is not None:
                    if transaction:
                        async with session.begin():
                            return await func(cls, *args, session=session, **kwargs)
                    return await func(cls, *args[1:], session=session, **kwargs)
                async with async_session() as ss:
                    if transaction:
                        async with ss.begin():
                            return await func(cls, *args, session=ss, **kwargs)
                    return await func(cls, *args, session=ss, **kwargs)
            except Exception as e:
                cls.__log__.error(f"操作Model: {cls.__model__.__name__}失败: {e}")
                raise DbException(f"操作数据失败: {e}")

        return wrapper

    return decorator


# Mapper单表类，类似mybatis-plus
class PikaWrapper(object):
    __log__ = PikaLogger("LargeBaseModel")
    __model__ = LargeBaseModel

    @classmethod
    @RedisHelper.cache("dao")
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
    async def pagination(page: int, size: int, session, sql: str, scalars=True):
        """
        分页查询
        Args:
            page:
            size:
            session:
            sql:
            scalars:

        Returns:

        """
        data = await session.execute(sql)
        total = data.raw.rowcount
        if total == 0:
            return [], 0
        sql = sql.offset((page - 1) * size).limit(size)
        data = await session.execute(sql)
        if scalars:
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
                if isinstance(value, bool) or isinstance(value, int) or value:
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
            setattr(dist, 'update_emp_no', operator)
        setattr(dist, 'updated_date', Moment.get_now_time())
        return changed

    @staticmethod
    def delete_model(dist, operator):
        """
        删除数据，兼容老的deleted_at
        :param dist:
        :param operator:
        :return:
        """
        if str(dist.__class__.delete_date.property.columns[0].type) == "DATETIME":
            dist.delete_date = Moment.get_now_time()
        else:
            dist.delete_date = Moment.get_now_time("13timestamp")
        dist.update_date = datetime.now()
        dist.update_emp_no = operator

    @classmethod
    @RedisHelper.cache("dao")
    @db_connect
    async def list_record_with_pagination(cls, page, size, /, *, session=None, **kwargs):
        """
        通过分页获取数据
        Args:
            session:
            page:
            size:
            **kwargs:

        Returns:

        """
        return await cls.pagination(page, size, session, cls.query_wrapper(**kwargs))

    @classmethod
    def where(cls, param: Any, sentence, condition: list):
        """
        根据where语句的内容，决定是否生成对应的sql
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
        包装查询条件，支持like, == 和自定义条件(condition)
        Args:
            condition:
            **kwargs:

        Returns:

        """
        conditions = condition if condition else list()
        if getattr(cls.__model__, "delete_flag", None):
            conditions.append(getattr(cls.__model__, "delete_flag") == 0)
        _sort = kwargs.pop("_sort", None)
        # 遍历参数，当参数不为None的时候传递
        for k, v in kwargs.items():
            # 判断是否是like的情况
            like = isinstance(v, str) and (v.startswith("%") or v.endswith("%"))
            if like and v == "%%":
                continue
            # 如果是like模式，则使用Model.字段.like 否则用 Model.字段 等于
            cls.where(v,
                      getattr(cls.__model__, k).like(v) if like else getattr(cls.__model__, k) == v,
                      conditions)
        sql = select(cls.__model__).where(*conditions)
        if _sort and isinstance(_sort, Iterable):
            for d in _sort:
                sql = getattr(sql, "order_by")(d)
        return sql

    @classmethod
    @RedisHelper.cache("dao")
    @db_connect
    async def query_record(cls, session: AsyncSession = None, **kwargs):
        sql = cls.query_wrapper(**kwargs)
        result = await session.execute(sql)
        return result.scalars().first()

    @classmethod
    @RedisHelper.up_cache("dao")
    @db_connect(transaction=True)
    async def insert(cls, *, model: LargeBaseModel, session: AsyncSession = None, log=False):
        session.add(model)
        await session.flush()
        session.expunge(model)
        if log:
            await asyncio.create_task(
                cls.insert_log(session, model.create_emp_no, SqlOperationTypeEnum.ONLY_INSERT,
                               model,
                               key=model.id))
        return model

    @classmethod
    @RedisHelper.up_cache("dao")
    async def update_by_map(cls, operator, *condition, **kwargs):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = update(cls.__model__).where(*condition).values(**kwargs,
                                                                         update_date=datetime.now(),
                                                                         update_emp_no=operator)
                    await session.execute(sql)
        except Exception as e:
            cls.__log__.error(f"更新数据失败: {e}")
            raise Exception("更新数据失败")

    @classmethod
    @RedisHelper.up_cache("dao")
    @db_connect(transaction=True)
    async def update_record_by_id(cls, operator: str, model, not_null=False, log=False, title=None,
                                  session=None):
        query = cls.query_wrapper(id=model.id)
        result = await session.execute(query)
        now = result.scalars().first()
        if now is None:
            raise Exception("数据不存在")
        old = deepcopy(now)
        changed = cls.update_model(now, model, operator, not_null)
        await session.flush()
        session.expunge_all()
        if log:
            await asyncio.create_task(
                cls.insert_log(session=session, operator=operator,
                               mode=SqlOperationTypeEnum.ONLY_UPDATE, before=old,
                               changed=changed,
                               key=model.id, title=title))

    @classmethod
    async def _inner_delete(cls, session, operator, value, log, key, exists, title=None):
        query = cls.query_wrapper(**{key: value})
        result = await session.execute(query)
        original = result.scalars().first()
        if original is None:
            if exists:
                raise ValidException(detail="记录不存在")
            return None
        cls.delete_model(original, operator)
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
            cls.__log__.exception(f"删除{cls.__model__.__name__}记录失败: \n{e}")
            raise ValidException(detail=f"删除失败,\n{e}")

    @classmethod
    @RedisHelper.up_cache("dao")
    async def delete_records(cls, session, operator, id_list: List[int], column="id", title=None,
                             log=True):
        try:
            for id_ in id_list:
                query = cls.query_wrapper(**{column: id_})
                result = await session.execute(query)
                original = result.scalars().first()
                if original is None:
                    continue
                    # raise Exception("记录不存在")
                cls.delete_model(original, operator)
                await session.flush()
                session.expunge(original)
                if log:
                    await asyncio.create_task(
                        cls.insert_log(session=session, operator=operator,
                                       mode=SqlOperationTypeEnum.ONLY_DELETE, before=original,
                                       changed={},
                                       key=id_, title=title))
        except Exception as e:
            cls.__log__.exception(f"删除{cls.__model__}记录失败, error: {e}")
            raise Exception(f"删除记录失败")

    @classmethod
    async def insert_log(cls, session, operator, mode, before=None, changed=None, key=None,
                         title=None):
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
    @db_connect(transaction=True)
    async def delete_by_id(cls, id, session=None):
        """
        物理删除
        Args:
            session:
            id:

        Returns:

        """
        query = cls.query_wrapper(id=id)
        result = await session.execute(query)
        original = result.scalars().first()
        if original is None:
            raise Exception("记录不存在")
        session.delete(original)
