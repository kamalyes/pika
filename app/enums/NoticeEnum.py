# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  NoticeEnum.py
@Time    :  2022/5/2 1:35 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class NoticeTypeEnum(IntEnum):
    EMAIL = 0
    DINGDING = 1
    WECHAT = 2
    FEISHU = 3
