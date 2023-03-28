# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  RedisEnum.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.enums.SysvarEnum import PikaGlobalVarEnum


class RedisKeyEnum:
    # 前端展示的动态码
    DYNAMIC_CODE = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}:auth:dynamic_code"
    AUTH_TOKEN = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}:auth:token"  # Token
    # 用户信息
    ONLINE_USER = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}:user:online"
    # 鉴权验证码
    FORGET_PWD_VERIFYCODE = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}:auth:forget_pwd_code"
    # 注册验证码
    REGISTER_VERIFYCODE = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}:auth:register_verifycode"
    # 登录验证码
    EMAIL_LOGIN_VERIFYCODE = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}:auth:EMAIL_LOGIN_VERIFYCODE"
    # 限制登录锁
    LOGIN_LOCK = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}:auth:login_lock"
    # 注册用户数
    REGISTER_NUMBER = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}:register:number"
