# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  action.py
@Time    :  2022/5/3 3:05 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import APIRouter
from hutools.pagination import add_pagination

router = APIRouter()


@router.post("/action/add", name="添加活动")
async def add_action():
    pass


@router.put("/action/update", name="更新活动配置信息")
async def update_action():
    pass


@router.delete("/action/delete", name="删除活动配置")
async def delete_action():
    pass


@router.get("/action/query", name="查询活动配置")
async def query_action():
    pass


@router.post("/action/bind", name="给成员绑定活动")
async def bind_action():
    pass


@router.delete("/action/unbind", name="给成员解绑活动")
async def unbind_action():
    pass


add_pagination(router)
