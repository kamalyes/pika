# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  CertEnum.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import IntEnum


class CertType(IntEnum):
    windows = 0
    linux = 1
    macos = 2
    ios = 3
    android = 4

    def get_suffix(self):
        if self == CertType.windows:
            return "p12"
        if self in (CertType.linux, CertType.macos, CertType.ios):
            return "pem"
        if self == CertType.android:
            return "cer"
        raise Exception("unsupported cert type")
