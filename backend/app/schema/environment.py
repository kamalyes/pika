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
from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel


class EnvironmentForm(BaseModel):
    id: int = None
    name: str
    description: str = None

    @validator("name")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
