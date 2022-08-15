# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  environment.py
@Time    :  2022/6/18 7:12 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  环境配置表
"""
from sqlalchemy import Column, String, UniqueConstraint

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel


class EnvironmentModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_environment'
    name = Column(String(ByteSizeEnum.LENGTH_50))
    __table_args__ = (UniqueConstraint('name'), {"comment": "环境配置"})

    def __init__(self, name, operator, description=None, id=None):
        super().__init__(id=id, operator=operator, description=description)
        self.name = name
