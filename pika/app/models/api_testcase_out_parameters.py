# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_out_parameters.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from uuid import uuid4

from sqlalchemy import SMALLINT, Column, String, UniqueConstraint

from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel


class ApiTestCaseOutParametersModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_testcase_out_parameters"
    __table_args__ = (UniqueConstraint("case_id", "name"), {"comment": "用例出参数据表,与用例绑定"})
    case_id = Column(BinaryUUID, default=uuid4, nullable=False, comment="用例id")
    name = Column(String(ByteSizeEnum.LENGTH_50), nullable=False, comment="参数名")
    source = Column(
        SMALLINT,
        nullable=False,
        server_default="0",
        comment="来源类型 0: Body(TEXT) 1: Body(JSON) 2: Header 3: Cookie 4: HTTP状态码",
    )
    expression = Column(String(ByteSizeEnum.LENGTH_128), comment="表达式")
    match_index = Column(String(ByteSizeEnum.LENGTH_16), comment="获取结果索引, 可以是random,也可以是all,还可以是数字")

    def __init__(self, name, source, case_id, operator, expression=None, match_index=None, id=None):
        super().__init__(id=id, operator=operator)
        self.name = name
        self.case_id = case_id
        self.expression = expression
        self.match_index = match_index
        self.source = source
