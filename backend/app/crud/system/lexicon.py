# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  lexicon.py
@Time    :  2022/6/7 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    : 　词库
"""
from app.core.handler.logger import PikaLogger


class SensitiveWordDao(object):
    log = PikaLogger("SensitiveWordDao")

    @staticmethod
    async def add_sensitive_word(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def delete_sensitive_word(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def update_sensitive_word(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def query_sensitive_word(request, emp_no, **kwargs):
        pass


class AliasWordDao(object):
    log = PikaLogger("AliasWordDao")

    @staticmethod
    async def add_alias_word(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def delete_alias_word(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def update_alias_word(request, emp_no, **kwargs):
        pass

    @staticmethod
    async def query_alias_word(request, emp_no, **kwargs):
        pass
