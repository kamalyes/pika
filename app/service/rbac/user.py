# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  user.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  用户表
"""
from typing import Any

from fastapi import APIRouter, Request, Depends
from hutools.pagination import LimitOffsetPage, add_pagination
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.handler.execres import ValidException
from app.core.handler.jsonres import PikaResponse
from app.crud.rbac.user import UserDao
from app.enums.RbacEnum import RoleEnum
from app.models import async_db_session_iterator
from app.schema.user import RegisterUserSchema, OAuth2LoginSchema, \
    ForgetPwdSchema, OAuth2TokenSchema, AddUserSchema, \
    ModifyUserInfoSchema, QueryUserInSchema, QueryUserOutSchema, \
    GetVerifyCodeSchema, ModifySecretSchema, EditSecuritySchema, \
    DelSecuritySchema, QuerySecuritySchema, EmailVerifyCodeSchema
from app.service import Permission

router = APIRouter()


@router.post("/register", summary="普通用户注册")
async def register(request: Request, register_model: RegisterUserSchema):
    return await UserDao.register_user(request, register_model)


@router.post("/login/", summary="（编号、用户名）及密码登录", include_in_schema=True)
async def login(request: Request, oauth2_login: OAuth2LoginSchema = Depends()):
    if oauth2_login.grant_type == "account":
        return await UserDao.account_login(request, oauth2_login)
    elif oauth2_login.grant_type == "email":
        return await UserDao.email_login(request, oauth2_login)
    else:
        raise ValidException(detail="暂不支持该model！")


@router.post("/verifytoken", summary="验证Token（用于刷新时使用）")
async def login(request: OAuth2TokenSchema = Depends()):
    user_info = await UserDao.verify_token(request)
    return PikaResponse.success(message="Authentication success",
                                data={**user_info, **{"token": request.token}})


@router.delete("/logout", summary="注销/退出登录")
async def logout(request: Request, oauth2_logout: OAuth2TokenSchema = Depends()):
    return await UserDao.account_logout(request, oauth2_logout)


@router.post("/add", dependencies=[], name="添加用户 （管理员操作）")
async def create_user(request: AddUserSchema,
                      user_info=Depends(Permission(RoleEnum.MANAGER.value))):
    return await UserDao.add_user(request, user_info)


@router.post("/info/update", summary="用户更新自己相关资料")
async def update_user_info(modify_user_info: ModifyUserInfoSchema,
                           user_info=Depends(Permission())):
    return await UserDao.update_user_info(modify_user_info, user_info)


@router.get("/alluser", summary="查询所有用户信息")
async def query_all_users(user_info=Depends(Permission())):
    try:
        query_users = await UserDao.query_all_users()
        return PikaResponse.success(data=query_users, exclude=("password",))
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/list", summary="查询用户列表", response_model=LimitOffsetPage[QueryUserOutSchema])
async def query_user_list(request: QueryUserInSchema = Depends(),
                          user_info=Depends(Permission(RoleEnum.ADMIN.value)),
                          db: AsyncSession = Depends(async_db_session_iterator)) -> Any:
    return await UserDao.query_user_info_list(db, request)


@router.get("/personal/detail", summary="获取用户个人资料详细")
async def query_user_details(user_info=Depends(Permission())):
    return user_info


@router.get("/auth/qrcode", summary="获取动态验证码")
async def get_dynamic_code(request: Request):
    return await UserDao.rand_dynamic_code(request)


@router.post("/auth/elcode", summary="获取邮箱验证码")
async def send_email_verify_code(request: EmailVerifyCodeSchema):
    return await UserDao.send_email_verify_code(request)


@router.post("/auth/verifycode", summary="发送验证码-邮件")
async def send_verify_code(request: GetVerifyCodeSchema, user_info=Depends(Permission())):
    return await UserDao.get_verifycode(request, user_info)


@router.post("/pwd/forget", summary="忘记密码？通过（邮箱验证码/密保）重置密码")
async def forget_pwd(request: ForgetPwdSchema = Depends(), user_info=Depends(Permission())):
    alter_type_list = [1, 2]
    if request.alter_type == alter_type_list[0]:
        await UserDao.has_mail_verify_code(verify_code=request.verify_code)
        await UserDao.update_pwd(new_password=request.new_password, emp_no=user_info["emp_no"])
    elif request.alter_type == alter_type_list[1]:
        await UserDao.update_pwd(new_password=request.new_password, emp_no=user_info["emp_no"])
    elif request.alter_type not in alter_type_list:
        raise ValidException(detail=f"alter_type 仅可传入{alter_type_list}")
    return PikaResponse.success()


@router.post("/pwd/update", summary="通过旧密码去更新密码")
async def update_pwd(request: ModifySecretSchema = Depends(), user_info=Depends(Permission())):
    await UserDao.old_value_update_pwd(emp_no=user_info["emp_no"],
                                       old_password=request.old_password,
                                       new_password=request.new_password)
    return PikaResponse.success()


@router.post("/security/add", summary="添加密保信息")
async def add_security(request: EditSecuritySchema = Depends(), user_info=Depends(Permission())):
    return await UserDao.add_security(request=request, user_info=user_info)


@router.delete("/security/empty", summary="清空密保问题（非软删）")
async def delete_security(security_ids: DelSecuritySchema = Depends(),
                          user_info=Depends(Permission())):
    return await UserDao.empty_security(request=security_ids, emp_no=user_info["emp_no"])


@router.post("/security/update", summary="更新密保问题")
async def update_security(request: EditSecuritySchema = Depends(), user_info=Depends(Permission())):
    return await UserDao.update_security(request=request, user_info=user_info)


@router.get("/security/info", summary="查询用户自己设置过的密保信息",
            response_model=LimitOffsetPage[QuerySecuritySchema])
async def query_security(user_info=Depends(Permission()),
                         db: AsyncSession = Depends(async_db_session_iterator)) -> Any:
    return await UserDao.query_security(db=db, emp_no=user_info["emp_no"])


add_pagination(router)
