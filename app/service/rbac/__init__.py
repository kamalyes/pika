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
from app.service.rbac.action import router as access_router
from app.service.rbac.kerberos import router as kerberos_router
from app.service.rbac.menu import router as menus_router
from app.service.rbac.organization import router as organization_router
from app.service.rbac.role import router as roles_router
from app.service.rbac.user import router as user_router
