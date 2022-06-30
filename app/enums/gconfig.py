# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gconfig.py
@Time    :  2022/5/2 1:36 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class GConfigParserEnum(IntEnum):
    string = 0
    json = 1
    yaml = 2


# 全局变量的类型
class GConfigTypeEnum:
    case = 0
    constructor = 1
    asserts = 2

    @staticmethod
    def value(val):
        if val == 0:
            return "用例"
        if val == 1:
            return "前后置条件"
        return "断言"
