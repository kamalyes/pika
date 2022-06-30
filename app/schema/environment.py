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
from typing import Optional

from fastapi import Body

from app.enums.bytesize import ByteSizeEnum
from app.schema.base import PikaOnlyDescModel, PikaOnlyIdModel


class EnvironmentForm(PikaOnlyIdModel, PikaOnlyDescModel):
    name: Optional[str] = Body(..., max_length=ByteSizeEnum.LENGTH_50)
