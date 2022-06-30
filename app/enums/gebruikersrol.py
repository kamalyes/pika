# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gebruikersrol.py
@Time    :  2022/5/2 1:36 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class RoleEnum(IntEnum):
    ROOT = 999
    ADMIN = 888
    MANAGER = 777
    ORDINARY = 666
