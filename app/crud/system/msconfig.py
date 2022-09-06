# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  msconfig.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  系统配置
"""
import os

import yaml
from hutools.core import System

from app.enums.SysvarEnum import ValidTimeEnum
from app.middleware.xredis import RedisHelper
from config import PikaAppConfig


class MsConfigDao(object):

    @staticmethod
    @RedisHelper.cache("msconfig", ValidTimeEnum.SYSTEM_CONFIG_VALID_TIME.value)
    def get_config():
        try:
            return PikaAppConfig.GLOBAL_POOL_CONFIG
        except Exception as e:
            raise Exception(f"获取系统设置失败, {e}")

    @staticmethod
    @RedisHelper.up_cache("msconfig")
    def update_config(config):
        try:
            filepath = PikaAppConfig.GLOBAL_POOL_CONFIG_FILEPATH
            with open(filepath, "w") as output:
                yaml.safe_dump(config, output, default_flow_style=False)
        except Exception as e:
            raise Exception(f"更新系统设置失败, {e}")
