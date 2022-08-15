# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gateway.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  请求网关地址表
"""

from sqlalchemy import Column, INT, String, UniqueConstraint

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel


class GatewayModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_gateway'
    __table_args__ = (
        UniqueConstraint('env', 'name'), {"comment": "请求网关地址表"}
    )
    env = Column(INT, comment='对应环境id')
    name = Column(String(ByteSizeEnum.LENGTH_50), comment="网关名称")
    gateway = Column(String(ByteSizeEnum.LENGTH_128), comment="网关地址")

    def __init__(self, env, name, gateway, operator, id=None):
        super().__init__(operator, id)
        self.name = name
        self.env = env
        self.gateway = gateway
