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
from fastapi import APIRouter, Depends

from app.core.handler.jsonres import PikaResponse
from app.crud.online.database import DbConfigDao, SQLHistoryDao
from app.models.database import DatabaseModel
from app.models.environment import EnvironmentModel
from app.models.sql_log import SQLHistoryModel
from app.schema.database import DatabaseSchema
from app.schema.online import OnlineSqlSchema
from app.service import Permission

router = APIRouter()


@router.post("/sql/command", summary="执行sql")
async def execute_sql(data: OnlineSqlSchema, escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    try:
        result, elapsed = await DbConfigDao.online_sql(data.id, data.sql)
        columns, result = PikaResponse.parse_sql_result(result)
        await SQLHistoryDao.insert(model=SQLHistoryModel(data.sql, elapsed, data.id, operator))
        return PikaResponse.success(data=dict(result=result, columns=columns, elapsed=elapsed))
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.get("/sql/history/query", summary="获取sql执行历史记录")
async def query_sql_history(page: int = 1, size: int = 4, user_info=Depends(Permission())):
    data, total = await SQLHistoryDao.list_with_pagination(page, size,
                                                           _sort=[SQLHistoryModel.create_date.desc()],
                                                           _select=[DatabaseModel, EnvironmentModel],
                                                           _join=[(DatabaseModel,
                                                                   DatabaseModel.id == SQLHistoryModel.database_id),
                                                                  (EnvironmentModel,
                                                                   EnvironmentModel.id == DatabaseModel.env)
                                                                  ])
    ans = []
    for history, database, env in data:
        database.env_info = env
        history.database = database
        ans.append(history)
    return PikaResponse.success(dict(data=ans, total=total))


@router.get("/sql/database/list")
async def list_databases(user_info=Depends(Permission())):
    try:
        result = await DbConfigDao.query_database_tree()
        return PikaResponse.success(result)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.post("/sql/tables/list", summary="获取数据库表和字段")
async def list_tables(form: DatabaseSchema, user_info=Depends(Permission())):
    try:
        children, tables = await DbConfigDao.get_tables(form)
        return PikaResponse.success(dict(children=children, tables=tables))
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
