# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Depends

from app.core.handler.execres import AuthException
from app.crud.rbac.user import UserDao
from app.excpetions.RequestException import PermissionException
from app.models import async_redis
from app.schema.user import OAuth2TokenModel

FORBIDDEN = "对不起, 你没有足够的权限"


class Permission:
    def __init__(self, identity: int = None):
        self.identity = identity

    async def __call__(self, request: OAuth2TokenModel = Depends()):
        try:
            user_info = await UserDao.verify_token(request)
            if self.identity is None:
                return user_info
            elif int(user_info.get('identity', 0)) >= self.identity:
                return user_info
            else:
                raise AuthException(detail=FORBIDDEN)
        except PermissionException as e:
            raise e
