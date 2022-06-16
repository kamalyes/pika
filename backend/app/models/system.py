# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  system.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  系统
"""

from sqlalchemy import Column, String, Text, DateTime

from app.enums.sysvar import GlobalVarEnum
from app.models import Base
from app.models.basic import PikaNormBase


class RequestHistory(Base, PikaNormBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_ask_history"
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
