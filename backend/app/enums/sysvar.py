# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  sysvar.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum

from hutools.time import Moment


class GlobalVarEnum:
    BANNER = r"""
         ____        __                  
        /\  _`\   __/\ \                 
        \ \ \L\ \/\_\ \ \/'\      __     
         \ \ ,__/\/\ \ \ , <    /'__`\   
          \ \ \/  \ \ \ \ \\`\ /\ \L\.\_ 
           \ \_\   \ \_\ \_\ \_\ \__/.\_\
            \/_/    \/_/\/_/\/_/\/__/\/_/
        """
    EMP_NO_START = "PK_"
    APP_NAME = "Pika"
    DEFAULT_PASSWORD = "1235678"
    APP_NAME_LOWER = APP_NAME.lower()
    PL_EMAIL = "mryu168@163.com"
    AGREE_MENT = "2022~2026"
    VERIFY_CODE_WHITE_LIST = ("888888", "Sweet")
    PWD_VALID_TIME = Moment.skew_date(180)  # 用户密码有效期
    SYS_NOW_TIME = Moment.get_now_time("%Y-%m-%d %H:%M:%S")  # 系统当前时间


class ValidTimeEnum(IntEnum):
    DF_VALID_TIME = 15 * 60  # 默认全局有效期
    LOGIN_LOCK_TIME = 60 * 60 * 1  # 登录锁：默认是1小时
    ERR_PWD_COUNT = 5  # 错误密码次数
    MAX_CODE_NUM = 5  # 限制一定频率下只能请求xx次前端动态码
    AUTH_VALID_TIME = 60 * 60 * 24 * 15  # AUTH有效期：默认是15天
    DYNAMIC_CODE_VALID_TIME = 2 * 60  # 前端动态码有效期（登录时防爬虫机制）
    AUTH_CODE_VALID_TIME = 5 * 60  # 鉴权验证码有效期（修改资料、密码等操作使用）
