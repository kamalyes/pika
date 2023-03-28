# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  exceres.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import status


class SystemException(Exception):
    def __init__(
        self,
        code: int = 500,
        detail: str = "Operation System Exception",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class AuthException(SystemException):
    def __init__(
        self, code: int = 401, detail: str = "Authentication failed", status_code: int = status.HTTP_401_UNAUTHORIZED,
    ):
        super().__init__(code, detail, status_code)


class AccessException(Exception):
    def __init__(self, code: int = 403, detail: str = "Access failed", status_code: int = status.HTTP_403_FORBIDDEN):
        super().__init__(code, detail, status_code)


class ValidException(SystemException):
    def __init__(
        self,
        code: int = 422,
        detail: str = "Parameter effect error",
        status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY,
    ):
        super().__init__(code, detail, status_code)
