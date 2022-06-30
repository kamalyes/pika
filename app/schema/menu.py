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
from typing import Optional

from fastapi import Query, Body

from app.enums.bytesize import ByteSizeEnum
from app.schema.base import PikaDeleteModel, PikaQueryModel, PikaQueryTypeModel, PikaOnlyDescModel, PikaOnlyDelModel


class EditMenuModel(PikaOnlyDescModel, PikaOnlyDelModel):
    son_id: Optional[int] = Body(None, title="子菜单id")
    title: Optional[str] = Body(..., title="菜单名称", max_length=ByteSizeEnum.LENGTH_70)
    icon: Optional[str] = Body(..., title="菜单图标", max_length=ByteSizeEnum.LENGTH_70)
    path: Optional[str] = Body(..., title="路由地址", max_length=ByteSizeEnum.LENGTH_255)
    type: Optional[str] = Body(..., title="菜单类型：用于区分模块、目录、菜单、按钮", max_length=ByteSizeEnum.LENGTH_20)
    component: Optional[str] = Body(..., title="菜单对应的组件路径", max_length=ByteSizeEnum.LENGTH_255)
    hidden: Optional[int] = Body(..., title="是否隐藏此菜单")
    parent_id: Optional[int] = Body(None, title="父菜单id")


class DelMenuModel(PikaDeleteModel):
    pass


class QueryMenuModel(PikaQueryModel, PikaQueryTypeModel):
    menu_title: Optional[int] = Query(None, title="菜单名称")
