# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
@Time    :  2022/5/3 2:15 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from fastapi import Body

from app.schema.base import PikaDeleteModel, PikaOnlyIdModel, PikaOnlyDescModel


class EditRoleModel(PikaOnlyIdModel, PikaOnlyDescModel):
    pass


class DelRoleModel(PikaDeleteModel):
    pass


class EditRoleRelModel(PikaOnlyDescModel):
    role_id: Optional[int] = Body(0, title="角色id")
    role_rel_id: Optional[int] = Body(0, title="角色应用id")


class DelRoleRelModel(PikaDeleteModel):
    pass
