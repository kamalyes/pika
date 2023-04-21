# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_test_result.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy import INT, Column, DATETIME, String, BOOLEAN
from sqlalchemy import SMALLINT
from sqlalchemy import TEXT
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.core.handler.sqlbin_uuid import BinaryUUID
from app.models.basic import ApiGBaseModel


class ApiTestResultModel(ApiGBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_test_result'
    __table_args__ = {"comment": "测试结果表"}
    directory_id = None
    report_id = Column(BinaryUUID,
                       default=uuid4, index=True, comment="报告id")
    case_id = Column(BinaryUUID,
                     default=uuid4, index=True, comment="用例id")
    case_name = Column(String(ByteSizeEnum.LENGTH_50), comment="用例名称")
    status = Column(SMALLINT, comment="对应状态 0: 成功 1: 失败 2: 出错 3: 跳过")
    start_date = Column(DATETIME, nullable=False, default=None, comment="开始时间")
    finished_date = Column(DATETIME, nullable=False, default=None, comment="结束时间")
    case_log = Column(TEXT, comment="测试日志")
    retry = Column(INT, server_default="0", comment="重试次数,预留字段")
    status_code = Column(INT, server_default="0", comment="http状态码")
    cookies = Column(TEXT, comment="请求参数")
    data_name = Column(String(ByteSizeEnum.LENGTH_50))
    data_id = Column(BinaryUUID,default=uuid4)
    cost = Column(String(ByteSizeEnum.LENGTH_12), nullable=False, comment="花费时间")
    asserts = Column(TEXT, comment="断言")

    def __init__(self, report_id: str, case_id: str, case_name: str, status: int,
                 case_log: str, start_date: datetime, finished_date: datetime,
                 url: str, request_body: str, request_method: str, request_headers: str, cost: str,
                 asserts: str, response_headers: str, response: str,
                 status_code: int, cookies: str, retry: int = None,
                 request_params: str = None, data_name: str = None, data_id: str = None,
                 operator=None, protocol=None, tag=None, id=None, delete_flag = 0
                 ):
        super().__init__(id=id, operator=operator, protocol=protocol,
                         url=url, tag=tag, request_method=request_method,
                         request_headers=request_headers, response=response, response_headers=response_headers,
                         request_params=request_params, delete_flag=delete_flag, request_body=request_body)
        self.report_id = report_id
        self.case_id = case_id
        self.case_name = case_name
        self.status = status
        self.case_log = case_log
        self.start_date = start_date
        self.finished_date = finished_date
        self.retry = retry
        self.status_code = status_code
        self.cost = cost
        self.asserts = asserts
        self.cookies = cookies
        self.data_name = data_name
        self.data_id = data_id
