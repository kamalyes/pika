# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
@Time    :  2023/3/30 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseQuerySchema, BaseQueryTypeSchema
from fastapi import Body


class QueryRoleOutSchema(BaseQuerySchema):
    """角色查询序列化"""

    name: Optional[str] = Body(None, name="菜单名称", max_length=ByteSizeEnum.LENGTH_64)
    role_type: Optional[int] = Body(10, name="权限类型,10菜单权限,20用户组权限")
    status: Optional[int] = Body(10, name="状态 10 启用 20 禁用")
    description: Optional[str] = Body(None, name="描述", max_length=ByteSizeEnum.LENGTH_255)

    class Config:
        orm_mode = True


class QueryRoleInSchema(QueryRoleOutSchema, BaseQueryTypeSchema):
    """角色查询序列化"""



class EditRoleSchema(BaseQuerySchema):
    """创建/新增角色"""

    name: Optional[str] = Body(None, name="菜单名称", max_length=ByteSizeEnum.LENGTH_64)
    menus: Optional[list] = Body(..., name="菜单列表")
    role_type: Optional[int] = Body(10, name="权限类型,10菜单权限,20用户组权限")
    status: Optional[int] = Body(10, name="状态 10 启用 20 禁用")
    description: Optional[str] = Body(None, name="描述", max_length=ByteSizeEnum.LENGTH_255)
    pass

    class Config:
        orm_mode = True

    @staticmethod
    def return_menu(obj):
        """
        初始化menus
        source: 1,2,3,5
        target: [1, 2, 3, 5]
        :param obj:
        :return:
        """
        if obj.menus:
            return list(map(int, obj.menus.split(",")))
        return []
