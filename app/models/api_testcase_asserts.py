# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_asserts.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from uuid import uuid4
from sqlalchemy import Column, String, TEXT
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.core.handler.sqlbin_uuid import BinaryUUID


class ApiTestCaseAssertsModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_testcase_asserts'
    __table_args__ = {"comment": "断言表"}
    name = Column(String(ByteSizeEnum.LENGTH_50),
                  nullable=False, comment="名称")
    case_id = Column(BinaryUUID,
                     default=uuid4, index=True, comment="用例id")
    assert_type = Column(String(ByteSizeEnum.LENGTH_16),
                         comment="断言类型 equal: 等于 not_equal: 不等于 in: 属于")
    expected = Column(TEXT, nullable=False, comment="预期结果")
    actually = Column(TEXT, nullable=False, comment="实际结果")

    def __init__(self, name, case_id, assert_type, expected, actually, operator):
        super().__init__(operator=operator)
        self.name = name
        self.case_id = case_id
        self.assert_type = assert_type
        self.expected = expected
        self.actually = actually
