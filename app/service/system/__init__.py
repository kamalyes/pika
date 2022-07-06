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
from app.service.system.history import router as history_router
from app.service.system.lexicon import router as lexicon_router
from app.service.system.minioss import router as mini_oss_router
from app.service.system.notification import router as notice_router
from app.service.system.operation import router as operation_log_router
