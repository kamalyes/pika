# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  regex_parser.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import re
from typing import Any

from app.core.paramters.parser import Parser
from app.exceptions import CaseParametersError


class RegexParser(Parser):
    @classmethod
    def get_source(cls, source: dict):
        return source.get("response")

    @classmethod
    def parse(cls, source: dict, expression: str = "", idx: str = None) -> Any:
        try:
            source = cls.get_source(source)
            if not source or not expression:
                raise CaseParametersError(
                    f"parse out parameters failed, source or expression is empty")
            if idx is None:
                raise CaseParametersError(
                    "index is empty, you must provide index for regex match results.")
            pattern = re.compile(expression)
            result = re.findall(pattern, source)
            if len(result) == 0:
                raise CaseParametersError(
                    f"regex match failed, please check your regex: {expression}")
            return Parser.parse_result(result, idx)
        except CaseParametersError as e:
            raise e
        except Exception as err:
            raise CaseParametersError(
                f"parse regex text error, please check regex or text: {err}")
            
class BodyRegexParser(RegexParser):
    @classmethod
    def get_source(cls, source: dict):
        return source.get("request_data")