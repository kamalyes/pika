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
from typing import Tuple

from app.core.request.convertor import Convertor
from app.core.request.har_convertor import HarConvertor
from app.enums.ConvertorEnum import CaseConvertorTypeEnum


def get_convertor(ct: CaseConvertorTypeEnum) -> Tuple[Convertor.convert, str]:
    if ct == CaseConvertorTypeEnum.har:
        return HarConvertor.convert, CaseConvertorTypeEnum.har.name
    return None, ""
