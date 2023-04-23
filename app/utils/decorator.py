# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  decorator
@Time    :  2022/6/18 7:06 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import asyncio
import functools
import os
from functools import wraps
from redlock import RedLock, RedLockError

from config import PikaAppConfig


class SingletonDecorator:
    """单例装饰器"""
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


def case_log(func):
    """_summary_
    Args:
        func (_type_): _description_
    Returns:
        _type_: _description_
    """
    @wraps(func)
    async def wrapper(*args, **kw):
        self = args[0]
        doc = func.__doc__
        func_info = doc.strip() if doc else func.__name__
        print("asyncio.iscoroutinefunction",asyncio.iscoroutine(func), asyncio.iscoroutinefunction(func), func_info)
        self.logger.append(content=get_str(args, kw), func_info=func_info)
        if asyncio.iscoroutinefunction(func):
            returns = await func(*args, **kw)
        else:
            returns = func(*args, **kw)
        self.logger.append(content=get_returns(returns), func_info=func_info, end=True)
        return returns
    return wrapper


def get_str(args, kwargs):
    """_summary_

    Args:
        args (_type_): _description_
        kwargs (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = []
    # 这里从1索引开始,是因为args[0]是self, 也就注定了case_log只能在Executor方法下使用
    for i, a in enumerate(args[1:], start=1):
        if callable(a):
            result.append(a.__doc__ if a.__doc__ else a.__name__)
        else:
            result.append(f"\n参数{i}:\n{str(a)}")
    if kwargs:
        for k, v in kwargs:
            result.append(f"\n{k}->{v}")
    if len(result) == 0:
        return "无"
    return ", ".join(result)


def get_returns(obj):
    """_summary_

    Args:
        obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not obj:
        return ""
    if callable(obj):
        return obj.__doc__ if obj.__doc__ else obj.__name__
    if isinstance(obj, object):
        return str(obj)
    return f"返回值: {obj}"


def lock(key):
    """
    redis分布式锁,基于redlock
    Args:
        key: 唯一key,确保所有任务一致,但不与其他任务冲突

    Returns:

    """

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                with RedLock(f"distributed_lock:{func.__name__}:{key}:{str(args)}",
                             connection_details=PikaAppConfig.REDIS_NODES,
                             ttl=30000,  # 锁释放时间为30s
                             ):
                    return await func(*args, **kwargs)
            except RedLockError:
                print(f"进程: {os.getpid()}获取任务失败, 不用担心,还有其他哥们给你执行了")

        return wrapper

    return decorator
