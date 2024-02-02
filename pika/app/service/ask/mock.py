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

from custard.pagination import LimitOffsetPage, add_pagination
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.itst.api.mock import MockDao
from app.models import async_db_session_iterator
from app.schema.base import BaseOnlyIdSchema
from app.schema.mock import DelMockSchema, EditMockSchema, QueryMockInSchema, QueryMockOutSchema
from app.service import Permission

router = APIRouter()


@router.post("/mock/add", summary="增加mock配置")
async def add_mock_deploy(request: EditMockSchema):
    return await MockDao.add_mock_deploy(request=request)


@router.delete("/mock/delete", summary="删除mock配置(软删)")
async def delete_mock_deploy(request: DelMockSchema = Depends(), escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    return await MockDao.delete_mock_deploy(request=request, operator=operator)


@router.post("/mock/update", summary="编辑mock配置")
async def update_mock_deploy(request: EditMockSchema, escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    return await MockDao.update_mock_deploy(request=request, operator=operator)


@router.get("/mock/list", summary="分页获取mock配置", response_model=LimitOffsetPage[QueryMockOutSchema])
async def list_mock_deploy(
    request: QueryMockInSchema = Depends(),
    escarole=Depends(Permission(escarole=True)),
    db: AsyncSession = Depends(async_db_session_iterator),
) -> Any:
    return await MockDao.list_mock_deploy(db, request)


@router.get("/mock/call", summary="请求mock返回")
async def call_mock_template(request: BaseOnlyIdSchema = Depends(), escarole=Depends(Permission(escarole=True))) -> Any:
    return await MockDao.call_mock_template(request)


add_pagination(router)
