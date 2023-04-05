# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gconfig.py
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Body

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseOnlyIdSchema


class GConfigSchema(BaseOnlyIdSchema):
    key: str = Body(..., name="key", max_length=ByteSizeEnum.LENGTH_56)
    value: str = Body(..., name="value", max_length=ByteSizeEnum.LENGTH_1W)
    env: str = Body(..., name="环境id", max_length=ByteSizeEnum.LENGTH_32)
    key_type: int = Body(..., name="参数类型 0: string 1: json 2: yaml")
    enabled_flag: bool = Body(True, name="启用标识")
