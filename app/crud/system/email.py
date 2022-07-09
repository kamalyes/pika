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
from typing import List

from hutools.core import MockHelper
from hutools.time import Moment

from app.core.handler.execres import ValidException
from app.core.handler.logger import PikaLogger
from app.core.notice.email import EmailManger
from app.enums.RedisEnum import RedisKeyEnum
from app.enums.SysvarEnum import ValidTimeEnum, PikaGlobalVarEnum
from app.models import async_redis


class Email(object):
    log = PikaLogger("Email")

    @staticmethod
    async def register_succeed(emp_no: str, username: str, addressee: List, pwd_valid_date,
                               app_name=PikaGlobalVarEnum.APP_NAME):
        """

        Args:
            emp_no:
            username:
            addressee:
            pwd_valid_date:
            app_name:

        Returns:

        """
        redis_now_time = await async_redis.time()
        try:  # 若发送邮件异常则回收对应验证码
            return EmailManger.send_email(
                content=EmailManger.register_succeed_template(
                    username,
                    emp_no,
                    addressee,
                    pwd_valid_date,
                    Moment.timestamp_to_date(list(redis_now_time)[0]),
                ),
                subject=f"{app_name}-注册成功通知",
                addressee=addressee
            )
        except Exception as e:
            raise e

    @staticmethod
    async def rand_mail_code(emp_no: str = None, username: str = None, addressee: List = None,
                             app_name=PikaGlobalVarEnum.APP_NAME, model=1):
        auth_code_ = MockHelper.rand_sample(length=6)
        redis_now_time = await async_redis.time()
        auth_code_valid_time = ValidTimeEnum.AUTH_CODE_VALID_TIME
        valid_time = list(redis_now_time)[0] + auth_code_valid_time
        if model == 1:
            auth_verify_code = f"{RedisKeyEnum.FORGET_PWD_VERIFYCODE}:{emp_no}"
        elif model == 2:
            auth_verify_code = f"{RedisKeyEnum.LOGIN_VERIFYCODE}:{emp_no}"
        elif model == 3:
            auth_verify_code = f"{RedisKeyEnum.REGISTER_VERIFYCODE}:{addressee}"
        else:
            raise ValidException(detail="暂不支持该model！")
        await async_redis.set(auth_verify_code, auth_code_, int(auth_code_valid_time))
        try:  # 若发送邮件异常则回收对应验证码
            if model in (1, 2):
                return EmailManger.send_email(
                    content=EmailManger.get_security_code_template(
                        username,
                        emp_no,
                        auth_code_,
                        Moment.timestamp_to_date(valid_time),
                        Moment.timestamp_to_date(int(valid_time - auth_code_valid_time)),
                    ),
                    subject=f"{app_name}-获取验证码成功通知",
                    addressee=addressee
                )
            elif model == 3:
                return EmailManger.send_email(
                    content=EmailManger.get_reg_code_template(
                        addressee,
                        auth_code_,
                        Moment.timestamp_to_date(valid_time),
                        Moment.timestamp_to_date(int(valid_time - auth_code_valid_time)),
                    ),
                    subject=f"{app_name}-注册验证码通知",
                    addressee=addressee
                )
        except Exception as e:
            await async_redis.delete(auth_verify_code)
            raise e
