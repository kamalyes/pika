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
from typing import Any, List

from fastapi import APIRouter, Depends
from hutools.pagination import LimitOffsetPage, add_pagination
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.rbac.role import RoleDao
from app.models import pagination_db
from app.schema.role import EditRoleModel, DelRoleModel, QueryRoleInModel, QueryRoleOutModel, BindRoleModel, \
    ApplyRoleModel, AuditRoleModel
from app.service import Permission

router = APIRouter()


@router.post("/role/add", name="添加角色配置")
async def add_role(request: EditRoleModel = Depends(), user_info=Depends(Permission())):
    return await RoleDao.add_role(request=request, emp_no=user_info["emp_no"])


@router.put("/role/update", name="更新角色配置信息")
async def update_role(request: EditRoleModel = Depends(), user_info=Depends(Permission())):
    return await RoleDao.update_role(request=request, emp_no=user_info["emp_no"])


@router.delete("/role/delete", name="删除角色配置")
async def delete_role(request: DelRoleModel = Depends(), user_info=Depends(Permission())):
    return await RoleDao.delete_role(request=request)


@router.get("/role/query", name="查询角色配置", response_model=LimitOffsetPage[QueryRoleOutModel])
async def query_role(request: QueryRoleInModel = Depends(), user_info=Depends(Permission()),
                     db: AsyncSession = Depends(pagination_db)) -> Any:
    return await RoleDao.query_role(db=db, request=request)


@router.post("/role/bind", name="给成员绑定角色")
async def bind_role(request: List[BindRoleModel], user_info=Depends(Permission())):
    return await RoleDao.bind_role(request=request, emp_no=user_info["emp_no"])


@router.post("/role/apply", name="角色关系申请")
async def apply_role(request: List[ApplyRoleModel], user_info=Depends(Permission())):
    return await RoleDao.apply_role(request=request, emp_no=user_info["emp_no"])


@router.post("/role/audit", name="角色关系审核")
async def audit_role(request: List[AuditRoleModel], user_info=Depends(Permission())):
    return await RoleDao.audit_role(request=request, userinfo=user_info)


add_pagination(router)
