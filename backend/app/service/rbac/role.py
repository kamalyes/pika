# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
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


@router.post("/role/bind", name="给成员绑定角色")
async def bind_role():
    pass


@router.delete("/role/unbind", name="给成员解绑角色")
async def unbind_role():
    pass


add_pagination(router)
