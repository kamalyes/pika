# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  user.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import Optional, List

from fastapi import Body, Header
from fastapi.params import Form
from pydantic import BaseModel

from app.enums.bytesize import ByteSizeEnum
from app.enums.gebruikersrol import RoleEnum
from app.schema.base import PikaQueryModel, PikaQueryTypeModel


class OAuth2TokenModel:
    """Token鉴权"""

    def __init__(
            self,
            emp_no: str = Header(None, title="用户编码", max_length=ByteSizeEnum.LENGTH_16),
            x_token: str = Header(None, title="x_token", max_length=ByteSizeEnum.LENGTH_600),
    ):
        self.emp_no = emp_no
        self.x_token = x_token


class RegisterModel(BaseModel):
    """用户注册"""
    username: Optional[str] = Body(
        ...,
        title="用户名",
        min_length=ByteSizeEnum.LENGTH_06,
        max_length=ByteSizeEnum.LENGTH_20,
    )
    email: Optional[str] = Body(..., title="邮箱地址", max_length=ByteSizeEnum.LENGTH_255)
    password: Optional[str] = Body(
        None,
        title="登录密码",
        min_length=ByteSizeEnum.LENGTH_06,
        max_length=ByteSizeEnum.LENGTH_255,
    )
    user_alias: Optional[str] = Body(
        None,
        title="用户花名",
        min_length=ByteSizeEnum.LENGTH_06,
        max_length=ByteSizeEnum.LENGTH_20,
    )
    mobile: Optional[str] = Body(None, title="手机号码", max_length=ByteSizeEnum.LENGTH_11)
    plane: Optional[str] = Body(None, title="座机", max_length=ByteSizeEnum.LENGTH_20)
    avatar: Optional[str] = Body(None, title="头像", max_length=ByteSizeEnum.LENGTH_255)
    gender: Optional[int] = Body(None, title="性别")
    city_name: Optional[str] = Body(None, title="所在城市", max_length=ByteSizeEnum.LENGTH_255)
    identity: Optional[str] = Body(RoleEnum.ORDINARY.value, title="用户身份", max_length=ByteSizeEnum.LENGTH_255)


class AddUserModel(RegisterModel):
    """添加用户"""
    pass


class OAuth2LoginModel:
    """用户登录"""

    def __init__(
            self,
            dynamic_code: Optional[str] = Form(..., title="动态码", max_length=ByteSizeEnum.LENGTH_06),
            grant_type: str = Form("localhost", title="授权方式", max_length=ByteSizeEnum.LENGTH_255),
            username: str = Form(None, title="用户名", max_length=ByteSizeEnum.LENGTH_20),
            emp_no: str = Form(None, title="用户编码", max_length=ByteSizeEnum.LENGTH_16),
            email: str = Form(None, title="邮箱", max_length=ByteSizeEnum.LENGTH_255),
            password: str = Form(None, title="密码", max_length=ByteSizeEnum.LENGTH_255),
            private_key: str = Form(None, title="私钥", max_length=ByteSizeEnum.LENGTH_255),
    ):
        self.grant_type = grant_type
        self.emp_no = emp_no
        self.username = username
        self.email = email
        self.password = password
        self.private_key = private_key
        self.dynamic_code = dynamic_code


class ModifyUserInfoModel(RegisterModel):
    pass


class QueryUserInModel(PikaQueryModel, PikaQueryTypeModel):
    username: Optional[str] = Body(None, title="用户名")
    user_alias: Optional[str] = Body(None, title="用户花名")
    emp_no: str = Form(None, title="用户编码")
    email: Optional[str] = Body(None, title="邮箱地址")
    mobile: Optional[str] = Body(None, title="手机号码")
    identity: Optional[str] = Body(None, title="用户身份")

    class Config:
        orm_mode = True


class QueryUserOutModel(PikaQueryModel):
    username: Optional[str] = Body(None, title="用户名")
    user_alias: Optional[str] = Body(None, title="用户花名")
    emp_no: str = Form(None, title="用户编码")
    email: Optional[str] = Body(None, title="邮箱地址")
    mobile: Optional[str] = Body(None, title="手机号码")
    identity: Optional[str] = Body(None, title="用户身份")

    class Config:
        orm_mode = True


class SendAuthCodeModel:
    def __init__(self, dynamic_code: Optional[str] = Form(None, title="动态验证码", max_length=ByteSizeEnum.LENGTH_06)):
        self.dynamic_code = dynamic_code


class ItemSecurityModel(BaseModel):
    security_id: Optional[str] = Body(..., title="密保序号", max_length=ByteSizeEnum.LENGTH_255)
    question: Optional[str] = Body(None, title="密保问题", max_length=ByteSizeEnum.LENGTH_255)
    answers: Optional[str] = Body(
        ...,
        title="密保答案",
        min_length=ByteSizeEnum.LENGTH_06,
        max_length=ByteSizeEnum.LENGTH_255,
    )

    class Config:
        orm_mode = True


class EditSecurityModel:
    def __init__(self, security: List[ItemSecurityModel] = Body(None, title="密保信息")):
        self.security = security


class DelSecurityModel:
    def __init__(self, security_id: Optional[list] = Form(..., title="密保序号")):
        self.security_id = security_id


class ForgetPwdModel(BaseModel):
    alter_type: Optional[str] = Body("verifycode", title="验证方式：（verifycode：邮箱验证码, security：密保）")
    verify_code: Optional[str] = Body(None, title="验证码", max_length=ByteSizeEnum.LENGTH_06)
    security: List[ItemSecurityModel] = Body(None, title="密保信息")
    new_password: Optional[str] = Body(..., title="新密码", max_length=ByteSizeEnum.LENGTH_255)

    class Config:
        orm_mode = True


class ModifyPwdModel(BaseModel):
    alter_type: Optional[str] = Body("pwd", title="操作类型：（pwd：修改密码, private_key：修改private_key）")
    old_password: Optional[str] = Body(None, title="旧密码", max_length=ByteSizeEnum.LENGTH_255)
    new_password: Optional[str] = Body(None, title="新密码", max_length=ByteSizeEnum.LENGTH_255)

    class Config:
        orm_mode = True
