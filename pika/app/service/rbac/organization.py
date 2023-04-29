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
from typing import Any

from custard.pagination import LimitOffsetPage, add_pagination
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.handler.jsonres import PikaResponse
from app.crud.rbac.organization import OrganizationDao
from app.enums.RbacEnum import RoleEnum
from app.models import async_db_session_iterator
from app.models.organization import OrganizationModel
from app.schema.base import BaseBatchDelIdsSchema
from app.schema.organization import OrganizationFormSchema, QueryOrganizationInSchema, QueryOrganizationOutSchema
from app.service import Permission

router = APIRouter()


@router.post("/organization/insert", summary="增加组织机构")
async def insert_organization(data: OrganizationFormSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    await OrganizationDao.insert_organization(data, user_info["emp_no"])
    return PikaResponse.success()


@router.delete("/organization/delete", summary="删除组织机构")
async def delete_organization(
    request: BaseBatchDelIdsSchema = Depends(),
    user_info=Depends(Permission(RoleEnum.ADMIN)),
):
    await OrganizationDao.delete_by_id(model=OrganizationModel, ids=request.ids.split(","))
    return PikaResponse.success()


@router.post("/organization/update", summary="更新组织机构")
async def update_organization(
    form: OrganizationFormSchema,
    user_info=Depends(Permission(RoleEnum.ADMIN)),
    session=Depends(async_db_session_iterator),
):
    await OrganizationDao.parity_field(
        session=session,
        name=form.name,
        organization_id=form.id,
        parent_id=form.parent_id,
    )
    await OrganizationDao.update_record_by_id(user_info["emp_no"], form, True)
    return PikaResponse.success()


@router.get("/organization/list", summary="查询组织机构列表", response_model=LimitOffsetPage[QueryOrganizationOutSchema])
async def list_organization(
    form: QueryOrganizationInSchema = Depends(),
    db: AsyncSession = Depends(async_db_session_iterator),
) -> Any:
    return await OrganizationDao.limit(db, form)


add_pagination(router)
