# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  database.py
@Time    :  2022/6/18 7:12 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import UniqueConstraint, Column, INT, String

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase


class PikaDatabase(PikaLargeBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_database_info"
    __table_args__ = (UniqueConstraint('env_id', 'name'),)
    env_id = Column(INT, nullable=False, comment="对应环境id")
    name = Column(String(ByteSizeEnum.LENGTH_30), nullable=False, comment="名称")
    host = Column(String(ByteSizeEnum.LENGTH_128), nullable=False, comment="host")
    port = Column(INT, nullable=False, comment="端口")
    username = Column(String(36), nullable=False, comment="登录用户名")
    password = Column(String(64), nullable=False, comment="登录密码")
    database = Column(String(36), nullable=False, comment="连接数据库名称")
    sql_type = Column(INT, nullable=False, comment="0: mysql 1: postgresql 2: mongo")

    def __init__(self, env, name, host, port, username, password, database, sql_type, operator, id=None):
        super().__init__(operator, id)
        self.env = env
        self.name = name
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.sql_type = sql_type
