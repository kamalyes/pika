# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  user.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from typing import Optional, List

from fastapi import Body, Header
from fastapi.params import Form, Query
from pydantic import BaseModel

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.RbacEnum import RoleEnum
from app.schema.base import BaseOnlyEmpNoSchema, BaseOnlyIdSchema, BaseOnlyUserNameSchema, BaseQuerySchema, BaseQueryTypeSchema, BaseBatchDelIdsSchema


class OAuth2TokenSchema:
    """Token鉴权"""
    def __init__(
            self,
            emp_no: Optional[str] = Header(
                None, title="用户编码", max_length=ByteSizeEnum.LENGTH_16),
            token: Optional[str] = Header(
                None, title="token", max_length=ByteSizeEnum.LENGTH_600),
    ):
        self.emp_no = emp_no
        self.token = token


class RegisterUserSchema(BaseModel):
    username: Optional[str] = Body(
        ...,
        title="用户名",
        min_length=ByteSizeEnum.LENGTH_06,
        max_length=ByteSizeEnum.LENGTH_16,
    )
    el_code: Optional[str] = Body(
        None, title="验证码", max_length=ByteSizeEnum.LENGTH_11)
    email: Optional[str] = Body(..., title="邮箱地址",
                                max_length=ByteSizeEnum.LENGTH_255)
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
    mobile: Optional[str] = Body(
        None, title="手机号码", max_length=ByteSizeEnum.LENGTH_11)
    plane: Optional[str] = Body(
        None, title="座机", max_length=ByteSizeEnum.LENGTH_20)
    avatar: Optional[str] = Body(
        None, title="头像", max_length=ByteSizeEnum.LENGTH_255)
    gender: Optional[int] = Body(None, title="性别")
    location: Optional[str] = Body(None, title="所在城市")
    identity: Optional[int] = Body(RoleEnum.ORDINARY.value, title="用户身份")


class AddUserSchema(RegisterUserSchema):
    """添加用户"""
    pass


class OAuth2LoginSchema:
    """用户登录"""

    def __init__(
            self,
            dynamic_code: Optional[str] = Form(None, title="动态码",
                                               max_length=ByteSizeEnum.LENGTH_06),
            grant_type: Optional[str] = Form(..., title="授权方式, account:用户名/员工编号、email:邮箱验证码",
                                             max_length=ByteSizeEnum.LENGTH_255),
            username: Optional[str] = Form(
                None, title="用户名", max_length=ByteSizeEnum.LENGTH_16),
            email: Optional[str] = Form(
                None, title="邮箱地址", max_length=ByteSizeEnum.LENGTH_255),
            password: Optional[str] = Form(
                None, title="密码", max_length=ByteSizeEnum.LENGTH_255),
            private_key: Optional[str] = Form(
                None, title="私钥", max_length=ByteSizeEnum.LENGTH_255),
    ):
        self.grant_type = grant_type
        self.username = username
        self.email = email
        self.password = password
        self.private_key = private_key
        self.dynamic_code = dynamic_code


class ModifyUserInfoSchema(RegisterUserSchema):
    pass


class QueryUserInSchema(BaseOnlyUserNameSchema, BaseOnlyEmpNoSchema, BaseQuerySchema, BaseQueryTypeSchema):
    user_alias: Optional[str] = Query(None, title="用户花名")
    email: Optional[str] = Query(None, title="邮箱地址")
    mobile: Optional[str] = Query(None, title="手机号码")
    # identity: Optional[str] = Query(None, title="用户身份")

    class Config:
        orm_mode = True


class QueryUserOutSchema(BaseOnlyUserNameSchema, BaseOnlyEmpNoSchema, BaseQuerySchema):
    user_alias: Optional[str] = Query(None, title="用户花名")
    email: Optional[str] = Query(None, title="邮箱地址")
    mobile: Optional[str] = Query(None, title="手机号码")
    identity: Optional[int] = Query(None, title="用户身份")

    class Config:
        orm_mode = True


class SendAuthCodeSchema:
    def __init__(self, dynamic_code: Optional[str] = Form(None, title="动态验证码",
                                                          max_length=ByteSizeEnum.LENGTH_06)):
        self.dynamic_code = dynamic_code


class ItemSecuritySchema(BaseOnlyIdSchema):
    question: Optional[str] = Body(
        None, title="密保问题", max_length=ByteSizeEnum.LENGTH_255)
    answers: Optional[str] = Body(
        ...,
        title="密保答案",
        min_length=ByteSizeEnum.LENGTH_06,
        max_length=ByteSizeEnum.LENGTH_255,
    )

    class Config:
        orm_mode = True


class EditSecuritySchema:
    def __init__(self, security: List[ItemSecuritySchema] = Body(None, title="密保信息")):
        self.security = security


class DelSecuritySchema(BaseBatchDelIdsSchema):
    pass


class QuerySecuritySchema(BaseOnlyIdSchema):
    question: Optional[str] = Body(
        None, title="密保问题", max_length=ByteSizeEnum.LENGTH_255)
    answers: Optional[str] = Body(
        ...,
        title="密保答案",
        min_length=ByteSizeEnum.LENGTH_06,
        max_length=ByteSizeEnum.LENGTH_255,
    )

    class Config:
        orm_mode = True


class GetVerifyCodeSchema(BaseModel):
    models: Optional[int] = Body(1, title="模式:（1:忘记密码）")

    class Config:
        orm_mode = True


class EmailVerifyCodeSchema(BaseModel):
    model: Optional[int] = Body(3, title="模型:2:邮箱登录使用,3:用户注册时使用")
    email: Optional[str] = Body(None, title="邮箱地址")

    class Config:
        orm_mode = True


class ForgetPwdSchema(BaseModel):
    alter_type: Optional[int] = Body(1, title="验证方式:（1:邮箱验证码, 2:密保）")
    verify_code: Optional[str] = Body(
        None, title="验证码", max_length=ByteSizeEnum.LENGTH_06)
    security: List[ItemSecuritySchema] = Body(None, title="密保信息")
    new_password: Optional[str] = Body(..., title="新密码",
                                       max_length=ByteSizeEnum.LENGTH_255)

    class Config:
        orm_mode = True


class ModifySecretSchema(BaseModel):
    old_password: Optional[str] = Body(..., title="旧密码",
                                       max_length=ByteSizeEnum.LENGTH_255)
    new_password: Optional[str] = Body(..., title="新密码",
                                       max_length=ByteSizeEnum.LENGTH_255)

    class Config:
        orm_mode = True
