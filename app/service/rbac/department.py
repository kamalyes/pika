# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  department.py
@Time    :  2022/9/15 11:10
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.rbac.department import DepartmentDao
from app.enums.RbacEnum import RoleEnum
from app.models import async_db_session_iterator
from app.schema.base import BaseOnlyPagingSchema
from app.schema.department import DepartmentFormSchema, QueryDepartmentInSchema
from app.service import Permission

router = APIRouter()


@router.post("/department/insert", summary="增加全局配置")
async def insert_department(data: DepartmentFormSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    await DepartmentDao.insert_department(data, user_info['emp_no'])
    return PikaResponse.success()


@router.delete("/department/delete", summary="删除全局配置")
async def delete_department(id: int, user_info=Depends(Permission(RoleEnum.ADMIN)),
                            session=Depends(async_db_session_iterator)):
    await DepartmentDao.delete_record_by_id(session, user_info['emp_no'], id, log=True)
    return PikaResponse.success()


@router.post("/department/update", summary="更新全局配置")
async def update_department(data: DepartmentFormSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    await DepartmentDao.update_record_by_id(user_info['emp_no'], data, True)
    return PikaResponse.success()


@router.get("/department/list", summary="查询全局配置列表")
async def list_department(data: QueryDepartmentInSchema = Depends(),
                          paging: BaseOnlyPagingSchema = Depends(),
                          user_info=Depends(Permission(RoleEnum.ADMIN))):
    data, total = await DepartmentDao.list_with_pagination(paging, data)
    return PikaResponse.success_with_size(data=data, total=total)


@router.post("/department/relation/bind", summary="建立成员与部门之间的关联")
async def bind_department_relation():
    pass


@router.delete("/department/relation/unbind", dependencies=[], name="解除成员与部门之间的关联")
async def unbind_department_relation():
    pass
