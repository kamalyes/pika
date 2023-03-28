# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  xredis.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  redis客户端Manager
"""

import asyncio
import functools
import inspect
import pickle
from random import Random
from typing import Any, Tuple

from awaits.awaitable import awaitable
from config import PikaAppConfig

# noinspection PyPackageRequirements
from custard.rediscluster import ClusterConnectionPool, RedisCluster
from loguru import logger
from redis import ConnectionPool, StrictRedis

from app.core.handler.jsonres import PikaJsonEncoder
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.exceptions import RedisError


class PikaRedisManager(PikaJsonEncoder):
    """非线程安全,可能存在问题"""

    _cluster_pool = {}
    _pool = {}

    @property
    def client(cls):
        pool = ConnectionPool(
            host=PikaAppConfig.REDIS_HOST,
            port=PikaAppConfig.REDIS_PORT,
            db=PikaAppConfig.REDIS_DB_INDEX,
            max_connections=PikaAppConfig.REDIS_MAX_CONNECTIONS,
            password=PikaAppConfig.REDIS_PASSWORD,
            encoding=PikaAppConfig.REDIS_ENCODING,
            decode_responses=PikaAppConfig.REDIS_DECODE_RESPONSES,
        )
        return StrictRedis(connection_pool=pool, decode_responses=PikaAppConfig.REDIS_DECODE_RESPONSES)

    @classmethod
    def get_redis_nodes(cls, nodes_str: str):
        startup_nodes = []
        nodes = nodes_str.split(",") if "," in nodes_str else [nodes_str]
        if len(nodes) > 0:
            for node in nodes:
                host, port = node.split(":")
                try:
                    port = port if isinstance(port, int) else int(port)
                except ValueError as ve:
                    raise Exception(f"redis端口强转失败{ve}")
                startup_nodes.append({"host": host, "port": port})
        return startup_nodes

    @classmethod
    def delete_client(cls, redis_id: str, cluster: bool):
        """
        根据redis_id和是否是集群删除客户端
        Args:
            redis_id:
            cluster:

        Returns:

        """
        if cluster:
            cls._cluster_pool.pop(redis_id)
        else:
            cls._pool.pop(redis_id)

    @classmethod
    def get_cluster_client(cls, redis_id: str, address: str, password: str):
        """
        获取redis集群客户端
        Args:
            redis_id:
            address:
            password:

        Returns:

        """
        cluster = cls._cluster_pool.get(redis_id)
        if cluster is not None:
            return cluster
        client = cls.get_cluster(address, password)
        cls._cluster_pool[redis_id] = client
        return client

    @classmethod
    def get_single_node_client(cls, redis_id: str, address: str, password: str, db: int):
        """
        获取redis单实例客户端
        Args:
            redis_id:
            address:
            password:
            db:

        Returns:

        """
        node = cls._pool.get(redis_id)
        if node is not None:
            return node
        if ":" not in address:
            raise RedisError("redis连接未包含端口号,请检查配置")
        host, port = address.split(":")
        pool = ConnectionPool(
            host=host,
            port=port,
            db=db,
            password=password,
            max_connections=PikaAppConfig.REDIS_MAX_CONNECTIONS,
            decode_responses=PikaAppConfig.REDIS_DECODE_RESPONSES,
        )
        client = StrictRedis(connection_pool=pool)
        cls._pool[redis_id] = client
        return client

    @classmethod
    def refresh_redis_client(cls, redis_id: str, address: str, password: str, db: str):
        """
        刷新redis客户端
        Args:
            redis_id:
            address:
            password:
            db:

        Returns:

        """
        host, port = address.split(":")
        pool = ConnectionPool(
            host=host,
            port=port,
            db=db,
            password=password,
            max_connections=PikaAppConfig.REDIS_MAX_CONNECTIONS,
            decode_responses=PikaAppConfig.REDIS_DECODE_RESPONSES,
        )
        client = StrictRedis(connection_pool=pool, decode_responses=PikaAppConfig.REDIS_DECODE_RESPONSES)
        cls._pool[redis_id] = client

    @classmethod
    def refresh_redis_cluster(cls, redis_id: str, addr: str, password: str):
        cls._cluster_pool[redis_id] = cls.get_cluster(addr, password)

    @classmethod
    def get_cluster(cls, address: str, password: str):
        """
        获取集群连接池
        Args:
            address:
            password:

        Returns:

        """
        startup_nodes = cls.get_redis_nodes(address)
        if len(startup_nodes) == 0:
            raise RedisError("找不到集群节点,请检查配置")
        pool = ClusterConnectionPool(
            startup_nodes=startup_nodes,
            max_connections=PikaAppConfig.REDIS_MAX_CONNECTIONS,
            decode_responses=PikaAppConfig.REDIS_DECODE_RESPONSES,
        )
        client = RedisCluster(connection_pool=pool, password=password)
        return client


class RedisHelper(PikaJsonEncoder):
    prefix = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}"
    cluster_nodes = PikaAppConfig.REDIS_CLUSTER_NODE
    password = PikaAppConfig.REDIS_PASSWORD
    if cluster_nodes is not None:
        pika_redis_client = PikaRedisManager.get_cluster(cluster_nodes, password)
    else:
        pika_redis_client = PikaRedisManager().client

    @classmethod
    @awaitable
    def execute_command(cls, client, command, *args, **kwargs):
        return client.execute_command(command, *args, **kwargs)

    @classmethod
    @awaitable
    def ping(cls):
        """
        test redis client
        :return:
        """
        return cls.pika_redis_client.ping()

    @classmethod
    @awaitable
    def get_address_record(cls, address: str):
        """
        获取ip是否已经开启录制
        Args:
            address:

        Returns:

        """
        key = cls.get_key(f"record:ip:{address}")
        return cls.pika_redis_client.get(key)

    @classmethod
    @awaitable
    def cache_record(cls, address: str, request):
        """

        Args:
            address:
            request:

        Returns:

        """
        key = cls.get_key(f"record:{address}:requests")
        cls.pika_redis_client.rpush(key, request)
        ttl = cls.pika_redis_client.ttl(key)
        if ttl < 0:
            cls.pika_redis_client.expire(key, 3600)

    @classmethod
    @awaitable
    def set_address_record(cls, operator: str, address: str, regex: str, retain_history=False):
        """
        设置录制状态
        Args:
            operator:    操作者员工编号
            address:
            regex: 录制的url正则
            retain_history: 保留历史记录

        Returns:

        """
        # 默认录制1小时
        value = cls.safe_json_dumps({"operator": operator, "regex": regex}, ensure_ascii=False)
        cls.pika_redis_client.set(cls.get_key(f"record:ip:{address}"), value, ex=3600)
        # 清楚上次录制数据
        cls.pika_redis_client.delete(cls.get_key(f"record:{address}:requests"))

    @classmethod
    @awaitable
    def remove_record_data(cls, address: str, index: int):
        """
        删除录制数据
        Args:
            address:
            index:

        Returns:

        """
        key = cls.get_key(f"record:{address}:requests")
        cls.pika_redis_client.lset(key, index, "DELETED")
        cls.pika_redis_client.lrem(key, 1, "DELETED")

    @classmethod
    @awaitable
    def remove_address_record(cls, address: str):
        """
        停止录制任务
        Args:
            address:

        Returns:

        """
        return cls.pika_redis_client.delete(cls.get_key(f"record:ip:{address}"))

    @classmethod
    @awaitable
    def list_record_data(cls, address: str):
        """
        查询录制任务
        Args:
            address:

        Returns:

        """
        key = cls.get_key(f"record:{address}:requests")
        data = cls.pika_redis_client.lrange(key, 0, -1)
        return [cls.safe_json_loads(x) for x in data]

    @classmethod
    @awaitable
    def async_delete_prefix(cls, key: str, traverse_del_num=99):
        """
        根据前缀删除数据
        Args:
            key:
            traverse_del_num:
        Returns:
        """
        while cls.pika_redis_client.zcard(key) > 0:
            # 判断集合中是否有元素,如有有则删除排行0-99的元素
            cls.pika_redis_client.zremrangebyrank(key, 0, traverse_del_num)
            logger.bind(name=None).info(f"delete redis key: {key}")

    @classmethod
    def delete_prefix(cls, key: str):
        """
        根据前缀删除数据
        Args:
            key:

        Returns:

        """
        for k in cls.pika_redis_client.scan_iter(f"{key}:*"):
            cls.pika_redis_client.delete(k)
            logger.bind(name=None).info(f"delete redis key: {k}")

    @classmethod
    def get_key(cls, _redis_key: str, args_key: bool = True, *args, **kwargs):
        if not args_key:
            return f"{cls.prefix}:{_redis_key}"
        filter_keys = ("<class", "<sqlalchemy", "(<sqlalchemy")
        filter_args = [key for key in args if not str(key).startswith(filter_keys)]
        for v in kwargs.values():
            if v and not str(v).startswith(filter_keys):
                filter_args.append(str(v))
        return (
            f"{cls.prefix}:{_redis_key}"
            f"{':' + ':'.join(str(a) for a in filter_args) if len(filter_args) > 0 else ''}"
        )

    @classmethod
    def get_key_with_suffix(cls, cls_name: str, key: str, args: tuple, key_suffix):
        filter_args = [a for a in args if not str(args[0]).startswith("<class")]
        suffix = key_suffix(filter_args)
        return f"{cls.prefix}:{cls_name}:{key}:{suffix}"

    @classmethod
    def cache(cls, key: str, expired_time=30 * 60, args_key=True):
        """
        自动缓存装饰器
        Args:
            key: 被缓存的key
            expired_time: 默认key过期时间
            args_key:

        Returns:

        """

        def decorator(func):
            # 缓存已存在
            if asyncio.iscoroutinefunction(func):

                @functools.wraps(func)
                async def wrapper(*args, **kwargs):
                    if not PikaAppConfig.REDIS_ENABLE_FLAG:
                        return await func(*args, **kwargs)
                    cls_name = inspect.getframeinfo(inspect.currentframe().f_back)[3][0].split(".")[0].split(" ")[-1]
                    redis_key = cls.get_key(f"{cls_name}:{key}", args_key, *args, **kwargs)
                    data = cls.pika_redis_client.get(redis_key)
                    # 缓存已存在
                    if data is not None:
                        return pickle.loads(bytes.fromhex(data))
                    # 获取最新数据
                    new_data = await func(*args, **kwargs)
                    info = pickle.dumps(new_data)
                    logger.bind(name=None).info(f"set redis key: {redis_key}")
                    cls.pika_redis_client.set(redis_key, info.hex(), ex=expired_time)
                    return new_data

                return wrapper
            else:

                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    if not PikaAppConfig.REDIS_ENABLE_FLAG:
                        return func(*args, **kwargs)
                    cls_name = inspect.getframeinfo(inspect.currentframe().f_back)[3][0].split(".")[0].split(" ")[-1]
                    redis_key = cls.get_key(f"{cls_name}:{key}", args_key, *args, **kwargs)
                    data = cls.pika_redis_client.get(redis_key)
                    # 缓存已存在
                    if data is not None:
                        return pickle.loads(bytes.fromhex(data))
                    # 获取最新数据
                    new_data = func(*args, **kwargs)
                    info = pickle.dumps(new_data)
                    logger.bind(name=None).info(f"set redis key: {redis_key}")
                    # 添加随机数防止缓存雪崩
                    cls.pika_redis_client.set(redis_key, info.hex(), ex=expired_time + Random().randint(10, 59))
                    return new_data

                return wrapper

        return decorator

    @classmethod
    def up_cache(cls, *key: str, key_and_suffix: Tuple = None):
        """
        redis缓存key,套了此方法,会自动执行更新数据操作后删除缓存
        Args:
            *key:
            key_and_suffix: 要删除的key和key组成规则

        Returns:

        """

        def decorator(func):
            if asyncio.iscoroutinefunction(func):

                @functools.wraps(func)
                async def wrapper(*args, **kwargs):
                    new_data = await func(*args, **kwargs)
                    if not PikaAppConfig.REDIS_ENABLE_FLAG:
                        return new_data
                    cls_name = inspect.getframeinfo(inspect.currentframe().f_back)[3][0].split(".")[0].split(" ")[-1]
                    for k in key:
                        redis_key = f"{cls.prefix}:{cls_name}:{k}*"
                        await cls.async_delete_prefix(redis_key)
                    if key_and_suffix is not None:
                        current_key = cls.get_key_with_suffix(cls_name, key_and_suffix[0], args, key_and_suffix[1])
                        cls.pika_redis_client.delete(current_key)
                    # 更新数据,删除缓存
                    return new_data

                return wrapper
            else:

                @functools.wraps(func)
                def wrapper(*args, **kwargs) -> Any:
                    new_data = func(*args, **kwargs)
                    if not PikaAppConfig.REDIS_ENABLE_FLAG:
                        return new_data
                    cls_name = inspect.getframeinfo(inspect.currentframe().f_back)[3][0].split(".")[0].split(" ")[-1]
                    for k in key:
                        redis_key = f"{cls.prefix}:{cls_name}:{k}"
                        cls.delete_prefix(redis_key)
                    if key_and_suffix is not None:
                        current_key = cls.get_key_with_suffix(cls_name, key_and_suffix[0], args, key_and_suffix[1])
                        cls.pika_redis_client.delete(current_key)
                    return new_data

                return wrapper

        return decorator
