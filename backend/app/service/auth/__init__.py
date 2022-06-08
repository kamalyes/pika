# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.service.auth.access import router as menus_router
from app.service.auth.kerberos import router as kerberos_router
from app.service.auth.user import router as user_router
from app.service.auth.organization import router as organization_router
