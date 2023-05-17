# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
# noinspection PyPep8Naming
from app.service.itst.api.testplan import router as api_testplan_router
from app.service.itst.functest.functest import router as functest_router
from app.service.itst.api.testcase import router as api_testcase_router
from app.service.itst.api.jmeter import router as jmeter_router
