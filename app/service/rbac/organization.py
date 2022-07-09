# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  organization.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  组织架构
"""

from fastapi import APIRouter, Depends

from app.schema.organization import DelUserGroupModel, QueryDeptRelModel

router = APIRouter()


@router.post("/group/add", summary="添加集团")
async def add_user_group():
    pass


@router.put("/group/update", summary="更新集团信息")
async def update_user_group():
    pass


@router.delete("/group/delete", dependencies=[], name="删除集团")
async def delete_user_group(request: DelUserGroupModel = Depends()):
    pass


@router.get("/group/list", summary="查询集团信息")
async def query_user_group():
    pass


@router.post("/department/add", summary="添加部门")
async def add_department():
    pass


@router.put("/department/update", summary="更新部门信息")
async def update_department():
    pass


@router.delete("/department/delete", dependencies=[], name="删除部门")
async def delete_department():
    pass


@router.post("/department/relation/bind", summary="建立成员与部门之间的关联")
async def bind_department_relation():
    pass


@router.delete("/department/relation/unbind", dependencies=[], name="解除成员与部门之间的关联")
async def unbind_department_relation():
    pass


@router.get("/department/relation/list", summary="查询用户所在部门信息")
async def query_department_relation(request: QueryDeptRelModel = Depends()):
    pass
