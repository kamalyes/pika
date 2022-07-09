# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  menu.py
@Time    :  2022/6/16 8:15 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from fastapi import APIRouter
from hutools.pagination import add_pagination

router = APIRouter()


@router.post("/menu/add", summary="添加菜单")
async def add_menu():
    pass


@router.put("/menu/update", summary="更新菜单信息")
async def update_menu():
    pass


@router.delete("/menu/delete", summary="删除菜单")
async def delete_menu():
    pass


@router.get("/menu/list", summary="查询菜单配置")
async def query_menu():
    pass


add_pagination(router)
