# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import traceback
from contextlib import contextmanager, asynccontextmanager
from typing import AsyncGenerator, AsyncIterator

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
    except Exception:
        session.rollback()
        raise DbExecuteException(
            code=SysFailedCodeEnum.SQL_OPERATION_ERROR,
            detail=f"数据操作失败，错误原因：{traceback.format_exc()}",
        )
    finally:
        session.close()


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
    except Exception:
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
