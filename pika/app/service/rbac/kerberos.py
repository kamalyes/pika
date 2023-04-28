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
from typing import Any

from fastapi import APIRouter, Depends
from custard.pagination import LimitOffsetPage, add_pagination
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.rbac.kerberos import KerberosDao
from app.models import async_db_session_iterator
from app.schema.kerberos import EditKerberosItemSchema, DelKerberosSchema, \
    QueryKerberosOutSchema, QueryKerberosInSchema
from app.service import Permission

router = APIRouter()


@router.post("/issue/add", summary="增加推荐的密保问题")
async def add_encrypt_issue(security: EditKerberosItemSchema = Depends(),
                            user_info=Depends(Permission())):
    return await KerberosDao.add_encrypt_issue(security=security, emp_no=user_info["emp_no"])


@router.delete("/issue/delete", summary="删除推荐的密保问题(非软删,谨慎操作)")
async def delete_encrypt_issue(request: DelKerberosSchema = Depends(),
                               user_info=Depends(Permission())):
    return await KerberosDao.delete_encrypt_issue(request=request)


@router.post("/issue/update", summary="编辑推荐的密保问题")
async def update_encrypt_issue(security: EditKerberosItemSchema = Depends(),
                               user_info=Depends(Permission())):
    return await KerberosDao.update_encrypt_issue(request=security, emp_no=user_info["emp_no"])


@router.get("/issue/list", summary="分页获取推荐的密保问题",
            response_model=LimitOffsetPage[QueryKerberosOutSchema])
async def query_encrypt_issue(request: QueryKerberosInSchema = Depends(),
                              user_info=Depends(Permission()),
                              db: AsyncSession = Depends(async_db_session_iterator)) -> Any:
    return await KerberosDao.query_encrypt_issue(db, request)


add_pagination(router)
