# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  mock
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  mock服务
"""

from typing import Any

from fastapi import APIRouter, Depends
from hutools.pagination import LimitOffsetPage, add_pagination
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.itst.mock import MockDao
from app.models import pagination_db
from app.schema.base import PikaOnlyIdModel
from app.schema.mock import (EditMockModel, DelMockModel,
                             QueryMockOutModel, QueryMockInModel)
from app.service import Permission

router = APIRouter()


@router.post("/mock/add", name="增加mock配置")
async def add_mock_deploy(request: EditMockModel):
    return await MockDao.add_mock_deploy(request=request)


@router.delete("/mock/delete", name="删除mock配置（软删）")
async def delete_mock_deploy(request: DelMockModel = Depends(), emp_no=Depends(Permission(return_emp_no=True))):
    return await MockDao.delete_mock_deploy(request=request, emp_no=emp_no)


@router.post("/mock/update", name="编辑mock配置")
async def update_mock_deploy(request: EditMockModel, emp_no=Depends(Permission(return_emp_no=True))):
    return await MockDao.update_mock_deploy(request=request, emp_no=emp_no)


@router.get("/mock/query", name="分页获取mock配置", response_model=LimitOffsetPage[QueryMockOutModel])
async def query_mock_deploy(request: QueryMockInModel = Depends(), emp_no=Depends(Permission(return_emp_no=True)),
                            db: AsyncSession = Depends(pagination_db)) -> Any:
    return await MockDao.query_mock_deploy(db, request)


@router.get("/mock/call", name="请求mock返回")
async def call_mock_template(request: PikaOnlyIdModel = Depends(),
                             emp_no=Depends(Permission(return_emp_no=True))) -> Any:
    return await MockDao.call_mock_template(request)


add_pagination(router)
