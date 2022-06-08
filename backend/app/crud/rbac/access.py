# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/5/3 2:15 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  access authorization control （访问权限控制）
"""
from app.core.handler.jsonres import PikaResponse


async def add_menu(**kwargs):
    return PikaResponse.success(message="成功添加新菜单")


async def update_menu(**kwargs):
    return PikaResponse.success(message="修改菜单信息成功")


async def delete_menu(**kwargs):
    return PikaResponse.success(message=f"批量删除菜单成功")


async def add_role_config(**kwargs):
    return PikaResponse.success(message="成功添加新角色")


async def update_role_config(**kwargs):
    return PikaResponse.success(message="修改角色信息成功")


async def del_role_config(**kwargs):
    return PikaResponse.success(message=f"批量删除角色成功")


async def query_role_config():
    pass


async def add_role_rel(**kwargs):
    return PikaResponse.success(message="成功添加新角色")


async def update_role_rel(**kwargs):
    return PikaResponse.success(message="修改角色信息成功")


async def del_role_rel(**kwargs):
    return PikaResponse.success(message=f"批量删除角色应用信息成功")


async def add_role_menu(**kwargs):
    return PikaResponse.success(message="成功添加新角色")
