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
from typing import Any

from fastapi import APIRouter, Depends
from hutools.pagination import add_pagination, LimitOffsetPage
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.handler.jsonres import PikaResponse
from app.crud.rbac.menu import MenuDao
from app.models import async_db_session_iterator
from app.schema.base import BaseBatchDelIdsSchema
from app.schema.menu import QueryMenuInSchema, QueryMenuOutSchema, EditMenuSchema
from app.service import Permission

router = APIRouter()


@router.post('/menu/list', summary="获取所有菜单数据",
             response_model=LimitOffsetPage[QueryMenuOutSchema])
async def list_menu(request: QueryMenuInSchema = Depends(),
                    # user_info=Depends(Permission()),
                    db: AsyncSession = Depends(async_db_session_iterator)) -> Any:
    return await MenuDao.list_menu(db, request)


@router.post('/menu/edit', summary="新增或更新菜单")
async def save_or_update_menus(request: EditMenuSchema,
                               # user_info=Depends(Permission())
                               ):
    try:
        await MenuDao.save_or_update_menus(request=request, operator="ha758P")
    except Exception as exc:
        return PikaResponse.failed(detail=f"{exc}")
    return PikaResponse.success()


@router.delete('/menu/delete', summary="删除菜单")
def delete_menu(id: BaseBatchDelIdsSchema,
                user_info=Depends(Permission())):
    pass


add_pagination(router)
