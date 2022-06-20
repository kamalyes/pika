# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  functest.py
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  功能测试
"""

from app.core.handler.logger import PikaLogger


class FuncCaseDao(object):
    log = PikaLogger("FuncCaseDao")

    @staticmethod
    async def add_funccase(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def delete_funccase(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def update_funccase(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def query_funccase(request, emp_no, **kwargs):
        pass
