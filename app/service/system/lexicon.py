# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  lexicon.py
@Time    :  2022/6/7 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    : 　词库
"""
from typing import Any

from fastapi import APIRouter, Depends
from hutools.pagination import LimitOffsetPage, add_pagination
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.system.lexicon import SensitiveWordDao, AliasWordDao
from app.models import pagination_db
from app.schema.lexicon import EditSensitiveWordModel, DelSensitiveWordModel, \
    QuerySensitiveWordOutModel, \
    QuerySensitiveWordInModel, EditAliasWordModel, QueryAliasWordOutModel, QueryAliasWordInModel, \
    DelAliasWordModel
from app.service import Permission

router = APIRouter()


@router.post("/sensitive_word/add", summary="增加敏感词")
async def add_sensitive_word(request: EditSensitiveWordModel,
                             emp_no=Depends(Permission(return_emp_no=True))):
    return await SensitiveWordDao.add_sensitive_word(request=request, emp_no=emp_no)


@router.delete("/sensitive_word/delete", summary="删除敏感词（软删）")
async def delete_sensitive_word(request: DelSensitiveWordModel = Depends(),
                                emp_no=Depends(Permission(return_emp_no=True))):
    return await SensitiveWordDao.delete_sensitive_word(request=request, emp_no=emp_no)


@router.post("/sensitive_word/update", summary="编辑敏感词")
async def update_sensitive_word(request: EditSensitiveWordModel,
                                emp_no=Depends(Permission(return_emp_no=True))):
    return await SensitiveWordDao.update_sensitive_word(request=request, emp_no=emp_no)


@router.get("/sensitive_word/list", summary="分页获取敏感词",
            response_model=LimitOffsetPage[QuerySensitiveWordOutModel])
async def query_sensitive_word(request: QuerySensitiveWordInModel = Depends(),
                               emp_no=Depends(Permission(return_emp_no=True)),
                               db: AsyncSession = Depends(pagination_db)) -> Any:
    return await SensitiveWordDao.query_sensitive_word(db, request)


@router.post("/alias_word/add", summary="增加化名词")
async def add_alias_word(request: EditAliasWordModel,
                         emp_no=Depends(Permission(return_emp_no=True))):
    return await AliasWordDao.add_alias_word(request=request, emp_no=emp_no)


@router.delete("/alias_word/delete", summary="删除化名词（软删）")
async def delete_alias_word(request: DelAliasWordModel = Depends(),
                            emp_no=Depends(Permission(return_emp_no=True))):
    return await AliasWordDao.delete_alias_word(request=request, emp_no=emp_no)


@router.post("/alias_word/update", summary="编辑化名词")
async def update_alias_word(request: EditAliasWordModel,
                            emp_no=Depends(Permission(return_emp_no=True))):
    return await AliasWordDao.update_alias_word(request=request, emp_no=emp_no)


@router.get("/alias_word/list", summary="分页获取化名词",
            response_model=LimitOffsetPage[QueryAliasWordOutModel])
async def query_alias_word(request: QueryAliasWordInModel = Depends(),
                           emp_no=Depends(Permission(return_emp_no=True)),
                           db: AsyncSession = Depends(pagination_db)) -> Any:
    return await AliasWordDao.query_alias_word(db, request)


add_pagination(router)
