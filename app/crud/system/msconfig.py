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

import yaml
from app.core.handler.exceres import SystemException

from app.enums.SysvarEnum import ValidTimeEnum
from app.middleware.xredis import RedisHelper
from config import PikaAppConfig


class MsConfigDao(object):

    @staticmethod
    @RedisHelper.cache("msconfig", ValidTimeEnum.SYSTEM_CONFIG_VALID_TIME.value)
    def get_config():
        try:
            return PikaAppConfig
        except Exception as e:
            raise SystemException(detail=f"获取系统设置失败, {e}")

    @classmethod
    @RedisHelper.up_cache("msconfig")
    async def update_config(cls, config):
        try:
            filepath = PikaAppConfig.GLOBAL_POOL_CONFIG_FILEPATH
            new_config, old_config = config.dict(), cls.get_config()
            for key, value in new_config.items():
                if value:
                    get_old_value = old_config.get(key, None)
                    if value != get_old_value:
                        old_config[key] = value
            with open(filepath, "w") as output:
                yaml.safe_dump(old_config, output, default_flow_style=False)
        except Exception as e:
            raise SystemException(detail=f"更新系统设置失败, {e}")
