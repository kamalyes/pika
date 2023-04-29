# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
# noinspection PyPep8Naming
from app.service.itstem.database import router as dbconfig_router
from app.service.itstem.environment import router as environment_router
from app.service.itstem.gateway import router as gateway_router
from app.service.itstem.gconfig import router as gconfig_router
from app.service.itstem.redis_config import router as redis_config_router
