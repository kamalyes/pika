# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  convertor.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import List

from app.schema.request import RequestInfoSchema


class Convertor(object):

    @staticmethod
    def convert(file, regex: str = None) -> List[RequestInfoSchema]:
        raise NotImplementedError
