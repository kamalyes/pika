# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  environment.py
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.schema.base import BaseOnlyDescSchema, BaseOnlyIdSchema, BaseOnlyNameSchema


class EnvironmentSchema(BaseOnlyIdSchema, BaseOnlyDescSchema, BaseOnlyNameSchema):
    pass
