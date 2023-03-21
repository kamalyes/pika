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
from app.core.paramters.jsonpath_parser import JSONPathParser
from app.core.paramters.kv_parser import HeaderParser, CookieParser
from app.core.paramters.regex_parser import RegexParser
from app.core.paramters.status_code_parser import StatusCodeParser
from app.enums.CaseParametersEnum import CaseParametersEnum


# noinspection PyPep8Naming
def parameters_parser(parameter_type: CaseParametersEnum):
    if parameter_type in (CaseParametersEnum.TEXT, CaseParametersEnum.BODY_REGEX):
        return RegexParser.parse
    if parameter_type in (CaseParametersEnum.JSON, CaseParametersEnum.BODY_JSON):
        return JSONPathParser.parse
    if parameter_type in (CaseParametersEnum.HEADER, CaseParametersEnum.REQUEST_HEADER):
        return HeaderParser.parse
    if parameter_type == CaseParametersEnum.COOKIE:
        return CookieParser.parse
    return StatusCodeParser.parse
