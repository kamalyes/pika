# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  environment.py
@Time    :  2022/6/18 7:12 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import Column, String, UniqueConstraint

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import GlobalVarEnum
from app.models.basic import PikaLargeBase


class Environment(PikaLargeBase):
    __tablename__ = f'{GlobalVarEnum.APP_NAME_LOWER}_environment'
    name = Column(String(ByteSizeEnum.LENGTH_16))

    __table_args__ = (UniqueConstraint('name'),)

    __fields__ = [name]
    __tag__ = "环境配置"
    __alias__ = dict(name="名称")

    def __init__(self, name, operator, description=None, id=0):
        super().__init__(operator, description, id)
        self.name = name
