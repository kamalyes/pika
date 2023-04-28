# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  notification.py
@Time    :  2023/3/30 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import List, Optional
from pydantic import BaseModel


class NotificationSchema(BaseModel):
    personal: Optional[list[str]] = None
    broadcast: Optional[list[str]] = None
