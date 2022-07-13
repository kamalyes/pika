# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  GconfigEnum.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :   全局变量
"""
from sqlalchemy import INT, Column, String, TEXT, UniqueConstraint

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel


class GConfigModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.APP_NAME_LOWER}_gconfig'
    env = Column(INT, comment="环境")
    key = Column(String(ByteSizeEnum.LENGTH_56), comment="key")
    value = Column(TEXT, comment="变量")
    key_type = Column(INT, nullable=False, comment="参数类型 0: string 1: json 2: yaml")

    __table_args__ = (
        UniqueConstraint('env', 'key'),
    )

    def __init__(self, env, key, value, key_type, operator, enabled_flag, id=None):
        super().__init__(operator, enabled_flag, id)
        self.env = env
        self.key = key
        self.value = value
        self.key_type = key_type
