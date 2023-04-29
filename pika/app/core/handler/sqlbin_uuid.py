# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  sqlbin_uuid.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from sqlalchemy.types import String, TypeDecorator

from app.enums.ByteSizeEnum import ByteSizeEnum

ENABLE_DB_TYPE = ["postgresql", "mysql"]


class BinaryUUID(TypeDecorator):
    """
    Platform-independent UUID type.
    """

    impl = String

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(String(ByteSizeEnum.LENGTH_64))

    def process_bind_param(self, value, dialect):
        return value if value is None else str(value)

    def process_result_value(self, value, dialect):
        return value if value is None else str(value)
