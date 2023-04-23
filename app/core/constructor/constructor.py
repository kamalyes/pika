# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  constructor.py
@Time    :  2022/6/10 6:53 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from abc import ABC

class ConstructorAbstract(ABC):

    @classmethod
    def get_name(cls, constructor):
        return '前置条件' if not constructor.suffix else '后置条件'
