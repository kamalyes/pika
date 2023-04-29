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

from app.crud import PikaMdWrapper, PikaWrapper
from app.enums.SysVarEnum import ValidTimeEnum
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.gconfig import GConfigModel
from app.schema.gconfig import GConfigSchema
from sqlalchemy import select


@PikaMdWrapper(GConfigModel)
class GConfigDao(PikaWrapper):
    @classmethod
    @RedisHelper.up_cache("dao")
    async def insert_gconfig(cls, form: GConfigSchema, operator: str) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(GConfigModel).where(
                            GConfigModel.env == form.env,
                            GConfigModel.key == form.key,
                            GConfigModel.delete_flag == 0,
                        ),
                    )
                    data = query.scalars().first()
                    if data is not None:
                        raise Exception("变量: {data.key}已存在")
                    config = GConfigModel(**form.dict(), operator=operator)
                    session.add(config)
        except Exception as e:
            err_detail = f"新增变量: {form.key}失败, {e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    @RedisHelper.cache("dao", ValidTimeEnum.DAO_TIME.value, True)
    async def async_get_gconfig_by_key(cls, key: str, env: str) -> GConfigModel:
        try:
            filters = [
                GConfigModel.key == key,
                GConfigModel.delete_flag == 0,
                GConfigModel.enabled_flag is True,
                GConfigModel.env == env,
            ]
            async with async_session() as session:
                sql = select(GConfigModel).where(*filters)
                result = await session.execute(sql)
                return result.scalars().first()
        except Exception as e:
            err_detail = f"查询全局变量失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)
