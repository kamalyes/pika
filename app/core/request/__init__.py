# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.core.request.convertor import Convertor
from app.core.request.har_convertor import HarConvertor
from app.enums.ConvertorEnum import CaseConvertorType


def get_convertor(c: CaseConvertorType) -> (Convertor.convert, str):
    if c == CaseConvertorType.har:
        return HarConvertor.convert, CaseConvertorType.har.name
    return None, ""
