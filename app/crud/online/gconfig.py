# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  GconfigEnum.py
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
from app.models.gconfig import GConfigModel
from app.schema.gconfig import GConfigForm
from app.utils.decorator import dao


@dao(GConfigModel, PikaLogger("GConfigDao"))
class GConfigDao(PikaMapper):

    @classmethod
    @RedisHelper.up_cache("dao")
    async def insert_gconfig(cls, form: GConfigForm, operator_emp_no: int) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(GConfigModel).where(GConfigModel.env == form.env,
                                                   GConfigModel.key == form.key,
                                                   GConfigModel.is_delete == 0))
                    data = query.scalars().first()
                    if data is not None:
                        raise Exception(f"变量: {data.key}已存在")
                    config = GConfigModel(**form.dict(), operator=operator_emp_no)
                    session.add(config)
        except Exception as e:
            cls.log.error(f"新增变量: {form.key}失败, {e}")
            raise Exception(f"新增变量: {form.key}失败")

    @staticmethod
    @RedisHelper.cache("dao", 1800, True)
    async def async_get_gconfig_by_key(key: str, env: int) -> GConfigModel:
        try:
            filters = [GConfigModel.key == key, GConfigModel.is_delete == 0,
                       GConfigModel.is_usable is True,
                       GConfigModel.env == env]
            async with async_session() as session:
                sql = select(GConfigModel).where(*filters)
                result = await session.execute(sql)
                return result.scalars().first()
        except Exception as e:
            raise Exception(f"查询全局变量失败: {str(e)}")
