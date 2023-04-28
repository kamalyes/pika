# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.7
# Python Version 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/5/5 5:08 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import gettext
import os

from app.core.handler.translation import i18n

APP_BASE_HOME = os.path.dirname(os.path.abspath(__file__))
LOCALE_HOME = os.path.join(APP_BASE_HOME, "locale")

i18n.load_translations(
    {
        "zh_CN": gettext.translation(
            domain="messages",
            localedir=LOCALE_HOME,
            languages=["zh_CN"],
            fallback=True
        ),
        "en_GB": gettext.translation(
            domain="messages",
            localedir=LOCALE_HOME,
            languages=["en_GB"],
            fallback=True
        ),
    }
)