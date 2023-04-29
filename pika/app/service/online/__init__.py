# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
# noinspection PyPep8Naming
from app.service.online.redis import router as redis_router
from app.service.online.script import router as script_router
from app.service.online.sql import router as sql_router
