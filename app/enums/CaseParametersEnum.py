# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  CaseParametersEnum.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class CaseParametersEnum(IntEnum):
    TEXT = 0
    JSON = 1
    HEADER = 2
    COOKIE = 3
    STATUS_CODE = 4
    BODY_REGEX = 5
    BODY_JSON = 6
    REQUEST_HEADER = 7
