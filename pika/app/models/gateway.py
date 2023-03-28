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
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint

from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.models.environment import EnvironmentModel


class GatewayModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_gateway"
    __table_args__ = (UniqueConstraint("env", "name"), {"comment": "请求网关地址表"})
    env = Column(BinaryUUID, ForeignKey(EnvironmentModel.id, ondelete="cascade", onupdate="cascade"), comment="环境id")
    name = Column(String(ByteSizeEnum.LENGTH_50), comment="网关名称")
    address = Column(String(ByteSizeEnum.LENGTH_128), comment="网关地址")

    def __init__(self, env, name, address, operator, id=None):
        super().__init__(id=id, operator=operator)
        self.name = name
        self.env = env
        self.address = address
