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
from sqlalchemy import Column, String, INT

from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.models.database import DatabaseModel


class SQLHistoryModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_sql_history"
    sql = Column(String(1024), comment="sql语句")
    elapsed = Column(INT, comment="请求耗时")
    database_id = Column(INT, comment="操作数据库id")
    database: DatabaseModel

    def __init__(self, sql, elapsed, database_id, operator):
        super().__init__(operator=operator)
        self.sql = sql
        self.elapsed = elapsed
        self.database_id = database_id
