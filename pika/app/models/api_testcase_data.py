# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_data.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from uuid import uuid4

from sqlalchemy import TEXT, Column, ForeignKey, String, UniqueConstraint

from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.models.environment import EnvironmentModel


class ApiTestCaseDataModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_testcase_data"
    __table_args__ = (
        UniqueConstraint("env", "case_id", "name"),
        {"comment": "测试数据表, 用来存储各个环境下的测试数据,用于数据驱动"},
    )
    env = Column(BinaryUUID, ForeignKey(EnvironmentModel.id, ondelete="cascade", onupdate="cascade"), comment="环境id")
    case_id = Column(BinaryUUID, default=uuid4, nullable=False, comment="用例id")
    name = Column(String(ByteSizeEnum.LENGTH_50), nullable=False, comment="名称")
    json_data = Column(TEXT, nullable=False, comment="json")

    def __init__(self, env, case_id, name, json_data, operator, id=None):
        super().__init__(id=id, operator=operator)
        self.env = env
        self.case_id = case_id
        self.name = name
        self.json_data = json_data
