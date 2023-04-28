# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
@Time    :  2022/6/16 8:15 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Any

from fastapi import APIRouter, Depends
from custard.pagination import LimitOffsetPage, add_pagination
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.handler.jsonres import PikaResponse
from app.crud.rbac.role import RoleDao
from app.models import async_db_session_iterator
from app.schema.base import BaseOnlyIdSchema
from app.schema.role import QueryRoleOutSchema, QueryRoleInSchema, EditRoleSchema
from app.service import Permission

router = APIRouter()


@router.get("/role/list", summary="分页获取角色数据", response_model=LimitOffsetPage[QueryRoleOutSchema])
async def query_encrypt_issue(request: QueryRoleInSchema = Depends(),
                              user_info=Depends(Permission()),
                              db: AsyncSession = Depends(async_db_session_iterator)) -> Any:
    return await RoleDao.list(db, request=request)


@router.post('/role/edit', summary="新增或更新角色")
async def save_or_update(request: EditRoleSchema, user_info=Depends(Permission())):
    try:
        await RoleDao.save_or_update(request=request, operator=user_info["emp_no"])
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
    return PikaResponse.success()


@router.delete('/role/delete', summary="删除角色")
async def delete(request: BaseOnlyIdSchema):
    """
    删除角色
    :return:
    """
    try:
        await RoleDao.delete(id=request.id)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
    return PikaResponse.success()


add_pagination(router)
