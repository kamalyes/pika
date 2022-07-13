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
from typing import Optional, List

from app.schema.base import BaseQuerySchema, BaseQueryTypeSchema, BaseOnlyIdSchema


class MenuSchema(BaseOnlyIdSchema):
    path: Optional[str]
    component: Optional[str]
    title: Optional[str]
    name: Optional[str]
    isLink: Optional[bool]
    isHide: Optional[bool]
    isKeepAlive: Optional[bool]
    isAffix: Optional[bool]
    isIframe: Optional[bool]
    icon: Optional[str]
    parent_id: Optional[int]
    redirect: Optional[str]
    sort: Optional[int]
    menu_type: Optional[int]
    active_menu: Optional[str]
    enabled_flag: Optional[bool]


class EditMenuSchema(MenuSchema):
    roles: Optional[str]
    children: List[MenuSchema]

    class Config:
        orm_mode = True


class QueryMenuInSchema(MenuSchema, BaseQuerySchema, BaseQueryTypeSchema):
    pass


class QueryMenuOutSchema(EditMenuSchema):
    pass

    class Config:
        orm_mode = True
