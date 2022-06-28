# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gconfig.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :   全局变量
"""
from sqlalchemy import INT, Column, String, TEXT, UniqueConstraint

from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase


class PikaGConfig(PikaLargeBase):
    __tablename__ = f'{PikaGlobalVarEnum.APP_NAME_LOWER}_gconfig'
    env = Column(INT)
    key = Column(String(16))
    value = Column(TEXT)
    key_type = Column(INT, nullable=False, comment="0: string 1: json 2: yaml")

    __table_args__ = (
        UniqueConstraint('env', 'key'),
    )

    __fields__ = (env, key)
    __tag__ = "全局变量"
    __alias__ = dict(env="环境", key="名称", key_type="类型", value="值")
    __show__ = 2

    def __init__(self, env, key, value, key_type, emp_no, id=None):
        super().__init__(emp_no, id)
        self.env = env
        self.key = key
        self.value = value
        self.key_type = key_type
