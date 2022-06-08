# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  email.py
@Time    :  2022/5/3 2:15 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Any

from hutools.core import MockHelper
from hutools.time import Moment

from app.core.handler.jsonres import PikaResponse
from app.core.handler.logger import Log
from app.core.notice.email import EmailHande
from app.enums.dimkey import RedisKeyEnum
from app.enums.sysvar import ValidTimeEnum, GlobalVarEnum
from app.models import async_redis


class Email(object):
    log = Log("Email")

    @staticmethod
    async def send_verify_code(request: Any, addressee, app_name=GlobalVarEnum.APP_NAME):
        auth_code_ = MockHelper.rand_sample(length=6)
        redis_now_time = async_redis.time()[0]
        auth_code_valid_time = ValidTimeEnum.AUTH_CODE_VALID_TIME
        valid_time = redis_now_time + auth_code_valid_time
        auth_verify_code = f"{RedisKeyEnum.AUTH_VERIFY_CODE}:{request.emp_no}"
        async_redis.set(auth_verify_code, auth_code_, auth_code_valid_time)
        try:  # 若发送邮件异常则回收对应验证码
            EmailHande.send_email(
                content=EmailHande.get_security_code_template(
                    request.user_desig,
                    request.emp_no,
                    auth_code_,
                    Moment.timestamp_to_date(valid_time),
                    Moment.timestamp_to_date(redis_now_time),
                ),
                subject=f"{app_name}-获取验证码成功通知",
                addressee=[addressee],
            )
        except Exception as e:
            async_redis.delele(auth_verify_code)
            raise e
        else:
            return PikaResponse.success(message=f'已成功发送验证码至邮箱，请查收')
