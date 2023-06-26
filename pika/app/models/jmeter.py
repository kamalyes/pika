# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  jmeter.py
@Time    :  2022/6/18 7:12 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  jmeter
"""

from app.models.basic import AlongTimeStampBaseModel
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.core.handler.sqlbin_uuid import BinaryUUID
from sqlalchemy import Column, String, BigInteger, SMALLINT, ForeignKey, UniqueConstraint, TEXT, BOOLEAN, DATETIME, text


class JmeterMinBaseModel(AlongTimeStampBaseModel):
    operator = Column(String(ByteSizeEnum.LENGTH_20), nullable=True, comment="操作者emp_no")
    operator_date = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="操作时间",
    )
    __abstract__ = True

    def __init__(self, id=None, operator=None, description=None, start_time=0, end_time=0):
        super().__init__(id=id, description=description, start_time=start_time, end_time=end_time)
        self.operator = operator


class JmeterTestSummaryModel(JmeterMinBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_jmeter_testsummary"
    __table_args__ = (UniqueConstraint("batch_no"), {"comment": "Jmeter测试报告"})
    batch_no = Column(String(ByteSizeEnum.LENGTH_128), comment="用例批次编号", nullable=False)
    project = Column(String(ByteSizeEnum.LENGTH_200), server_default=None, comment="项目名称")
    env = Column(String(ByteSizeEnum.LENGTH_200), comment="环境名称")
    os_type = Column(SMALLINT, server_default="0", comment="机器类型(1:手动构建/2:自动化)")
    total = Column(BigInteger, server_default="0", comment="用例总数")
    success = Column(BigInteger, server_default="0", comment="成功数")
    failure = Column(BigInteger, server_default="0", comment="失败数")
    pass_rate = Column(String(ByteSizeEnum.LENGTH_06), server_default="0", comment="通过率")
    duration = Column(BigInteger, server_default="0", comment="持续时间")
    result = Column(BOOLEAN, server_default="0", comment="测试结果")

    def __init__(
        self,
        batch_no=None,
        project=None,
        env=None,
        os_type=None,
        total=0,
        success=0,
        failure=0,
        pass_rate=0,
        duration=0,
        result=0,
        id=None,
        operator=None,
        description=None,
        start_time=0,
        end_time=0,
    ):
        super().__init__(id=id, operator=operator, description=description, start_time=start_time, end_time=end_time)
        self.batch_no = batch_no
        self.project = project
        self.env = env
        self.os_type = os_type
        self.total = total
        self.success = success
        self.failure = failure
        self.pass_rate = pass_rate
        self.duration = duration
        self.result = result


class JmeterTestCaseModel(JmeterMinBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_jmeter_testcase"
    __table_args__ = {"comment": "Jmeter测试用例"}
    batch_no = Column(String(ByteSizeEnum.LENGTH_128), comment="用例批次编号", nullable=False)
    module_name = Column(String(ByteSizeEnum.LENGTH_200), comment="模块名称")
    case_name = Column(TEXT, nullable=True, comment="用例名称")
    request_url = Column(TEXT, nullable=True, comment="请求地址")
    request_method = Column(TEXT, nullable=True, comment="请求方法")
    request_header = Column(TEXT, nullable=True, comment="请求头")
    request_query = Column(TEXT, nullable=True, comment="请求体(Query、一般是get请求)")
    request_body = Column(TEXT, nullable=True, comment="请求体(Body、一般是post请求)")
    response_body = Column(TEXT, nullable=True, comment="响应体")
    response_code = Column(BigInteger, server_default="200", comment="响应状态码")
    response_time = Column(BigInteger, server_default="0", comment="响应时间")
    response_size = Column(BigInteger, server_default="0", comment="响应包体大小")
    response_header = Column(TEXT, nullable=True, comment="响应头")
    fail_message = Column(TEXT, nullable=True, comment="失败明细")
    cookies = Column(TEXT, nullable=True, comment="cookies")
    body_size = Column(BigInteger, server_default="0", comment="body大小")
    request_size = Column(BigInteger, server_default="0", comment="请求数据大小")
    headers_size = Column(BigInteger, server_default="0", comment="headers大小")
    error_count = Column(BigInteger, server_default="0", comment="失败数量")
    successful = Column(BOOLEAN, server_default="0", comment="是否通过、成功（符合预期断言）")
    connect_time = Column(BigInteger, server_default="0", comment="连接时间")
    latency = Column(BigInteger, server_default="0", comment="延迟")
    group_threads = Column(BigInteger, server_default="0", comment="线程组数")
    all_threads = Column(BigInteger, server_default="0", comment="所有线程数")
    data_encoding = Column(TEXT, nullable=True, comment="数据编码类型")
    ignore = Column(BOOLEAN, server_default="0", comment="是否忽略")
    total_assertions = Column(BigInteger, server_default="0", comment="断言点总数")
    pass_assertions = Column(BigInteger, server_default="0", comment="断言成功数量")
    assertions = Column(TEXT, nullable=True, comment="断言详情")

    def __init__(
        self,
        batch_no=None,
        module_name=None,
        case_name=None,
        request_url=None,
        request_method=None,
        request_header=None,
        request_query=None,
        request_body=None,
        response_header=None,
        response_body=None,
        response_time=None,
        response_size=None,
        response_code=None,
        fail_message=None,
        cookies=None,
        body_size=None,
        request_size=None,
        headers_size=None,
        error_count=None,
        successful=False,
        connect_time=None,
        latency=None,
        group_threads=None,
        all_threads=None,
        data_encoding=None,
        ignore=False,
        total_assertions=None,
        pass_assertions=None,
        assertions=None,
        id=None,
        operator=None,
        description=None,
        start_time=0,
        end_time=0,
    ):
        super().__init__(id=id, operator=operator, description=description, start_time=start_time, end_time=end_time)
        self.batch_no = batch_no
        self.module_name = module_name
        self.case_name = case_name
        self.request_url = request_url
        self.request_method = request_method
        self.request_header = request_header
        self.request_query = request_query
        self.request_body = request_body
        self.response_header = response_header
        self.response_body = response_body
        self.response_code = response_code
        self.response_time = response_time
        self.response_size = response_size
        self.fail_message = fail_message
        self.cookies = cookies
        self.body_size = body_size
        self.request_size = request_size
        self.headers_size = headers_size
        self.error_count = error_count
        self.successful = successful
        self.connect_time = connect_time
        self.latency = latency
        self.group_threads = group_threads
        self.all_threads = all_threads
        self.data_encoding = data_encoding
        self.ignore = ignore
        self.total_assertions = total_assertions
        self.pass_assertions = pass_assertions
        self.assertions = str(assertions)
