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
from app.models import Base


class ApiTestResultModel(Base):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_test_result'
    __table_args__ = {"comment": "测试结果表"}
    id = Column(BinaryUUID,
                default=uuid4, primary_key=True)
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
    retry = Column(INT, default=0, comment="重试次数,预留字段")
    status_code = Column(INT, comment="http状态码")
    url = Column(TEXT, comment="URL")
    body = Column(TEXT, comment="body")
    request_method = Column(String(ByteSizeEnum.LENGTH_12), nullable=True, comment="请求方式")
    request_headers = Column(TEXT, comment="请求headers")
    request_params = Column(TEXT, comment="请求参数")
    cookies = Column(TEXT, comment="请求参数")
    data_name = Column(String(ByteSizeEnum.LENGTH_50))
    data_id = Column(BinaryUUID,
                     default=uuid4)
    cost = Column(String(ByteSizeEnum.LENGTH_12), nullable=False, comment="花费时间")
    asserts = Column(TEXT, comment="断言")
    response_headers = Column(TEXT, comment="响应头部")
    response = Column(TEXT, comment="返回参数")
    delete_flag = Column(BOOLEAN, server_default="0",
                         comment="删除标识 1：已删除,0：未删除")

    def __init__(self, report_id: str, case_id: str, case_name: str, status: int,
                 case_log: str, start_date: datetime, finished_date: datetime,
                 url: str, body: str, request_method: str, request_headers: str, cost: str,
                 asserts: str, response_headers: str, response: str,
                 status_code: int, cookies: str, retry: int = None,
                 request_params: str = None, data_name: str = None, data_id: str = None
                 ):
        self.report_id = report_id
        self.case_id = case_id
        self.case_name = case_name
        self.status = status
        self.case_log = case_log
        self.start_date = start_date
        self.finished_date = finished_date
        self.retry = retry
        self.status_code = status_code
        self.url = url
        self.request_method = request_method
        self.request_headers = request_headers
        self.body = body
        self.cost = cost
        self.response = response
        self.response_headers = response_headers
        self.asserts = asserts
        self.cookies = cookies
        self.request_params = request_params
        self.data_name = data_name
        self.data_id = data_id
        self.delete_flag = 0
