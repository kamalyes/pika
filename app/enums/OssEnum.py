# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  OssEnum.py
@Time    :  2022/5/2 5:51 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from enum import Enum


class MiniOssTypeEnum(Enum):
    ALIYUN = "aliyun"
    GITEE = "gitee"
    QINIU = "qiniu"
    TENCENT = "tencent"
