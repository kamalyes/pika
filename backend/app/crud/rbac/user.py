# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  user.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    : 　None
"""
import json
import random
from typing import Any

from hutools.core import MockHelper, Kerberos, DataHand
from hutools.core.factory import fake
from hutools.pagination.async_sqlalchemy import paginate
from hutools.time import Moment
from sqlalchemy import or_, select, func, and_, update

from app.core.handler.execres import AuthException, \
    SystemException, ThirdException, RedisException, RegisterException
from app.core.handler.jsonres import PikaResponse
from app.core.handler.logger import Log
from app.crud.rbac import regex_register_str, client_ip
from app.enums.dimkey import RedisKeyEnum
from app.enums.gebruikersrol import RoleEnum
from app.enums.statuscode import SysFailedCodeEnum
from app.enums.sysvar import GlobalVarEnum, ValidTimeEnum
from app.enums.toast import PromptEnum
from app.models import async_db_session, async_redis
from app.models.admin import UserAdmin
from app.models.user import User
from config import PikaAppConfig


class UserDao(object):
    log = Log("UserDao")

    @staticmethod
    async def exists_users(users: Any, request):
        exists_users = users.scalars().first()
        # 判断用户名或邮箱是否被注册使用
        if exists_users:
            if request.username == exists_users.username:
                raise RegisterException(code=SysFailedCodeEnum.USER_HAS_USED, detail="该用户名已被使用！")
            elif request.email == exists_users.email:
                raise RegisterException(code=SysFailedCodeEnum.EMAIL_HAS_USED, detail="该邮箱账号已被使用！")
        # 注册的时候给密码加盐
        pwd = Kerberos.md5_encode(decode_msg=request.password)
        emp_no = f"{GlobalVarEnum.EMP_NO_START}{MockHelper.rand_verify_code(6, 1)}".upper()
        return emp_no, pwd

    @staticmethod
    async def register_user(request, register_model):
        """
        用户注册
        Args:
            request:
            register_model:
        Returns:
        """
        user_ip = await client_ip(request)
        await regex_register_str(email=register_model.email)
        async with async_db_session() as session:
            async with session.begin():
                users = await session.execute(select(User).where(
                    or_(User.username == register_model.username, User.email == register_model.email)))
                counts = await session.execute(select(func.count(User.id)))
                # 如果用户数量为0 则注册为超管,且激活状态为1
                identity = RoleEnum.ROOT.value if counts.scalars().first() == 0 else RoleEnum.ORDINARY.value
                is_activate = 1 if identity == RoleEnum.ROOT else 0
                emp_no, pwd = await UserDao.exists_users(users=users, request=register_model)
                user = User(emp_no=emp_no, username=register_model.username, identity=identity,
                            email=register_model.email)
                session.add(user)
            await session.refresh(user)
            user_admin = UserAdmin(uid=user.id, emp_no=user.emp_no, is_activate=is_activate, password=pwd,
                                   pwd_valid_time=GlobalVarEnum.PWD_VALID_TIME,
                                   registration_at=Moment.get_now_time("%Y-%m-%d %H:%M:%S"),
                                   registration_ip=user_ip)
            session.add(user_admin)
            return PikaResponse.success(result=user, message=PromptEnum.REGISTER_SUCCEED.value)

    @staticmethod
    async def account_status_verify(**kwargs):
        # 状态
        if kwargs["is_delete"]:
            raise AuthException(code=SysFailedCodeEnum.ACCOUNT_HAS_DELETE, detail="账号已被删除！")
        if kwargs["is_usable"] is False:
            raise AuthException(code=SysFailedCodeEnum.ACCOUNT_HAS_DISENABLED, detail="账号已被禁用！")
        if str(kwargs["is_activate"]) == 0:
            raise AuthException(code=SysFailedCodeEnum.ACCOUNT_HAS_NOT_ACTIVATE, detail="账号未激活！")
        try:
            skew_date = Moment.skew_date(kwargs["pwd_valid_time"], Moment.get_now_time("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            raise SystemException(code=SysFailedCodeEnum.FIELD_TYPE_ERROR, detail=f"密码有效期对比失败！具体错误原因：{e}")
        if skew_date is False:
            raise AuthException(code=SysFailedCodeEnum.PASSWORD_HAS_EXPIRED, detail="密码已过期，请修改后进行登录！")

    @staticmethod
    async def pwd_mistake_limit(**kwargs):
        async with async_db_session() as session:
            async with session.begin():
                err_pwd_counts = await session.execute(
                    select(UserAdmin.err_pwd_count).where(UserAdmin.uid == kwargs["uid"]))
                err_pwd_count = err_pwd_counts.scalars().first()
                if err_pwd_count > ValidTimeEnum.ERR_PWD_COUNT.value:
                    raise AuthException(code=SysFailedCodeEnum.PASSWORD_ERROR_COUNT_OUT,
                                        detail="错误密码次数超出限制，请联系管理员或稍后重试！")
                else:
                    sql = update(UserAdmin).where(UserAdmin.uid == kwargs["uid"]).values(
                        {"err_pwd_count": int(err_pwd_count + 1)})
                    await session.execute(sql)
                    await session.commit()
                    raise AuthException(code=SysFailedCodeEnum.PASSWORD_ERROR, detail="登录密码错误！")

    @staticmethod
    async def generate_uuid_jwt(**kwargs):
        """
        生成jwt+uuid形态的token
        Args:
            **kwargs:
        Returns:
        """
        target_value = {"emp_no": kwargs["emp_no"], "password": kwargs["password"]}
        try:
            uuid4_ = str(fake.uuid4()).upper()
            jwt_encode_result = Kerberos.jwt_encode(secret_key=PikaAppConfig.JWT_SECRET_KEY,
                                                    target_value=target_value,
                                                    seconds=kwargs["valid_time"])
            return f'{jwt_encode_result}.{uuid4_}'.replace("4", str(random.randint(5, 9)))
        except Exception as uuid_jwt_err:
            raise ThirdException(code=SysFailedCodeEnum.JWT_ENCODE_ERROR,
                                 detail=f"加密失败，具体原因{uuid_jwt_err}")

    @staticmethod
    async def uuid_jwt_sync_redis(**kwargs):
        """
        uuid_jwt同步至redis
        Args:
            **kwargs:
        Returns:
        """
        try:
            await async_redis.set(kwargs["key"], kwargs["value"], int((kwargs["ex"])))
        except Exception as redis_err:
            raise RedisException(detail=str(redis_err))

    @staticmethod
    async def user_info_sync_redis(**kwargs):
        """
        user_info同步至redis
        Args:
            **kwargs:
        Returns:
        """
        try:
            await async_redis.hset(kwargs["name"], kwargs["key"], kwargs["value"])
        except Exception as redis_err:
            raise RedisException(detail=str(redis_err))

    @staticmethod
    async def delete_redis_token(**kwargs):
        """
        删除 redis中Token
        Args:
            **kwargs:
        Returns:
        """
        try:
            await async_redis.delete(kwargs["key"])
        except Exception as redis_err:
            raise RedisException(detail=str(redis_err))

    @staticmethod
    async def update_last_login_field(**kwargs):
        uid, emp_no = kwargs.get("uid", None), kwargs.get("emp_no", None)
        async with async_db_session() as session:
            async with session.begin():
                sql = update(UserAdmin).where(
                    or_(UserAdmin.id == uid, UserAdmin.id == emp_no)).values(
                    {"last_login_ip": kwargs["last_login_ip"],
                     "last_login_at": Moment.get_now_time("%Y-%m-%d %H:%M:%S")})
                await session.execute(sql)

    @staticmethod
    async def update_last_logout_field(**kwargs):
        uid, emp_no, last_logout_ip = kwargs.get("uid", None), kwargs.get("emp_no", None), kwargs["last_logout_ip"]
        async with async_db_session() as session:
            async with session.begin():
                sql = update(UserAdmin).where(
                    or_(UserAdmin.id == uid, UserAdmin.emp_no == emp_no)).values(
                    {"last_logout_ip": last_logout_ip,
                     "last_logout_at": Moment.get_now_time("%Y-%m-%d %H:%M:%S")})
                await session.execute(sql)

    @staticmethod
    async def query_user_info(**kwargs):
        uid, emp_no = kwargs.get("uid", None), kwargs.get("emp_no", None)
        async with async_db_session() as session:
            users = await session.execute(select(User).where(or_(User.id == uid, User.emp_no == emp_no)))
            user_admins = await session.execute(
                select(UserAdmin).where(or_(UserAdmin.uid == uid, UserAdmin.emp_no == emp_no)))
            user, user_admin = users.scalars().first(), user_admins.scalars().first()
            if user and user_admin:
                user_infos = DataHand.chain_all([PikaResponse.model_to_dict(user),
                                                 PikaResponse.model_to_dict(user_admin)])
                # 屏蔽字段
                dislodge = ["open_id", "private_key", "open_id", "password", "description", "id"]
                user_infos = {key: val for key, val in user_infos.items() if key not in dislodge}
            else:
                raise AuthException(detail="用户信息不存在！")
        # 更新在线用户信息
        await UserDao.user_info_sync_redis(name=f'{RedisKeyEnum.ONLINE_USER}',
                                           key=user.emp_no,
                                           value=json.dumps(user_infos))
        return user_infos

    @staticmethod
    async def account_login(request, oauth2_login):
        """
        账号登录
        Args:
            request:
            oauth2_login:
        Returns:
        """
        user_ip = await client_ip(request)
        async with async_db_session() as session:
            async with session.begin():
                sql = select(User).where(or_(User.username == oauth2_login.username,
                                             User.emp_no == oauth2_login.emp_no,
                                             User.email == oauth2_login.email))
                users = await session.execute(sql)
                user = users.scalars().first()
                if user:
                    user_admins = await session.execute(
                        select(UserAdmin).where(
                            and_(UserAdmin.password == oauth2_login.password, UserAdmin.uid == user.id)))
                    user_admin = user_admins.scalars().first()
                    if user_admin:
                        await UserDao.account_status_verify(uid=user_admin.uid,
                                                            is_activate=user_admin.is_activate,
                                                            is_delete=user_admin.is_delete,
                                                            is_usable=user_admin.is_usable,
                                                            pwd_valid_time=str(user_admin.pwd_valid_time),
                                                            err_pwd_count=int(user_admin.err_pwd_count))
                    else:
                        await UserDao.pwd_mistake_limit(uid=user.id)
                    old_token = await async_redis.get(f'{RedisKeyEnum.AUTH_TOKEN}:{user_admin.emp_no}')
                    if old_token and PikaAppConfig.JWT_SINGLE_LOGIN:
                        uuid_jwt = old_token
                    else:
                        # 生成uuid_jwt并同步至redis
                        valid_time = ValidTimeEnum.AUTH_VALID_TIME
                        uuid_jwt = await UserDao.generate_uuid_jwt(emp_no=user.emp_no,
                                                                   valid_time=valid_time,
                                                                   password=user_admin.password)
                        await UserDao.uuid_jwt_sync_redis(key=f'{RedisKeyEnum.AUTH_TOKEN}:{user.emp_no}',
                                                          value=uuid_jwt,
                                                          ex=valid_time)
                else:
                    raise AuthException(code=SysFailedCodeEnum.ACCOUNT_NOT_EXISTS,
                                        detail="该用户名不存在，请使用正常的账户登录！")
        await UserDao.update_last_login_field(uid=user.id, last_login_ip=user_ip)
        user_infos = await UserDao.query_user_info(uid=user.id)
        return PikaResponse.success(
            result=DataHand.chain_all([user_infos, {"x_token": uuid_jwt}]),
            message=PromptEnum.LOGIN_SUCCEED.value)

    @staticmethod
    async def account_logout(request, oauth2_logout):
        await UserDao.verify_token(oauth2_logout)
        key_t = f'{RedisKeyEnum.AUTH_TOKEN}:{oauth2_logout.emp_no}'
        last_logout_ip = await client_ip(request)
        await UserDao.delete_redis_token(key=key_t)
        await UserDao.update_last_logout_field(emp_no=oauth2_logout.emp_no, last_logout_ip=last_logout_ip)
        return PikaResponse.success(message="注销登录成功！")

    @staticmethod
    async def verify_token(request):
        """
        验证token
        Args:
            request:
        Returns:
        """
        key_t = f'{RedisKeyEnum.AUTH_TOKEN}:{request.emp_no}'
        exists_token = await async_redis.get(key_t)
        if exists_token == request.x_token:
            user_infos = await UserDao.query_user_info(emp_no=request.emp_no)
            try:
                await UserDao.account_status_verify(uid=user_infos["uid"],
                                                    is_activate=user_infos["is_activate"],
                                                    is_delete=user_infos["is_delete"],
                                                    is_usable=user_infos["is_usable"],
                                                    pwd_valid_time=str(user_infos["pwd_valid_time"]),
                                                    err_pwd_count=int(user_infos["err_pwd_count"]))
            except Exception as account_err:
                await UserDao.delete_redis_token(key=key_t)
                raise account_err
            else:
                return user_infos
        else:
            raise AuthException()

    @staticmethod
    async def add_user(request, user_info):
        """
        添加用户
        Args:
            request:
            user_info:
        Returns:
        """
        await regex_register_str(email=request.email)
        async with async_db_session() as session:
            async with session.begin():
                users = await session.execute(select(User).where(
                    or_(User.username == request.username, User.email == request.email)))
            emp_no, pwd = await UserDao.exists_users(users, request)
            user = User(emp_no=emp_no, username=request.username,
                        identity=request.identity, email=request.email)
            session.add(user)
            await session.refresh(user)
            user_admin = UserAdmin(uid=user.id, emp_no=user.emp_no, is_activate=1, password=pwd,
                                   pwd_valid_time=GlobalVarEnum.PWD_VALID_TIME,
                                   create_emp_no=user_info.get("emp_no", None),
                                   registration_at=Moment.get_now_time("%Y-%m-%d %H:%M:%S"))
            session.add(user_admin)
            return PikaResponse.success(result=user, message=PromptEnum.REGISTER_SUCCEED.value)

    @staticmethod
    async def update_user_info(modify_user_info, user_info):
        """
        更新用户信息
        Args:
            modify_user_info:
            user_info:
        Returns:
        """
        await regex_register_str(email=modify_user_info.email,
                                 mobile=modify_user_info.mobile,
                                 gender=modify_user_info.gender)
        update_info = {'avatar': modify_user_info.avatar,
                       'city_name': modify_user_info.city_name,
                       'email': modify_user_info.email,
                       'gender': modify_user_info.gender,
                       'identity': modify_user_info.identity,
                       'mobile': modify_user_info.mobile,
                       'plane': modify_user_info.plane,
                       'user_alias': modify_user_info.user_alias,
                       'username': modify_user_info.username}

        async with async_db_session() as session:
            async with session.begin():
                sql = update(User).where(User.id == user_info.get("uid")).values(update_info)
                await session.execute(sql)

    @staticmethod
    async def query_user_info_list(db, request):
        if str(request.query_type) == '0':
            return await paginate(db, select(User))
        elif str(request.query_type) == '1':
            return await paginate(db, select(User).where(
                or_(User.id == request.id, User.emp_no == request.emp_no, User.email == request.email,
                    User.username.like(f"%{request.username}%"), User.user_alias.like(f"%{request.user_alias}%"),
                    User.identity == User.identity, User.mobile.like(f"%{request.mobile}%")),
                and_(User.create_time >= request.create_time, User.update_time <= request.update_time)
            ))
        else:
            return PikaResponse.failed(code=SysFailedCodeEnum.VAR_ERROR, detail=f"grant_type值不对，仅可传0：全部数据，1：条件查询")

    @staticmethod
    async def rand_dynamic_code():
        try:
            dynamic_code = MockHelper.rand_verify_code(6, 1).upper()
            await async_redis.set(RedisKeyEnum.DYNAMIC_CODE, dynamic_code, ValidTimeEnum.DYNAMIC_CODE_VALID_TIME.value)
            return PikaResponse.success(result=dynamic_code)
        except Exception as redis_err:
            raise RedisException(detail=str())

    @staticmethod
    async def has_dynamic_code(dynamic_code):
        """
        检查动态验证码是否存在
        :param dynamic_code:
        :return:
        Example::
            >>> UserDao.has_dynamic_code(8888)
            >>> UserDao.has_dynamic_code(888888)
        """
        redis_dynamic_code_ = f"{RedisKeyEnum.DYNAMIC_CODE}:{dynamic_code}"
        has_key = await async_redis.exists(redis_dynamic_code_)
        if dynamic_code in GlobalVarEnum.VERIFY_CODE_WHITE_LIST or has_key:
            return await async_redis.delele(redis_dynamic_code_)
        else:
            raise AuthException(code=SysFailedCodeEnum.DYNAMIC_ERROR, detail="验证码已过期或不存在")

    @staticmethod
    async def has_mail_verify_code(verify_code):
        """
        检查邮箱验证码是否存在
        :param verify_code:
        :return:
        Example::
            >>> UserDao.has_mail_verify_code(8888)
            >>> UserDao.has_mail_verify_code(888888)
        """
        redis_verify_code_ = f"{RedisKeyEnum.AUTH_VERIFY_CODE}:{verify_code}"
        has_key = await async_redis.exists(redis_verify_code_)
        if verify_code in GlobalVarEnum.VERIFY_CODE_WHITE_LIST or has_key:
            return await async_redis.delele(redis_verify_code_)
        else:
            raise AuthException(code=SysFailedCodeEnum.DYNAMIC_ERROR, detail="验证码已过期或不存在")

    @staticmethod
    async def verifycode_forget_pwd(request):
        pass

    @staticmethod
    async def security_forget_pwd(request):
        pass
