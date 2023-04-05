# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  DatabaseEnum.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Depends, APIRouter
from app.core.handler.exceres import DbExecuteException, SystemException

from app.core.handler.jsonres import PikaResponse
from app.crud.itstem.database import DbConfigDao
from app.enums.RbacEnum import RoleEnum
from app.models import DatabaseHelper, db_helper
from app.schema.base import BaseOnlyPagingSchema
from app.schema.database import DatabaseSchema
from app.service import Permission

router = APIRouter()


@router.post("/dbconfig/insert", summary="增加数据库配置")
async def insert_dbconfig(form: DatabaseSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    try:
        await DbConfigDao.insert_database(form, user_info['emp_no'])
        return PikaResponse.success()
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.delete("/dbconfig/delete", summary="删除数据库配置")
async def delete_dbconfig(id: str, user_info=Depends(Permission(RoleEnum.ADMIN))):
    try:
        await DbConfigDao.delete_database(id, user_info['emp_no'])
        return PikaResponse.success()
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.post("/dbconfig/update", summary="更新数据库配置")
async def update_dbconfig(form: DatabaseSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    try:
        await DbConfigDao.update_database(form, user_info['emp_no'])
        return PikaResponse.success()
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.get("/dbconfig/list", summary="查询数据库配置")
async def list_dbconfig(name: str = None, database: str = None, env: str = None,
                        user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        data = await DbConfigDao.list_database(name, database, env)
        return PikaResponse.success(data=data)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.get("/dbconfig/connect", summary="测试数据库连接")
async def connect_test(sql_type: int, host: str, port: int, username: str, password: str,
                       database: str,
                       user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        data = await db_helper.get_connection(sql_type, host, port, username, password, database)
        if data is None:
            raise DbExecuteException(detail="测试连接失败")
        await DatabaseHelper.test_connection(data.get("session"))
        return PikaResponse.success(message="连接成功")
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
