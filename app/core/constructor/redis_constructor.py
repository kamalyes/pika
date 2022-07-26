# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  redis_constructor.py
@Time    :  2022/6/10 6:53 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import json

from app.core.constructor.constructor import ConstructorAbstract
from app.crud.online.rdconfig import PikaRedisConfigDao
from app.models.constructor import ConstructorModel


class RedisConstructor(ConstructorAbstract):

    @staticmethod
    async def run(executor, env, index, path, params, req_params, constructor: ConstructorModel,
                  **kwargs):
        try:
            executor.append(
                f"当前路径: {path}, 第{index + 1}条{ConstructorAbstract.get_name(constructor)}")
            data = json.loads(constructor.constructor_json)
            redis = data.get("redis")
            command = data.get("command")
            executor.append(
                f"当前{ConstructorAbstract.get_name(constructor)}类型为redis, 名称: {redis}\n命令: {command}\n")
            command_result = await PikaRedisConfigDao.execute_command(command=command, name=redis,
                                                                      env=env)
            params[constructor.value] = command_result
            executor.append(
                f"当前{ConstructorAbstract.get_name(constructor)}返回变量: {constructor.value}\n返回值:\n {command_result}\n")
        except Exception as e:
            raise Exception(
                f"{path}->{constructor.name} 第{index + 1}个{ConstructorAbstract.get_name(constructor)}执行失败: {e}")
