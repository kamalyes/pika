# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  redis_config.py
@Time    :  2023/3/30 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import Optional
from pydantic import validator

from app.schema.base import BaseOnlyIdSchema, PikaBaseModel


class RedisConfigSchema(BaseOnlyIdSchema):
    name: Optional[str] = None
    addr: Optional[str] = None
    db: Optional[int] = 0
    username: Optional[str] = None
    password: Optional[str] = None
    cluster: bool = False
    env: Optional[str] = None

    # noinspection PyMethodParameters
    @validator("name", "addr", "cluster", "db", "env")
    def data_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
