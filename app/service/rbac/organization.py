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


@router.post("/organization/insert", summary="增加全局配置")
async def insert_organization(data: OrganizationFormSchema,
                              user_info=Depends(Permission(RoleEnum.ADMIN))):
    await OrganizationDao.insert_organization(data, user_info['emp_no'])
    return PikaResponse.success()


@router.delete("/organization/delete", summary="删除全局配置")
async def delete_organization(id: int, user_info=Depends(Permission(RoleEnum.ADMIN)),
                              session=Depends(async_db_session_iterator)):
    await OrganizationDao.delete_record_by_id(session, user_info['emp_no'], id, log=True)
    return PikaResponse.success()


@router.post("/organization/update", summary="更新全局配置")
async def update_organization(data: OrganizationFormSchema,
                              user_info=Depends(Permission(RoleEnum.ADMIN))):
    await OrganizationDao.update_record_by_id(user_info['emp_no'], data, True)
    return PikaResponse.success()


@router.get("/organization/list", summary="查询全局配置列表")
async def list_organization(data: QueryOrganizationInSchema = Depends(),
                            user_info=Depends(Permission(RoleEnum.ADMIN))):
    data, total = await OrganizationDao.list_with_pagination(data)
    return PikaResponse.success_with_size(data=data, total=total)


@router.post("/organization/relation/bind", summary="建立成员与部门之间的关联")
async def bind_organization_relation():
    pass


@router.delete("/organization/relation/unbind", dependencies=[], name="解除成员与部门之间的关联")
async def unbind_organization_relation():
    pass
