# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  operation.py
@Time    :  2022/5/2 1:35 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class SqlOperationTypeEnum:
    ROOT = 1
    ONLY_INSERT = 2
    ONLY_DELETE = 3
    ONLY_UPDATE = 4
    ONLY_SELECT = 5
    ONLY_SELECT_AND_INSERT = 6
    ONLY_SELECT_AND_UPDATE = 7


class VerifyCodeEnum(IntEnum):
    FORGET_PWD = 1
