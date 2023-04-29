# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  notice
@Time    :  2022/6/17 12:58 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import List

from fastapi import APIRouter, Depends

from app.core.handler.jsonres import PikaResponse
from app.crud.system.broadcast import BroadcastReadDao
from app.crud.system.notification import PikaNotificationDao
from app.enums.MessageEnum import MessageStateEnum
from app.models import async_db_session_iterator
from app.models.broadcast import BroadcastReadUserModel
from app.models.notification import NotificationModel
from app.schema.notification import NotificationSchema
from app.service import Permission

router = APIRouter()


@router.get("/list", summary="获取用户消息列表")
async def list_msg(msg_status: int, msg_type: int, user_info=Depends(Permission())):
    try:
        data = await PikaNotificationDao.list_messages(
            msg_type=msg_type,
            msg_status=msg_status,
            receiver=user_info["emp_no"],
        )
        return PikaResponse.success(data=data)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/read", summary="用户读取消息")
async def read_msg(form: NotificationSchema, user_info=Depends(Permission())):
    try:
        if form.personal:
            await PikaNotificationDao.update_by_map(
                user_info["emp_no"],
                NotificationModel.id.in_(form.personal),
                NotificationModel.receiver == user_info["emp_no"],
                msg_status=MessageStateEnum.read.value,
            )
        if form.broadcast:
            operator = user_info["emp_no"]
            for f in form.broadcast:
                model = BroadcastReadUserModel(f, operator)
                await BroadcastReadDao.insert(model=model)
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/delete", summary="用户删除消息")
async def delete_msg(msg_id: List[str], user_info=Depends(Permission()), session=Depends(async_db_session_iterator)):
    try:
        await PikaNotificationDao.delete_message(session, msg_id, user_info["emp_no"])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
