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

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase


class PikaGateway(PikaLargeBase):
    __tablename__ = f'{PikaGlobalVarEnum.APP_NAME_LOWER}_gateway'
    __table_args__ = (
        UniqueConstraint('env_id', 'name'),
    )
    env_id = Column(INT, comment='对应环境id')
    name = Column(String(ByteSizeEnum.LENGTH_50), comment="网关名称")
    address = Column(String(ByteSizeEnum.LENGTH_128), comment="网关地址")

    __fields__ = (name, env_id, address)
    __tag__ = "网关"
    __alias__ = dict(name="网关名称", env="环境", address="网关地址")
    __show__ = 2

    def __init__(self, env_id, name, address, operator, id=None):
        super().__init__(operator, id)
        self.name = name
        self.env = env_id
        self.address = address
