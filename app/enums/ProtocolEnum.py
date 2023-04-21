# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  ProtocolTypeEnum.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class ProtocolTypeEnum(IntEnum):
    http = 1
    grpc = 2
    dubbo = 3
    websocket = 4
