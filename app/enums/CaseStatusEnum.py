# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  CaseStatusEnum.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class CaseStatus(IntEnum):
    # 1: 调试中 2: 暂时关闭 3: 正常运作
    debugging = 1
    closed = 2
    running = 3
