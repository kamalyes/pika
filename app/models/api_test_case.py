# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_test_case.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import List
from uuid import uuid4
from sqlalchemy import Column, String, SMALLINT, TEXT, SMALLINT, UniqueConstraint
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.models.basic import LargeBaseModel
from app.core.handler.sqlbin_uuid import BinaryUUID


class ApiTestCaseModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_testcase"
    # 调整联合唯一索引
    __table_args__ = (UniqueConstraint(
        'directory_id', 'name'), {"comment": "测试用例表"})
    name = Column(String(ByteSizeEnum.LENGTH_50), index=True, comment="名称")
    request_type = Column(
        SMALLINT, default=1, comment="请求类型 1: http 2: grpc 3: dubbo")
    url = Column(TEXT, nullable=False, comment="请求url")
    request_method = Column(String(ByteSizeEnum.LENGTH_12), nullable=True,
                            comment="请求方式, 如果非http可为空")
    request_headers = Column(TEXT, comment="请求头,可为空")
    base_path = Column(String(ByteSizeEnum.LENGTH_24), comment="请求base_path")
    body = Column(TEXT, comment="请求body")
    body_type = Column(
        SMALLINT, comment="请求类型, 0: none 1: json 2: form 3: x-form 4: binary 5: GraphQL")
    directory_id = Column(BinaryUUID,
                          default=uuid4, comment="所属目录")
    tag = Column(String(ByteSizeEnum.LENGTH_64), comment="用例标签")
    status = Column(SMALLINT, comment="用例状态: 1: 调试中 2: 暂时关闭 3: 正常运作")
    priority = Column(String(ByteSizeEnum.LENGTH_03), comment="用例优先级: p0-p3")
    case_type = Column(SMALLINT, comment="0: 普通用例 1: 前置用例 2: 数据工厂")
    out_parameters: List[ApiTestCaseOutParametersModel] = None

    def __init__(self, name, request_type, url, directory_id, status, priority, operator,
                 body_type=1, base_path=None, out_parameters=None,
                 tag=None, request_headers=None, case_type=0, body=None, request_method=None,
                 id=None):
        super().__init__(id=id, operator=operator)
        self.name = name
        self.request_type = request_type
        self.url = url
        self.priority = priority
        self.directory_id = directory_id
        self.tag = tag
        self.status = status
        self.out_parameters = out_parameters
        self.body_type = body_type
        self.case_type = case_type
        self.body = body
        self.request_headers = request_headers
        self.request_method = request_method
        self.base_path = base_path

    def __str__(self):
        return f"[用例: {self.name}]({self.id}))"
