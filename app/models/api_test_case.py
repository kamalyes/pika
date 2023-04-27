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
from sqlalchemy import Column, String, SMALLINT, TEXT, SMALLINT, UniqueConstraint, ForeignKey
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.api_testcase_directory import ApiTestCaseDirectoryModel
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.models.basic import ApiGBaseModel
from app.core.handler.sqlbin_uuid import BinaryUUID


class ApiTestCaseModel(ApiGBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_testcase"
    # 调整联合唯一索引
    __table_args__ = (UniqueConstraint('directory_id', 'name'), {"comment": "测试用例表"})
    name = Column(String(ByteSizeEnum.LENGTH_50), index=True, comment="名称")
    directory_id = Column(BinaryUUID, 
                       ForeignKey(ApiTestCaseDirectoryModel.id, ondelete="cascade", onupdate="cascade"),
                       comment="所属module")
    status = Column(SMALLINT, comment="用例状态: 1: 调试中 2: 暂时关闭 3: 正常运作")
    case_type = Column(SMALLINT, comment="0: 普通用例 1: 前置用例 2: 数据工厂")
    out_parameters: List[ApiTestCaseOutParametersModel] = None
    del ApiGBaseModel.cost

    def __init__(self, name, protocol, directory_id, status, priority, operator, tag, 
                 url=None, request_body_type=1, base_path=None, out_parameters=None,
                 request_headers=None, case_type=0, request_body=None, request_method=None, id=None):
        super().__init__(id=id, operator=operator, protocol=protocol, url=url, tag=tag,
                         request_body=request_body, request_body_type=request_body_type)
        self.name = name
        self.priority = priority
        self.directory_id = directory_id
        self.status = status
        self.out_parameters = out_parameters
        self.case_type = case_type
        self.request_headers = request_headers
        self.request_method = request_method
        self.base_path = base_path        

    def __str__(self):
        return f"[用例: {self.name}]({self.id}))"
