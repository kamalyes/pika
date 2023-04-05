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

from app.schema.base import BaseIPdSchema, BaseQuerySchema, BaseQueryTypeSchema, BaseOnlyIdSchema


class MenuSchema(BaseIPdSchema):
    path: Optional[str]
    component: Optional[str]
    title: Optional[str]
    name: Optional[str]
    is_link: Optional[bool]
    is_hide: Optional[bool]
    is_keepalive: Optional[bool]
    is_affix: Optional[bool]
    is_iframe: Optional[bool]
    icon: Optional[str]
    redirect: Optional[str]
    roles: Optional[str]
    sort: Optional[int]
    menu_type: Optional[int]
    active_menu: Optional[str]
    enabled_flag: Optional[bool]


class EditMenuSchema(MenuSchema):
    children: List[MenuSchema] = []

    class Config:
        orm_mode = True


class QueryMenuInSchema(MenuSchema, BaseQuerySchema, BaseQueryTypeSchema):
    pass


class QueryMenuOutSchema(EditMenuSchema):
    pass

    class Config:
        orm_mode = True
