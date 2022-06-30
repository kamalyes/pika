# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  constructor
@Time    :  2022/6/18 7:06 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from app.models.constructor import PikaConstructor


class ConstructorHelper(object):

    def parse(self, path, data: PikaConstructor):
        pass


class TestCaseConstructorHelper(ConstructorHelper):

    def parse(self, path, data: PikaConstructor):
        pass
