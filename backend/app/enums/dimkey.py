# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  dimkey.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from config import PikaAppConfig


class RedisKeyEnum:
    DYNAMIC_CODE = f"{PikaAppConfig.APP_NAME}:auth:dynamic_code"  # 前端展示的动态码
    AUTH_TOKEN = f"{PikaAppConfig.APP_NAME}:auth:token"  # Token
    ONLINE_USER = f"{PikaAppConfig.APP_NAME}:user:online"  # 用户信息
    AUTH_VERIFY_CODE = f"{PikaAppConfig.APP_NAME}:auth:verify_code"  # 鉴权验证码
    LOGIN_LOCK = f"{PikaAppConfig.APP_NAME}:auth:login_lock"  # 限制登录锁
    REGISTER_NUMBER = f"{PikaAppConfig.APP_NAME}:register:number"  # 注册用户数
