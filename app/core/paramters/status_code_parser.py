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
import json

from app.core.paramters.parser import Parser


class StatusCodeParser(Parser):
    @staticmethod
    def parse(source: dict, expression: str = None, idx: str = None) -> str:
        return json.dumps(source.get("status_code"))
