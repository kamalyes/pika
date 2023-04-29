# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  sql_log.py
@Time    :  2022/8/19 12:21
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import INT, Column, ForeignKey, String

from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.models.database import DatabaseModel


class SQLHistoryModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_sql_history"
    __table_args__ = {"comment": "sql执行历史表"}
    sql = Column(String(ByteSizeEnum.LENGTH_1024), comment="sql语句")
    elapsed = Column(INT, server_default="0", comment="请求耗时")
    database_id = Column(
        BinaryUUID,
        ForeignKey(DatabaseModel.id, ondelete="cascade", onupdate="cascade"),
        comment="操作的数据库id",
    )

    def __init__(self, sql, elapsed, database_id, operator):
        super().__init__(operator=operator)
        self.sql = sql
        self.elapsed = elapsed
        self.database_id = database_id
