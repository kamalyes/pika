# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  sql.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.online.database import DbConfigDao
from app.schema.online import OnlineSQLForm

router = APIRouter()


@router.post("/sql/command", summary="执行sql")
async def execute_sql(data: OnlineSQLForm):
    try:
        result = await DbConfigDao.online_sql(data.id, data.sql)
        columns, result = PikaResponse.parse_sql_result(result)
        return PikaResponse.success(data=dict(result=result, columns=columns))
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.get("/sql/showtables", summary="获取数据库及表结构")
async def list_tables():
    try:
        result, table_map = await DbConfigDao.query_database_and_tables()
        return PikaResponse.success(data=dict(database=result, tables=table_map))
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
