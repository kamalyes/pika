# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  redis.py
@Time    :  2022/6/20 11:16 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.online.rdconfig import PikaRedisConfigDao
from app.schema.online import OnlineRedisForm

router = APIRouter()


@router.post("/redis/command")
async def test_redis_command(form: OnlineRedisForm):
    try:
        res = await PikaRedisConfigDao.execute_command(form.command, id=form.id)
        return PikaResponse.success(data=res)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
