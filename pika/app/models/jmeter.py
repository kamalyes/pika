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

from app.models.basic import LargeBaseModel
from pika.app.enums.ByteSizeEnum import ByteSizeEnum
from pika.app.enums.SysVarEnum import PikaGlobalVarEnum
from sqlalchemy import Column, String, BigInteger, SMALLINT, ForeignKey, UniqueConstraint, TEXT, BOOLEAN, DATETIME


class JmeterTestSummaryModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_jmeter_testsummary"
    __table_args__ = (UniqueConstraint("batch_no"), {"comment": "Jmeter测试报告"})
    batch_no = Column(String(ByteSizeEnum.LENGTH_50), comment="用例批次编号")
    project = Column(String(ByteSizeEnum.LENGTH_50), server_default=None, comment="项目名称")
    env = Column(String(ByteSizeEnum.LENGTH_50), comment="环境名称")
    run_type = Column(SMALLINT, comment="构建类型")
    total = Column(BigInteger, comment="用例总数")
    success = Column(BigInteger, comment="成功数")
    fail = Column(BigInteger, comment="失败数")
    pass_rate = Column(SMALLINT(6), server_default="0", comment="通过率")
    duration = Column(BigInteger, server_default="0", comment="持续时间")
    result = Column(BOOLEAN, server_default="0", comment="测试结果")
    start_date = Column(DATETIME, nullable=False, default=None, comment="开始时间")
    finished_date = Column(DATETIME, nullable=False, default=None, comment="结束时间")


class JmeterTestCaseModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_jmeter_testcase"
    __table_args__ = (UniqueConstraint("batch_no"), {"comment": "Jmeter测试用例"})
    batch_no = Column(
        String(ByteSizeEnum.LENGTH_20),
        ForeignKey(JmeterTestSummaryModel.batch_no, ondelete="cascade", onupdate="cascade"),
        comment="用例批次编号",
        nullable=False,
    )
    module_name = Column(max_length=50, comment="模块名称")
    case_name = Column(TEXT, comment="用例名称")
    request_url = Column(TEXT, comment="请求地址")
    request_method = Column(TEXT, blank=True, null=True, comment="请求方法")
    request_header = Column(TEXT, blank=True, null=True, comment="请求头")
    request_body = Column(TEXT, blank=True, null=True, comment="请求体")
    response_header = Column(TEXT, blank=True, null=True, comment="响应头")
    response_body = Column(TEXT, blank=True, null=True, comment="响应体")
    response_code = Column(max_length=50, blank=True, null=True, comment="响应状态码")
    test_result = Column(BOOLEAN, comment="测试结果")
    fail_message = Column(TEXT, blank=True, null=True, comment="模块名称")
    start_date = Column(DATETIME, nullable=False, default=None, comment="开始时间")
    finished_date = Column(DATETIME, nullable=False, default=None, comment="结束时间")
