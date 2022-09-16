# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  environment.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import APIRouter, Depends

from app.core.handler.jsonres import PikaResponse
from app.crud.itstem.environment import EnvironmentDao
from app.enums.RbacEnum import RoleEnum
from app.models import async_db_session_iterator
from app.schema.base import BaseOnlyPagingSchema
from app.schema.environment import EnvironmentSchema
from app.service import Permission

router = APIRouter()


@router.post("/environment/insert", summary="增加环境配置")
async def insert_environment(data: EnvironmentSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    await EnvironmentDao.insert_env(data=data, emp_no=user_info['emp_no'])
    return PikaResponse.success()


@router.delete("/environment/delete", summary="删除环境配置")
async def delete_environment(id: int, user_info=Depends(Permission(RoleEnum.ADMIN)),
                             session=Depends(async_db_session_iterator)):
    await EnvironmentDao.delete_record_by_id(session=session, operator=user_info['emp_no'], value=id, log=True)
    return PikaResponse.success()


@router.post("/environment/update", summary="更新环境配置")
async def update_environment(data: EnvironmentSchema, user_info=Depends(Permission(RoleEnum.ADMIN)),
                             session=Depends(async_db_session_iterator)):
    ans = await EnvironmentDao.update_record_by_id(operator=user_info['emp_no'], model=data, not_null=True)
    return PikaResponse.success(data=ans)


@router.get("/environment/list", summary="查询环境配置列表")
async def list_environment(paging: BaseOnlyPagingSchema = Depends(),
                           name: str = "", exactly=False,
                           user_info=Depends(Permission())):
    data, total = await EnvironmentDao.list_env(paging, name, exactly)
    return PikaResponse.success_with_size(data=data, total=total)
