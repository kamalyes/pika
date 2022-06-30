# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  apitest.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  接口测试
"""
from app.core.handler.logger import PikaLogger


class ApiCaseDao(object):
    log = PikaLogger("ApiCaseDao")

    @staticmethod
    async def add_apicase(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def delete_apicase(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def update_apicase(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def query_apicase(request, emp_no, **kwargs):
        pass
