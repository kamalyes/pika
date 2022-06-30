# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  database.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class DatabaseEnum(IntEnum):
    """
    数据库类型枚举
    """
    MYSQL = 0  # mysql
    POSTGRESQL = 1  # pg
