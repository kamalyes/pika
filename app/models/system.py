# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  system.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  系统
"""

from sqlalchemy import Column, String, Text, DateTime, SMALLINT, INT

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.OperationEnum import SqlOperationTypeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel, MinBaseModel


class SysRecordModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_sys_record"
    remote_addr = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment='用户名称')
    real_ip = Column(String(ByteSizeEnum.LENGTH_255), nullable=False, comment='request_ip')
    request = Column(Text, nullable=False, comment='request')
    method = Column(String(ByteSizeEnum.LENGTH_255), nullable=True, comment='请求方式')
    url = Column(String(ByteSizeEnum.LENGTH_255), nullable=True, comment='url地址')
    args = Column(String(ByteSizeEnum.LENGTH_255), nullable=True, comment='args')
    form = Column(String(ByteSizeEnum.LENGTH_255), nullable=True, comment='form')
    json = Column(Text, nullable=True, comment='json')
    response = Column(Text, nullable=True, comment='响应')
    elapsed = Column(Text, nullable=True, comment='操作')
    request_time = Column(DateTime, nullable=True, comment='请求时间')
    env = Column(String(ByteSizeEnum.LENGTH_255), nullable=True, comment='环境')
    emp_code = Column(String(ByteSizeEnum.LENGTH_255), nullable=True, comment='员工编号')


class OperationLogModel(MinBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_operation_log'
    __table_args__ = {"comment": "操作记录表"}
    diff_data = Column(String(ByteSizeEnum.LENGTH_1000), nullable=True, comment="diff_data")
    tag = Column(String(ByteSizeEnum.LENGTH_1000), comment="操作table_args")
    mode = Column(SMALLINT, comment="操作类型")
    key = Column(INT, nullable=True, comment="关键id,可能是目录id,case_id或者其他id")

    def __init__(self, operator, mode: SqlOperationTypeEnum, tag=None, diff_data=None, description=None, key=None):
        super().__init__(operator=operator, description=description)
        self.tag = tag
        self.diff_data = diff_data
        self.mode = mode.value
        self.key = key
