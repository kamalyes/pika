# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  execres.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from fastapi import status
from hutools.limiter import RateLimitException

from app.enums.statuscode import SysFailedCodeEnum


class ValidException(Exception):
    def __init__(
        self,
        code: int = 422,
        status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail: str = "Parameter effect error",
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class RegisterException(Exception):
    def __init__(
        self,
        code: int = 500,
        detail: str = "Register failed",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class LoginException(Exception):
    def __init__(
        self,
        code: int = 500,
        detail: str = "Login failed",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class AuthException(Exception):
    def __init__(
        self,
        code: int = 401,
        detail: str = "Authentication failed",
        status_code: int = status.HTTP_401_UNAUTHORIZED,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class TokenException(Exception):
    def __init__(
        self,
        code: int = 401,
        detail: str = "Token failed",
        status_code: int = status.HTTP_401_UNAUTHORIZED,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class AccessException(Exception):
    def __init__(
        self,
        code: int = 403,
        detail: str = "Access failed",
        status_code: int = status.HTTP_403_FORBIDDEN,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class OperationException(Exception):
    def __init__(
        self,
        code: int = 400,
        detail: str = "Operation failed",
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class ThirdException(Exception):
    def __init__(
        self,
        code: int = 500,
        detail: str = "Third Service Exception",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class DbExecuteException(Exception):
    def __init__(
        self,
        code: int = 500,
        detail: str = "Database operation failed",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


class RedisException(Exception):
    def __init__(
        self,
        code: int = SysFailedCodeEnum.REDIS_ERROR,
        detail: str = "Redis operation failed",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        self.code = code
        self.detail = detail
        self.status_code = status_code


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
