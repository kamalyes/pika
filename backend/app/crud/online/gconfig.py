# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gconfig.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from sqlalchemy import select

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.gconfig import PikaGConfig
from app.schema.gconfig import GConfigForm
from app.utils.decorator import dao


@dao(PikaGConfig, PikaLogger("GConfigDao"))
class GConfigDao(PikaMapper):

    @classmethod
    @RedisHelper.up_cache("dao")
    async def insert_gconfig(cls, form: GConfigForm, emp_no: int) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(PikaGConfig).where(PikaGConfig.env == form.env, PikaGConfig.key == form.key,
                                                  PikaGConfig.is_delete == 0))
                    data = query.scalars().first()
                    if data is not None:
                        raise Exception(f"变量: {data.key}已存在")
                    config = PikaGConfig(**form.dict(), emp_no=emp_no)
                    session.add(config)
        except Exception as e:
            cls.log.error(f"新增变量: {data.key}失败, {e}")
            raise Exception(f"新增变量: {data.key}失败")

    @staticmethod
    @RedisHelper.cache("dao", 1800, True)
    async def async_get_gconfig_by_key(key: str, env: int) -> PikaGConfig:
        try:
            filters = [PikaGConfig.key == key, PikaGConfig.is_delete == 0, PikaGConfig.is_usable is True,
                       PikaGConfig.env == env]
            async with async_session() as session:
                sql = select(PikaGConfig).where(*filters)
                result = await session.execute(sql)
                return result.scalars().first()
        except Exception as e:
            raise Exception(f"查询全局变量失败: {str(e)}")
