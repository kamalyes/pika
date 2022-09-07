# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  msconfig.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  系统配置
"""
from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.system.msconfig import MsConfigDao
from app.enums.RbacEnum import RoleEnum
from app.schema.system import MsConfigSchema
from app.service import Permission

router = APIRouter()


@router.get("/config", summary="获取系统配置")
def get_system_config(user_info=Depends(Permission(RoleEnum.ADMIN))):
    configuration = MsConfigDao.get_config()
    return PikaResponse.success(configuration)


@router.post("/config/update", summary="更新系统配置")
def get_system_config(config: MsConfigSchema, user_info=Depends(Permission(RoleEnum.ADMIN))):
    MsConfigDao.update_config(config)
    return PikaResponse.success()
