# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  mock.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  mock服务
"""

from app.core.handler.logger import PikaLogger


class MockDao(object):
    log = PikaLogger("MockDao")

    @staticmethod
    async def add_mock_deploy(request, **kwargs):
        pass

    @staticmethod
    async def delete_mock_deploy(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def update_mock_deploy(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def query_mock_deploy(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def call_mock_template(request):
        pass
