# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from contextlib import contextmanager, asynccontextmanager
from typing import AsyncGenerator, AsyncIterator
from urllib import parse
import uuid

import aioredis
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.handler.exceres import (
    DbExecuteException,
    ValidException)
from app.enums.DatabaseEnum import DatabaseTypeEnum
from app.enums.SysCodeEnum import ExcCodeEnum
from config import PikaAppConfig

# 同步engine
engine = create_engine(
    PikaAppConfig.SQLALCHEMY_DATABASE_URI,
    pool_recycle=PikaAppConfig.MYSQL_POOL_RECYCLE,
    encoding=PikaAppConfig.MYSQL_CHARSET)
sync_session = sessionmaker(engine, autocommit=False)

# 异步engine
async_engine = create_async_engine(
    PikaAppConfig.ASYNC_SQLALCHEMY_URI,
    pool_recycle=PikaAppConfig.MYSQL_POOL_RECYCLE,
    encoding=PikaAppConfig.MYSQL_CHARSET)
async_session = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async_redis = aioredis.from_url(f'redis://{PikaAppConfig.REDIS_HOST}',
                                password=PikaAppConfig.REDIS_PASSWORD,
                                db=PikaAppConfig.REDIS_DB_INDEX,
                                port=PikaAppConfig.REDIS_PORT,
                                encoding=PikaAppConfig.REDIS_ENCODING,
                                decode_responses=PikaAppConfig.REDIS_DECODE_RESPONSES)


async def async_create_table():
    """
    初始化创建表结构
    Returns:
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def async_db_session_generator() -> AsyncGenerator:
    """
    异步db
    Returns:
    """
    session = async_session()
    try:
        yield session
        await session.commit()
    except SQLAlchemyError as sql_exc:
        await session.rollback()
        raise DbExecuteException(
            code=ExcCodeEnum.SQL_OPERATION_ERROR,
            detail=f"数据操作失败,错误原因：{sql_exc}",
        )
    finally:
        await session.close()


async def async_db_session_iterator() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session


class DatabaseHelper(object):

    def __init__(self):
        # cache
        self.connections = dict()

    async def get_connection(self, sql_type: int, host: str, port: int, username: str,
                             password: str, database: str):
        # 拼接key
        password = parse.quote_plus(password)
        key = f"{host}:{port}:{database}:{username}:{password}:{database}"
        connection = self.connections.get(key)
        # 先判断是否已经有connection了,如果有则直接返回
        if connection is not None:
            return connection
        # 获取sqlalchemy需要的jdbc url
        jdbc_url = DatabaseHelper.get_jdbc_url(
            sql_type, host, port, username, password, database)
        # 创建异步引擎
        eg = create_async_engine(
            jdbc_url, pool_recycle=PikaAppConfig.MYSQL_POOL_RECYCLE)
        ss = sessionmaker(bind=eg, class_=AsyncSession)
        # 将数据缓存起来
        data = dict(engine=eg, session=ss)
        self.connections[key] = data
        return data

    @staticmethod
    async def test_connection(ss):
        if ss is None:
            raise ValidException("暂不支持的数据库类型")
        async with ss() as session:
            await session.execute("select 1")

    @staticmethod
    def get_jdbc_url(sql_type: int, host: str, port: int, username: str, password: str,
                     database: str):
        if sql_type == DatabaseTypeEnum.MYSQL:
            # mysql模式
            return f'mysql+aiomysql://{username}:{password}@{host}:{port}/{database}'
        if sql_type == DatabaseTypeEnum.POSTGRESQL:
            return f'postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}'
        raise ValidException(detail="未知的数据库类型")

    def remove_connection(self, host: str, port: int, username: str, password: str, database: str):
        key = f"{host}:{port}:{database}:{username}:{password}:{database}"
        if self.connections.get(key):
            self.connections.pop(key)


db_helper = DatabaseHelper()
