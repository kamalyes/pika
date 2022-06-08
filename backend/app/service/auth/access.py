# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  access.py
@Time    :  2022/5/3 3:05 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/menu/add", name="添加菜单")
async def add_menu():
    pass


@router.put("/menu/update", name="更新菜单信息")
async def update_menu():
    pass


@router.delete("/menu/delete", name="删除菜单")
async def delete_menu():
    pass


@router.get("/menu/query", name="查询菜单配置")
async def query_menu():
    pass


@router.post("/role/add", name="添加角色配置")
async def add_role():
    pass


@router.put("/role/update", name="更新角色配置信息")
async def update_role():
    pass


@router.delete("/role/delete", name="删除角色配置")
async def delete_role():
    pass


@router.get("/role/query", name="查询角色配置")
async def query_role():
    pass


@router.post("/role/bind", name="绑定角色")
async def bind_role():
    pass


@router.delete("/role/unbind", name="解绑角色")
async def unbind_role():
    pass


@router.post("/action/bind", name="绑定活动")
async def bind_action():
    pass


@router.delete("/action/unbind", name="解绑活动")
async def unbind_action():
    pass


@router.get("/action/query", name="查询活动")
async def query_action():
    pass
