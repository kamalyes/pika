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

from sqlalchemy import select, or_
from app.crud import PikaWrapper, PikaMdWrapper
from app.models import async_session
from app.models.gateway import GatewayModel
from app.core.handler.exceres import KeyUndefinedException


@PikaMdWrapper(GatewayModel)
class GatewayDao(PikaWrapper):

    @classmethod
    async def query_gateway(cls, env, name=None, id=None):
        async with async_session() as session:
            query_sql = select(GatewayModel).where(or_(GatewayModel.delete_flag == 0,
                                                   GatewayModel.env == env,
                                                   GatewayModel.name == name,
                                                   GatewayModel.id == id))
            query_result = await session.execute(query_sql)
            data = query_result.scalars().first()
            if data is None:
                raise KeyUndefinedException(detail=f"此环境没有网关配置: {name}")
            return data.address
