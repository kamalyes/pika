# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  jsonpath_parser.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import json
from functools import lru_cache
from typing import Any

import jsonpath
from app.core.handler.jsonres import PikaJsonEncoder

from app.core.paramters.parser import Parser
from app.exceptions import CaseParametersError


class JSONPathParser(Parser, PikaJsonEncoder):
    @classmethod
    def get_source(cls, source):
        return source.get("response")
    
    @classmethod
    def parse(cls, source: dict, expression: str = "", **kwargs) -> Any:
        source = cls.get_source(source)
        if not source or not expression:
            raise CaseParametersError(
                f"parse out parameters failed, source or expression is empty")
        try:
            data = JSONPathParser.get_object(source)
            results = jsonpath.jsonpath(data, expression)
            if results is False:
                if not data and expression == "$..*":
                    # 说明想要全匹配并且没数据,直接返回data
                    return json.dumps(data, ensure_ascii=False)
                raise CaseParametersError(
                    "jsonpath match failed, please check your response or jsonpath.")
            return Parser.parse_result(results, "0")
        except CaseParametersError as e:
            raise e
        except Exception as err:
            raise CaseParametersError(
                f"parse json data error, please check jsonpath or json: {err}")

    @classmethod
    @lru_cache()
    def get_object(cls, json_str):
        return cls.safe_json_loads(json_str)

class BodyJSONPathParser(JSONPathParser):
    @classmethod
    def get_source(cls, source):
        return source.get("request_data")