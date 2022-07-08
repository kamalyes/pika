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
from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, SMALLINT, INT

from app.enums.bytesize import ByteSizeEnum
from app.enums.operation import SqlOperationTypeEnum
from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaNormBase, PikaMinBase


class PikaSysRecord(PikaNormBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_sys_record"
    remote_addr = Column(String(255), nullable=False, comment='用户名称')
    real_ip = Column(String(255), nullable=False, comment='request_ip')
    request = Column(Text, nullable=False, comment='request')
    method = Column(String(255), nullable=True, comment='请求方式')
    url = Column(String(255), nullable=True, comment='url地址')
    args = Column(String(255), nullable=True, comment='args')
    form = Column(String(255), nullable=True, comment='form')
    json = Column(Text, nullable=True, comment='josn')
    response = Column(Text, nullable=True, comment='响应')
    elapsed = Column(Text, nullable=True, comment='操作')
    request_time = Column(DateTime, nullable=True, comment='请求时间')
    env = Column(String(255), nullable=True, comment='环境')
    emp_code = Column(String(255), nullable=True, comment='员工编号')


class PikaOperationLog(PikaMinBase):
    __tablename__ = f'{PikaGlobalVarEnum.APP_NAME_LOWER}_operation_log'
    title = Column(String(ByteSizeEnum.LENGTH_128), nullable=False, comment="操作title")
    tag = Column(String(ByteSizeEnum.LENGTH_56), comment="操作tag")
    mode = Column(SMALLINT, comment="操作类型")
    key = Column(INT, nullable=True, comment="关键id，可能是目录id，case_id或者其他id")

    def __init__(self, operator, mode: SqlOperationTypeEnum, title, tag, description=None, key=None, id=0):
        super().__init__(operator, description, id)
        self.title = title
        self.tag = tag
        self.mode = mode.value
        self.key = key
        self.operator_date = datetime.now()
        self.description = description
        self.id = id
