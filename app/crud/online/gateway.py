# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gateway.py
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
from app.models import async_session
from app.models.gateway import GatewayModel
from app.utils.decorator import dao


@dao(GatewayModel, PikaLogger("PikaRedisConfigDao"))
class GatewayDao(PikaMapper):

    @staticmethod
    async def query_gateway(env, name):
        async with async_session() as session:
            query_sql = select(GatewayModel).where(GatewayModel.delete_flag == False,
                                                   GatewayModel.env == env,
                                                   GatewayModel.name == name)
            query_result = await session.execute(query_sql)
            data = query_result.scalars().first()
            if data is None:
                raise Exception(f"此环境没有网关配置: {name}")
            return data.gateway
