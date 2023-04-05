# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  database.py
@Time    :  2022/6/18 7:12 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  数据库配置表
"""
from uuid import uuid4
from sqlalchemy import ForeignKey, UniqueConstraint, Column, INT, String
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.models.environment import EnvironmentModel
from app.core.handler.sqlbin_uuid import BinaryUUID


class DatabaseModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_database_info"
    __table_args__ = (UniqueConstraint("env", "name"), {"comment": "数据库配置表"})
    env = Column(BinaryUUID, ForeignKey(
        EnvironmentModel.id, ondelete="cascade", onupdate="cascade"), comment="环境id")
    name = Column(String(ByteSizeEnum.LENGTH_50), nullable=False, comment="名称")
    host = Column(String(ByteSizeEnum.LENGTH_128),
                  nullable=False, comment="host")
    port = Column(INT, nullable=False, comment="端口")
    username = Column(String(ByteSizeEnum.LENGTH_50),
                      nullable=False, comment="登录用户名")
    password = Column(String(ByteSizeEnum.LENGTH_64),
                      nullable=False, comment="登录密码")
    database = Column(String(ByteSizeEnum.LENGTH_36),
                      nullable=True, comment="连接数据库名称")
    sql_type = Column(INT, nullable=False,
                      comment="0: mysql 1: postgresql 2: mongo")
    env_info: EnvironmentModel

    def __init__(self, env, name, host, port, username, password, database, sql_type, operator, id=None):
        super().__init__(id=id, operator=operator)
        self.env = env
        self.name = name
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.sql_type = sql_type
