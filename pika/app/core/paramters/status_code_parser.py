# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  status_code_parser.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.core.handler.jsonres import PikaJsonEncoder
from app.core.paramters.parser import Parser


class StatusCodeParser(Parser, PikaJsonEncoder):
    @classmethod
    def parse(cls, source: dict, expression: str = None, idx: str = None) -> str:
        return cls.safe_json_dumps(source.get("status_code"))
