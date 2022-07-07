# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testcase_data.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import Column, INT, String, UniqueConstraint, TEXT

from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase


class PikaTestCaseData(PikaLargeBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_testcase_data"
    __table_args__ = (
        UniqueConstraint('env', 'case_id', 'name'),
        {"comment": "测试数据表, 用来存储各个环境下的测试数据，用于数据驱动"}
    )
    env = Column(INT, nullable=False, comment="环境")
    case_id = Column(INT, nullable=False, comment="用例id")
    name = Column(String(32), nullable=False, comment="名称")
    json_data = Column(TEXT, nullable=False, comment="json")

    def __init__(self, env, case_id, name, json_data, operator, id=None):
        super().__init__(operator, id)
        self.env = env
        self.case_id = case_id
        self.name = name
        self.json_data = json_data
