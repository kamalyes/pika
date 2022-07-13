# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  GconfigEnum.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.online.gconfig import GConfigDao
from app.enums.RbacEnum import RoleEnum
from app.models import async_db_session
from app.schema.gconfig import GConfigFormSchema
from app.service import Permission

router = APIRouter()


@router.post("/gconfig/insert", summary="增加全局配置")
async def insert_gconfig(data: GConfigFormSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    await GConfigDao.insert_gconfig(data, user_info['emp_no'])
    return PikaResponse.success()


@router.delete("/gconfig/delete", summary="删除全局配置")
async def delete_gconfig(id: int, user_info=Depends(Permission(RoleEnum.ADMIN)),
                         session=Depends(async_db_session)):
    await GConfigDao.delete_record_by_id(session, user_info['emp_no'], id, log=True)
    return PikaResponse.success()


@router.post("/gconfig/update", summary="更新全局配置")
async def update_gconfig(data: GConfigFormSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    await GConfigDao.update_record_by_id(user_info['emp_no'], data, True, True)
    return PikaResponse.success()


@router.get("/gconfig/list", summary="查询全局配置列表")
async def list_gconfig(page: int = 1, size: int = 8, env=None, key: str = "",
                       user_info=Depends(Permission())):
    data, total = await GConfigDao.list_record_with_pagination(page, size, env=env, key=key)
    return PikaResponse.success_with_size(data=data, total=total)
