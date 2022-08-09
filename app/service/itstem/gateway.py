# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gateway.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.online.gateway import GatewayDao
from app.enums.RbacEnum import RoleEnum
from app.models import async_db_session
from app.models.gateway import GatewayModel
from app.schema.gateway import PikaGatewaySchema
from app.service import Permission

router = APIRouter()


@router.post("/gateway/insert", summary="添加请求地址")
async def insert_gateway(form: PikaGatewaySchema, user_info=Depends(Permission(RoleEnum.MANAGER))):
    model = GatewayModel(**form.dict(), operator=user_info['emp_no'])
    model = await GatewayDao.insert(model, True)
    return PikaResponse.success(data=model)


@router.delete("/gateway/delete", summary="删除请求地址")
async def delete_gateway(id: int, user_info=Depends(Permission(RoleEnum.MANAGER)),
                         session=Depends(async_db_session)):
    await GatewayDao.delete_record_by_id(session=session,
                                         operator=user_info['emp_no'],
                                         value=id)
    return PikaResponse.success()


@router.post("/gateway/update", summary="编辑请求地址")
async def insert_gateway(form: PikaGatewaySchema, user_info=Depends(Permission(RoleEnum.MANAGER))):
    model = await GatewayDao.update_record_by_id(operator=user_info['emp_no'],
                                                 model=form, not_null=True,
                                                 log=True)
    return PikaResponse.success(data=model)


@router.get("/gateway/list", summary="查询请求地址列表")
async def list_gateway(name: str = '', gateway: str = '', env: int = None,
                       user_info=Depends(Permission(RoleEnum.MANAGER))):
    data = await GatewayDao.select_list(env=env, gateway=f"%{gateway}%", name=f"%{name}%")
    return PikaResponse.success(data)
