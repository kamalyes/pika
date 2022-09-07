# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  rdconfig.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.crud import PikaWrapper, PikaMdWrapper
from app.middleware.xredis import RedisHelper, PikaRedisManager
from app.models.redis_config import RedisModel


@PikaMdWrapper(RedisModel)
class PikaRedisConfigDao(PikaWrapper):

    @classmethod
    async def execute_command(cls, command: str, **kwargs):
        try:
            redis_config = await PikaRedisConfigDao.query_record(**kwargs)
            if redis_config is None:
                raise Exception("Redis配置不存在")
            if not redis_config.cluster:
                client = PikaRedisManager.get_single_node_client(redis_config.id, redis_config.addr,
                                                                 redis_config.password,
                                                                 redis_config.db)
            else:
                client = PikaRedisManager.get_cluster_client(redis_config.id, redis_config.addr)
            return await RedisHelper.execute_command(client, command)
        except Exception as e:
            raise Exception(f"执行redis命令出错: {e}")
