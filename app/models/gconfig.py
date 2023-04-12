# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gconfig.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :   全局变量
"""
from sqlalchemy import SMALLINT, Column, ForeignKey, String, TEXT, UniqueConstraint
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.core.handler.sqlbin_uuid import BinaryUUID
from app.models.environment import EnvironmentModel


class GConfigModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_gconfig'
    env = Column(BinaryUUID, ForeignKey(
        EnvironmentModel.id, ondelete="cascade", onupdate="cascade"), comment="环境id")
    key = Column(String(ByteSizeEnum.LENGTH_56), comment="key")
    value = Column(TEXT, comment="变量")
    key_type = Column(SMALLINT, nullable=False, comment="参数类型 0: string 1: json 2: yaml")

    __table_args__ = (
        UniqueConstraint('env', 'key'),
        {"comment": "全局变量配置表"}
    )

    def __init__(self, env, key, value, key_type, operator, enabled_flag, id=None):
        super().__init__(id=id, operator=operator, enabled_flag=enabled_flag)
        self.env = env
        self.key = key
        self.value = value
        self.key_type = key_type
