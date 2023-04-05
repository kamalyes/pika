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
from app.crud.itstem.gateway import GatewayDao
from app.enums.RbacEnum import RoleEnum
from app.enums.SysVarEnum import ValidTimeEnum
from app.models import async_db_session_iterator
from app.models.gateway import GatewayModel
from app.schema.gateway import PikaGatewaySchema
from app.service import Permission

router = APIRouter()


@router.post("/gateway/insert", summary="添加请求地址")
async def insert_gateway(form: PikaGatewaySchema, user_info=Depends(Permission(RoleEnum.MANAGER))):
    model = GatewayModel(**form.dict(), operator=user_info['emp_no'])
    model = await GatewayDao.insert(model=model, log=True)
    return PikaResponse.success(data=model)


@router.delete("/gateway/delete", summary="删除请求地址")
async def delete_gateway(id: str, user_info=Depends(Permission(RoleEnum.MANAGER)),
                         session=Depends(async_db_session_iterator)):
    await GatewayDao.delete_record_by_id(session=session, operator=user_info['emp_no'], value=id, log=True)
    return PikaResponse.success(message=f'删除成功,因redis缓存结果需等待{ValidTimeEnum.GLOBAL_SELECT_LIST_TIME.value}s后查询')


@router.post("/gateway/update", summary="编辑请求地址")
async def insert_gateway(form: PikaGatewaySchema, user_info=Depends(Permission(RoleEnum.MANAGER))):
    model = await GatewayDao.update_record_by_id(operator=user_info['emp_no'], log=True,  model=form, not_null=True)
    return PikaResponse.success(data=model)


@router.get("/gateway/list", summary="查询请求地址列表")
async def list_gateway(name: str = '', address: str = '', env: str = None,
                       user_info=Depends(Permission(RoleEnum.MANAGER))):
    data = await GatewayDao.select_list(env=env, address=f"%{address}%", name=f"%{name}%")
    return PikaResponse.success(data)
