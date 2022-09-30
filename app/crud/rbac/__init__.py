# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/5/3 2:15 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from custard.core import RegEx

from app.core.handler.execres import ValidException
from app.enums.SysCodeEnum import ExcCodeEnum


async def regex_register_str(email, gender=None, mobile=None):
    """
    正则匹配User对象
    Args:
        email:
        gender:
        mobile:
    Returns:
    Example::
        >>> print(regex_register_str(mobile=None, email=None, gender=None))
        >>> print(regex_register_str(mobile=None, email="mryu168@163.com", gender=0))
        >>> print(regex_register_str(mobile=18175699611, email="5678888.com", gender=0))
        >>> print(regex_register_str(mobile=18175699611, email=None, gender=0))
        >>> print(regex_register_str(mobile=18175699611, email="mryu168@163.com", gender=None))
        >>> print(regex_register_str(mobile=18175699611, email="mryu168@163.com", gender=1))
        >>> print(regex_register_str(mobile=18175699611, email="mryu168@163.com", gender=0))
    """
    if email is None:
        raise ValidException(code=ExcCodeEnum.VAR_ERROR, detail=f"邮箱地址不能为空")
    elif RegEx.match_email(email) is False:
        raise ValidException(code=ExcCodeEnum.FIELD_TYPE_ERROR, detail="邮箱格式不正确")
    if mobile is not None and RegEx.match_mobile(mobile) is False:
        raise ValidException(code=ExcCodeEnum.FIELD_TYPE_ERROR, detail="手机号格式不正确！")
    if gender is not None and (not isinstance(gender, int) or gender not in (0, 1, 2)):
        raise ValidException(code=ExcCodeEnum.FIELD_TYPE_ERROR, detail="性别字段仅可传：0-未填写，1-男，2-女")


async def client_ip(request):
    try:
        forwarded = request.headers.get("X-Forwarded-For")
        return forwarded.split(",")[0] if forwarded else request.client.host
    except Exception as e:
        return None
