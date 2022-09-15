# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  organization.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  组织架构
"""

from fastapi import APIRouter, Depends

from app.core.handler.jsonres import PikaResponse
from app.crud.rbac.organization import OrganizationDao
from app.enums.RbacEnum import RoleEnum
from app.models import async_db_session_iterator
from app.schema.organization import OrganizationFormSchema, QueryOrganizationInSchema
from app.service import Permission

router = APIRouter()


@router.post("/organization/insert", summary="增加组织机构")
async def insert_organization(data: OrganizationFormSchema,
                              user_info=Depends(Permission(RoleEnum.ADMIN))):
    await OrganizationDao.insert_organization(data, user_info['emp_no'])
    return PikaResponse.success()


@router.delete("/organization/delete", summary="删除组织机构")
async def delete_organization(id: int, user_info=Depends(Permission(RoleEnum.ADMIN)),
                              session=Depends(async_db_session_iterator)):
    await OrganizationDao.delete_record_by_id(session, user_info['emp_no'], id, log=True)
    return PikaResponse.success()


@router.post("/organization/update", summary="更新组织机构")
async def update_organization(data: OrganizationFormSchema,
                              user_info=Depends(Permission(RoleEnum.ADMIN))):
    await OrganizationDao.update_record_by_id(user_info['emp_no'], data, True)
    return PikaResponse.success()


@router.get("/organization/list", summary="查询组织机构列表")
async def list_organization(data: QueryOrganizationInSchema = Depends(),
                            user_info=Depends(Permission(RoleEnum.ADMIN))):
    data, total = await OrganizationDao.list_with_pagination(data)
    return PikaResponse.success_with_size(data=data, total=total)

