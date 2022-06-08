# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  kerberos.py
@Time    :  2022/5/3 1:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/issue/add", name="增加推荐的密保问题")
async def add_encrypt_issue():
    pass


@router.delete("/issue/delete", name="删除推荐的密保问题")
async def delete_encrypt_issue():
    pass


@router.post("/issue/update", name="编辑推荐的密保问题")
async def update_encrypt_issue():
    pass


@router.get("/issue/query", name="分页获取推荐的密保问题")
async def query_encrypt_issue():
    pass


@router.post("/security/add", name="添加/更新密保信息")
async def add_security():
    pass


@router.delete("/security/delete", name="删除密保问题")
async def delete_security():
    pass


@router.post("/security/update", name="编辑密保问题")
async def update_security():
    pass


@router.get("/security/info", dependencies=[], name="查询用户自己设置过的密保信息")
async def query_security():
    pass
