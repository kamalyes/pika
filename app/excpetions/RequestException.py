# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  RequestException.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from fastapi import HTTPException


class AuthException(HTTPException):
    pass


class PermissionException(HTTPException):
    pass
