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

from app.schema.base import BaseOnlyEnvIdSchema, BaseOnlyIdSchema, PikaBaseModel
from pydantic import validator


class RedisConfigSchema(BaseOnlyIdSchema, BaseOnlyEnvIdSchema):
    name: Optional[str] = None
    addr: Optional[str] = None
    db: Optional[int] = 0
    username: Optional[str] = None
    password: Optional[str] = None
    cluster: bool = False

    # noinspection PyMethodParameters
    @validator("name", "addr", "cluster", "db")
    def data_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
