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

from fastapi import APIRouter, Depends
from hutools.pagination import LimitOffsetPage, add_pagination
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.itst.functest import FuncCaseDao
from app.models import pagination_db
from app.schema.functest import EditFuncCaseModel, DelFuncCaseModel, QueryFuncCaseInModel, QueryFuncCaseOutModel
from app.service import Permission

router = APIRouter()


@router.post("/funccase/add", name="增加功能测试用例")
async def add_funccase(request: EditFuncCaseModel, emp_no=Depends(Permission(return_emp_no=True))):
    return await FuncCaseDao.add_funccase(request=request, emp_no=emp_no)


@router.delete("/funccase/delete", name="删除功能测试用例（软删）")
async def delete_funccase(request: DelFuncCaseModel = Depends(), emp_no=Depends(Permission(return_emp_no=True))):
    return await FuncCaseDao.delete_funccase(request=request, emp_no=emp_no)


@router.post("/funccase/update", name="编辑功能测试用例")
async def update_funccase(request: EditFuncCaseModel, emp_no=Depends(Permission(return_emp_no=True))):
    return await FuncCaseDao.update_funccase(request=request, emp_no=emp_no)


@router.get("/funccase/query", name="分页获取功能测试用例", response_model=LimitOffsetPage[QueryFuncCaseOutModel])
async def query_funccase(request: QueryFuncCaseInModel = Depends(), emp_no=Depends(Permission(return_emp_no=True)),
                         db: AsyncSession = Depends(pagination_db)) -> Any:
    return await FuncCaseDao.query_funccase(db, request)


add_pagination(router)
