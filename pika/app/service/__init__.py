# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from fastapi import Depends

from app.core.handler.exceres import AccessException
from app.crud.rbac.user import UserDao
from app.schema.user import OAuth2TokenSchema

FORBIDDEN = "对不起, 你没有足够的权限"


class Permission:
    def __init__(self, identity: int = 0, escarole=False):
        self.identity = identity
        self.escarole = escarole

    async def __call__(self, request: OAuth2TokenSchema = Depends()):
        user_info = await UserDao.verify_token(request)
        if self.identity is None or int(user_info.get("identity", 0)) >= self.identity:
            return (user_info["emp_no"], user_info["identity"]) if self.escarole else user_info
        else:
            raise AccessException(detail=FORBIDDEN)
