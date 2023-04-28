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
from app.core.constructor.constructor import ConstructorAbstract
from app.core.handler.jsonres import PikaJsonEncoder
from app.crud.itstem.rdconfig import PikaRedisConfigDao
from app.models.constructor import ConstructorModel


class RedisConstructor(ConstructorAbstract, PikaJsonEncoder):

    @classmethod
    async def run(cls, executor, env, index, path, params, constructor: ConstructorModel, **kwargs):
        try:
            constructor_type_ = cls.get_name(constructor)
            executor.append(
                f"当前路径: {path}, 第{index + 1}条{constructor_type_}")
            data = cls.safe_json_loads(constructor.constructor_json)
            redis = data.get("redis")
            command = data.get("command")
            executor.append(f"当前{constructor_type_}类型为redis, 名称: {redis}\n命令: {command}\n")
            command_result = await PikaRedisConfigDao.execute_command(command=command, name=redis,env=env)
            params[constructor.value] = command_result
            executor.append(f"当前{constructor_type_}返回变量: {constructor.value}\n返回值:\n {command_result}\n")
        except Exception as e:
            raise Exception(f"{path}->{constructor.name} 第{index + 1}个{constructor_type_}执行失败: {e}")
