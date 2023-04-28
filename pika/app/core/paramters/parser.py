# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  parser.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import json
import random
from typing import Any
from app.core.handler.jsonres import PikaJsonEncoder

from app.exceptions import CaseParametersError


class Parser(PikaJsonEncoder):
    @staticmethod
    def parse(source: dict, expression: str = None, **kwargs) -> Any:
        raise NotImplementedError

    @classmethod
    def parse_result(cls, data: list, match_index: str = None):
        if len(data) == 0:
            return "null"
        # 如果是数字
        length = len(data)
        if match_index is not None:
            if match_index.isdigit():
                idx = int(match_index)
                if idx >= length or idx < -length:
                    raise CaseParametersError(
                        f"results length is {length}, index is not in [{-length}, {length})")
                return cls.safe_json_dumps(data[idx], ensure_ascii=False)
            if match_index.lower() == "random":
                # 随机选取
                return cls.safe_json_dumps(random.choice(data), ensure_ascii=False)
            if match_index.lower() == "all":
                return cls.safe_json_dumps(data, ensure_ascii=False)
            raise CaseParametersError(
                f"invalid match index: {match_index}, not number or random")
        return cls.safe_json_dumps(data, ensure_ascii=False)
