# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  functest
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  功能测试
"""

from typing import Any

from app.models import async_db_session_iterator
from app.schema.functest import DelFuncCaseSchema, EditFuncCaseSchema, QueryFuncCaseInSchema, QueryFuncCaseOutSchema
from app.service import Permission
from custard.pagination import LimitOffsetPage, add_pagination
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/funccase/add", summary="增加功能测试用例")
async def add_funccase(request: EditFuncCaseSchema, escarole=Depends(Permission(escarole=True))):
    emp_no, role = escarole
    return await FuncCaseDao.add_funccase(request=request, emp_no=emp_no)


@router.delete("/funccase/delete", summary="删除功能测试用例(软删)")
async def delete_funccase(request: DelFuncCaseSchema = Depends(), escarole=Depends(Permission(escarole=True))):
    emp_no, role = escarole
    return await FuncCaseDao.delete_funccase(request=request, emp_no=emp_no)


@router.post("/funccase/update", summary="编辑功能测试用例")
async def update_funccase(request: EditFuncCaseSchema, escarole=Depends(Permission(escarole=True))):
    emp_no, role = escarole
    return await FuncCaseDao.update_funccase(request=request, emp_no=emp_no)


@router.get("/funccase/list", summary="分页获取功能测试用例", response_model=LimitOffsetPage[QueryFuncCaseOutSchema])
async def list_funccase(
    request: QueryFuncCaseInSchema = Depends(),
    escarole=Depends(Permission(escarole=True)),
    db: AsyncSession = Depends(async_db_session_iterator),
) -> Any:
    return await FuncCaseDao.list_funccase(db, request)


add_pagination(router)
