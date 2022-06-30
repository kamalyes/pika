# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  apicase
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  接口测试测试
"""
from typing import Any

from fastapi import APIRouter, Depends
from hutools.pagination import LimitOffsetPage, add_pagination
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.itst.apitest import ApiCaseDao
from app.models import pagination_db
from app.schema.apitest import EditApiCaseModel, DelApiCaseModel, QueryApiCaseInModel, QueryApiCaseOutModel
from app.service import Permission

router = APIRouter()


@router.post("/apicase/add", name="增加接口测试用例")
async def add_apicase(request: EditApiCaseModel, emp_no=Depends(Permission(return_emp_no=True))):
    return await ApiCaseDao.add_apicase(request=request, emp_no=emp_no)


@router.delete("/apicase/delete", name="删除接口测试用例（软删）")
async def delete_apicase(request: DelApiCaseModel = Depends(), emp_no=Depends(Permission(return_emp_no=True))):
    return await ApiCaseDao.delete_apicase(request=request, emp_no=emp_no)


@router.post("/apicase/update", name="编辑接口测试用例")
async def update_apicase(request: EditApiCaseModel, emp_no=Depends(Permission(return_emp_no=True))):
    return await ApiCaseDao.update_apicase(request=request, emp_no=emp_no)


@router.get("/apicase/query", name="分页获取接口测试用例", response_model=LimitOffsetPage[QueryApiCaseOutModel])
async def query_apicase(request: QueryApiCaseInModel = Depends(), emp_no=Depends(Permission(return_emp_no=True)),
                        db: AsyncSession = Depends(pagination_db)) -> Any:
    return await ApiCaseDao.query_apicase(db, request)


add_pagination(router)
