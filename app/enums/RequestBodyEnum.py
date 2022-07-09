# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  RequestBodyEnum.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class ReqBodyTypeEnum(IntEnum):
    none = 0
    json = 1
    form = 2
    x_form = 3
    binary = 4
    graphQL = 5
