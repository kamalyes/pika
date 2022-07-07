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
from app.service.itst.apitest import router as aiptest_router
from app.service.itst.functest import router as functest_router
from app.service.itst.testcase import router as testcase_router
from app.service.itst.testplan import router as testplan_router
