# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
@Time    :  2022/5/3 2:15 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional, List

from fastapi import Body

from app.enums.bytesize import ByteSizeEnum
from app.schema.base import PikaDeleteModel, PikaOnlyIdModel, PikaOnlyDescModel, PikaQueryModel, PikaQueryTypeModel, \
    PikaOnlyEmpNoModel


class RoleGlobalModel(PikaOnlyIdModel, PikaOnlyDescModel):
    name: Optional[str] = Body(None, title="角色名称", max_length=ByteSizeEnum.LENGTH_255)
    role_type: Optional[int] = Body(None, title="角色权限类型，10菜单权限，20用户组权限")
    menus_id: Optional[str] = Body(None, title="菜单id", max_length=ByteSizeEnum.LENGTH_64)


class EditRoleModel:
    def __init__(self, role: List[RoleGlobalModel] = Body(..., title="角色信息")):
        self.role = role


class DelRoleModel(PikaDeleteModel):
    pass


class QueryRoleInModel(PikaQueryModel, PikaQueryTypeModel, RoleGlobalModel):
    pass


class QueryRoleOutModel(PikaQueryModel, RoleGlobalModel):
    class Config:
        orm_mode = True


class BindRoleModel(PikaOnlyEmpNoModel):
    id: Optional[int] = Body(0, title="id")
    role_id: Optional[int] = Body(0, title="角色id")


class ApplyRoleModel(PikaOnlyDescModel):
    role_id: Optional[int] = Body(..., title="角色id")


class AuditRoleModel(PikaOnlyIdModel, PikaOnlyDescModel):
    pass


class DelRoleRelModel(PikaDeleteModel):
    pass
