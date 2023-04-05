# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  PromptEnum.py
@Time    :  2022/5/2 5:57 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from enum import Enum


class PromptEnum(Enum):
    REGISTER_SUCCEED = "注册成功！"
    REGISTER_ERROR = "注册失败,"
    LOGIN_ERROR = "登录失败,该账号"
    LOGIN_SUCCEED = "登录成功！"
    GET_VERIFY_SUCCEED = "获取验证码成功！"
