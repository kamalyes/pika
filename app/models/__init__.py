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
import time
import traceback
from contextlib import contextmanager, asynccontextmanager
from datetime import datetime
from typing import AsyncGenerator, AsyncIterator, List

import aioredis
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.handler.execres import (
    DbExecuteException,
    OperationException,
    AuthException,
    ValidException,
    AccessException,
    ThirdException, RedisException, RegisterException, SystemException)
from app.enums.database import DatabaseEnum
from app.enums.statuscode import SysFailedCodeEnum
from config import PikaAppConfig

# 同步engine
engine = create_engine(PikaAppConfig.SQLALCHEMY_DATABASE_URI, pool_recycle=1500)
sync_session = sessionmaker(engine, autocommit=False)

# 异步engine
async_engine = create_async_engine(PikaAppConfig.ASYNC_SQLALCHEMY_URI, pool_recycle=1500)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async_redis = aioredis.from_url(f'redis://{PikaAppConfig.REDIS_HOST}',
                                password=PikaAppConfig.REDIS_PASSWORD,
                                db=PikaAppConfig.REDIS_DB,
                                port=PikaAppConfig.REDIS_PORT,
                                encoding="utf-8", decode_responses=True)


async def async_create_table():
    """
    初始化创建表结构
    Returns:
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@contextmanager
def sync_db_session():
    """
    同步db
    Returns:
    """
    session = sync_session()
    try:
        yield session
        session.commit()
    except OperationException as operation_error:
        raise operation_error
    except AuthException as auth_err:
        raise auth_err
    except ValidException as valid_err:
        raise valid_err
    except AccessException as access_err:
        raise access_err
    except ThirdException as third_err:
        raise third_err
    except RedisException as redis_err:
        raise redis_err
    except RegisterException as register_err:
        raise register_err
    except SystemException as sys_err:
        raise sys_err
    except Exception as e:
        session.rollback()
        raise DbExecuteException(
            code=SysFailedCodeEnum.SQL_OPERATION_ERROR,
            detail=f"数据操作失败，错误原因：{traceback.format_exc()}",
        )
    finally:
        session.close()


async def get_async_session():
    """
    获取异步session
    :return:
    """
    async with async_session() as session:
        yield session


@asynccontextmanager
async def async_db_session() -> AsyncGenerator:
    """
    异步db
    Returns:
    """
    session = async_session()
    try:
        yield session
        await session.commit()
    except OperationException as operation_error:
        raise operation_error
    except AuthException as auth_err:
        raise auth_err
    except ValidException as valid_err:
        raise valid_err
    except AccessException as access_err:
        raise access_err
    except ThirdException as third_err:
        raise third_err
    except RedisException as redis_err:
        raise redis_err
    except RegisterException as register_err:
        raise register_err
    except SystemException as sys_err:
        raise sys_err
    except Exception as e:
        await session.rollback()
        raise DbExecuteException(
            code=SysFailedCodeEnum.SQL_OPERATION_ERROR,
            detail=f"数据操作失败，错误原因：{traceback.format_exc()}",
        )
    finally:
        await session.close()


async def pagination_db() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session


class DatabaseHelper(object):

    def __init__(self):
        # cache
        self.connections = dict()

    async def get_connection(self, sql_type: int, host: str, port: int, username: str, password: str, database: str):
        # 拼接key
        key = f"{host}:{port}:{database}:{username}:{password}:{database}"
        connection = self.connections.get(key)
        # 先判断是否已经有connection了，如果有则直接返回
        if connection is not None:
            return connection
        # 获取sqlalchemy需要的jdbc url
        jdbc_url = DatabaseHelper.get_jdbc_url(sql_type, host, port, username, password, database)
        # 创建异步引擎
        eg = create_async_engine(jdbc_url, pool_recycle=1500)
        ss = sessionmaker(bind=eg, class_=AsyncSession)
        # 将数据缓存起来
        data = dict(engine=eg, session=ss)
        self.connections[key] = data
        return data

    @staticmethod
    async def test_connection(ss):
        if ss is None:
            raise Exception("暂不支持的数据库类型")
        async with ss() as session:
            await session.execute("select 1")

    @staticmethod
    def get_jdbc_url(sql_type: int, host: str, port: int, username: str, password: str, database: str):
        if sql_type == DatabaseEnum.MYSQL:
            # mysql模式
            return f'mysql+aiomysql://{username}:{password}@{host}:{port}/{database}'
        if sql_type == DatabaseEnum.POSTGRESQL:
            return f'postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}'
        raise Exception("未知的数据库类型")

    def remove_connection(self, host: str, port: int, username: str, password: str, database: str):
        key = f"{host}:{port}:{database}:{username}:{password}:{database}"
        if self.connections.get(key):
            self.connections.pop(key)

    @staticmethod
    def update_model(dist, source, operator=None, not_null=False):
        """

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
        return changed

    @staticmethod
    def delete_model(dist, operator):
        """
        删除数据
        Args:
            dist:
            operator:

        Returns:

        """
        if str(dist.__class__.delete_date.property.columns[0].type) == "DATETIME":
            dist.delete_date = datetime.now()
        else:
            dist.delete_date = int(time.time() * 1000)
        dist.update_date = datetime.now()
        dist.update_emp_no = operator

    @classmethod
    def where(cls, param, sentence, condition: List):
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
    def like(s: str):
        if s:
            return f"%{s}%"
        return s


db_helper = DatabaseHelper()
