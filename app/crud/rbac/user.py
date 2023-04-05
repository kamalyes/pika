# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  user.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    : 　None
"""
import random
from typing import Any

from custard.core import MockHelper, Kerberos, DataHand
from custard.core.factory import fake
from custard.pagination.async_sqlalchemy import paginate
from custard.time import Moment
from sqlalchemy import or_, select, func, and_, update, delete, distinct

from app.core.handler.asyncsql import AsyncDbSession
from app.core.handler.exceres import AuthException, \
    SystemException, ThirdException, RedisException,  ValidException
from app.core.handler.jsonres import PikaResponse
from app.crud import PikaWrapper, PikaMdWrapper
from app.crud.rbac import regex_register_str, client_ip
from app.crud.system import Email
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.OperationEnum import VerifyCodeEnum
from app.enums.PromptEnum import PromptEnum
from app.enums.RbacEnum import RoleEnum
from app.enums.RedisEnum import RedisKeyEnum
from app.enums.SysCodeEnum import ExcCodeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum, ValidTimeEnum
from app.middleware.xredis import RedisHelper
from app.models import async_db_session_generator, async_redis, async_session
from app.models.admin import SysUserAdminModel
from app.models.kerberos import PikaSecurityRelIssues
from app.models.user import UserModel
from config import PikaAppConfig


@PikaMdWrapper(UserModel)
class UserDao(PikaWrapper):

    @staticmethod
    async def assert_user_info(username, exists_username, email, exists_email, mobile=None,
                               exists_mobile=None):
        """
        判断用户名或邮箱或手机号是否被注册使用
        Args:
            username:
            exists_username:
            email:
            exists_email:
            mobile:
            exists_mobile:

        Returns:

        """
        if username == exists_username:
            raise SystemException(
                code=ExcCodeEnum.USER_HAS_USED, detail="该用户名已被使用！")
        elif email == exists_email:
            raise SystemException(
                code=ExcCodeEnum.EMAIL_HAS_USED, detail="该邮箱账号已被使用！")
        elif mobile == exists_mobile and (mobile is not None and exists_mobile is not None):
            raise SystemException(
                code=ExcCodeEnum.EMAIL_HAS_USED, detail="该手机号已被使用！")

    @classmethod
    async def create_users_epd(cls, users: Any, request):
        exists_users = users.scalars().first()
        if exists_users:
            await cls.assert_user_info(username=request.username,
                                       exists_username=exists_users.username,
                                       email=request.email, exists_email=exists_users.email)
        # 注册的时候给密码加盐
        pwd = Kerberos.md5_encode(decode_msg=request.password)
        emp_no = f"{PikaGlobalVarEnum.EMP_NO_START}{MockHelper.rand_verify_code(6, 1)}".upper(
        )
        return emp_no, pwd

    @classmethod
    async def register_user(cls, request, register_model):
        """
        用户注册
        Args:
            request:
            register_model:
        Returns:
        """
        user_ip = await client_ip(request)
        async with async_db_session_generator() as session:
            async with session.begin():
                users = await session.execute(select(UserModel).where(
                    or_(UserModel.username == register_model.username,
                        UserModel.email == register_model.email)))
                counts = await session.execute(select(func.count(UserModel.id)))
                # 如果用户数量为0 则注册为超管,且激活状态为1
                identity = RoleEnum.ADMIN.value if counts.scalars(
                ).first() == 0 else RoleEnum.ORDINARY.value
                is_activate = 1 if identity == RoleEnum.ADMIN else 0
                emp_no, pwd = await cls.create_users_epd(users=users, request=register_model)
                user = UserModel(emp_no=emp_no, username=register_model.username,
                                 identity=identity,
                                 email=register_model.email)
                session.add(user)
                await session.flush()
                await session.refresh(user)
                pwd_valid_date = PikaGlobalVarEnum.PWD_VALID_DATE
                user_admin = SysUserAdminModel(uid=user.id, emp_no=user.emp_no, is_activate=is_activate,
                                               password=pwd,
                                               pwd_valid_date=pwd_valid_date,
                                               registration_date=Moment.get_now_time(
                                                   PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS),
                                               registration_ip=user_ip)
                session.add(user_admin)
        try:
            await Email.register_succeed(emp_no=user.emp_no, username=register_model.username,
                                         addressee=register_model.email,
                                         pwd_valid_date=pwd_valid_date)
        except Exception as e:
            pass
        return PikaResponse.success(data=user, message=PromptEnum.REGISTER_SUCCEED.value)

    @staticmethod
    async def account_status_verify(**kwargs):
        # 状态
        if kwargs["delete_flag"]:
            raise AuthException(
                code=ExcCodeEnum.ACCOUNT_HAS_DELETE, detail="账号已被删除！")
        if kwargs["enabled_flag"] is False:
            raise AuthException(
                code=ExcCodeEnum.ACCOUNT_HAS_DIS_ENABLED, detail="账号已被禁用！")
        if kwargs["is_activate"] == 0:
            raise AuthException(
                code=ExcCodeEnum.ACCOUNT_HAS_NOT_ACTIVATE, detail="账号未激活！")
        try:
            compare_time = Moment.compare_time(kwargs["pwd_valid_date"],
                                               Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS))
        except Exception as e:
            raise SystemException(
                code=ExcCodeEnum.FIELD_TYPE_ERROR, detail=f"密码有效期对比失败！具体错误原因：{e}")
        if compare_time is False:
            raise AuthException(
                code=ExcCodeEnum.PASSWORD_HAS_EXPIRED, detail="密码已过期,请修改后进行登录！")

    @staticmethod
    async def pwd_mistake_limit(**kwargs):
        async with async_db_session_generator() as session:
            async with session.begin():
                err_pwd_counts = await session.execute(
                    select(SysUserAdminModel.err_pwd_count).where(SysUserAdminModel.uid == kwargs["uid"]))
                err_pwd_count = err_pwd_counts.scalars().first()
                if err_pwd_count >= ValidTimeEnum.ERR_PWD_COUNT.value:
                    raise AuthException(code=ExcCodeEnum.PASSWORD_ERROR_COUNT_OUT,
                                        detail="错误密码次数超出限制,请联系管理员或稍后重试！")
                else:
                    sql = update(SysUserAdminModel).where(SysUserAdminModel.uid == kwargs["uid"]).values(
                        {"err_pwd_count": int(err_pwd_count + 1)})
                    await session.execute(sql)
                    await session.commit()
                    raise AuthException(
                        code=ExcCodeEnum.PASSWORD_ERROR, detail="登录密码错误！")

    @classmethod
    async def generate_uuid_jwt(cls, **kwargs):
        """
        生成jwt+uuid形态的token
        Args:
            **kwargs:
        Returns:
        """
        target_value = {
            "emp_no": kwargs["emp_no"], "password": kwargs["password"]}
        try:
            uuid4_ = str(fake.uuid4).upper()
            jwt_encode_result = Kerberos.jwt_encode(secret_key=PikaAppConfig.JWT_SECRET_KEY,
                                                    target_value=target_value,
                                                    seconds=kwargs["valid_time"])
            return f'{jwt_encode_result}.{uuid4_}'.replace("4", str(random.randint(5, 9)))
        except Exception as uuid_jwt_err:
            raise ThirdException(code=ExcCodeEnum.JWT_ENCODE_ERROR,
                                 detail=f"加密失败,具体原因{uuid_jwt_err}")

    @classmethod
    async def uuid_jwt_sync_redis(cls, **kwargs):
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

    @classmethod
    async def delete_redis_token(cls, **kwargs):
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

    @classmethod
    async def update_last_login_field(cls, **kwargs):
        uid, emp_no = kwargs.get("uid", None), kwargs.get("emp_no", None)
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = update(SysUserAdminModel).where(
                    or_(SysUserAdminModel.id == uid, SysUserAdminModel.emp_no == emp_no)).values(
                    {"last_login_ip": kwargs["last_login_ip"],
                     "last_login_date": Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)})
                await session.execute(sql)

    @classmethod
    async def update_last_logout_field(cls, **kwargs):
        uid, emp_no, last_logout_ip = kwargs.get("uid", None), kwargs.get("emp_no", None), kwargs[
            "last_logout_ip"]
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = update(SysUserAdminModel).where(
                    or_(SysUserAdminModel.id == uid, SysUserAdminModel.emp_no == emp_no)).values(
                    {"last_logout_ip": last_logout_ip,
                     "last_logout_date": Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)})
                await session.execute(sql)

    @classmethod
    async def update_avatar(cls, emp_no, avatar):
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = update(UserModel).where(UserModel.emp_no == emp_no).values(
                    {"avatar": avatar})
                await session.execute(sql)

    @classmethod
    async def query_user_info(cls, **kwargs):
        uid, emp_no = kwargs.get("uid", None), kwargs.get("emp_no", None)
        async with async_db_session_generator() as session:
            users = await session.execute(
                select(UserModel).where(
                    or_(UserModel.id == uid, UserModel.emp_no == emp_no)))
            user_admins = await session.execute(
                select(SysUserAdminModel).where(
                    or_(SysUserAdminModel.uid == uid, SysUserAdminModel.emp_no == emp_no)))
            user, user_admin = users.scalars().first(), user_admins.scalars().first()
            if user and user_admin:
                user_infos = DataHand.chain_all([PikaResponse.model_to_dict(user),
                                                 PikaResponse.model_to_dict(user_admin)])
                # 屏蔽字段
                dislodge = ["open_id", "private_key",
                            "password", "description", "id"]
                result = {key: val for key, val in user_infos.items()
                          if key not in dislodge}
            else:
                raise AuthException(detail="用户信息不存在！")
        return result

    @classmethod
    async def account_login(cls, request, oauth2_login):
        """
        账号登录
        Args:
            request:
            oauth2_login:
        Returns:
        """
        user_ip = await client_ip(request)
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = select(UserModel).where(or_(UserModel.username == oauth2_login.username,
                                                  UserModel.emp_no == oauth2_login.username,
                                                  UserModel.mobile == oauth2_login.username,
                                                  UserModel.email == oauth2_login.username))
                users = await session.execute(sql)
                user = users.scalars().first()
                if user:
                    pwd = Kerberos.md5_encode(oauth2_login.password)
                    user_admins = await session.execute(
                        select(SysUserAdminModel).where(
                            and_(SysUserAdminModel.password == pwd,
                                 SysUserAdminModel.uid == user.id)))
                    user_admin = user_admins.scalars().first()
                    if user_admin:
                        await cls.account_status_verify(uid=user_admin.uid,
                                                        is_activate=user_admin.is_activate,
                                                        delete_flag=user_admin.delete_flag,
                                                        enabled_flag=user_admin.enabled_flag,
                                                        pwd_valid_date=str(
                                                            user_admin.pwd_valid_date),
                                                        err_pwd_count=int(user_admin.err_pwd_count))
                    else:
                        await cls.pwd_mistake_limit(uid=user.id)
                    old_token = await async_redis.get(
                        f'{RedisKeyEnum.AUTH_TOKEN}:{user_admin.emp_no}')
                    if old_token and PikaAppConfig.JWT_MPOP:
                        uuid_jwt = old_token
                    else:
                        # 生成uuid_jwt并同步至redis
                        valid_time = ValidTimeEnum.AUTH_VALID_TIME
                        uuid_jwt = await cls.generate_uuid_jwt(emp_no=user.emp_no,
                                                               valid_time=valid_time,
                                                               password=user_admin.password)
                        await cls.uuid_jwt_sync_redis(
                            key=f'{RedisKeyEnum.AUTH_TOKEN}:{user.emp_no}',
                            value=uuid_jwt,
                            ex=valid_time)
                else:
                    raise AuthException(code=ExcCodeEnum.ACCOUNT_NOT_EXISTS,
                                        detail="该用户名不存在,请使用正常的账户登录！")
        await cls.update_last_login_field(uid=user.id, last_login_ip=user_ip)
        user_infos = await cls.query_user_info(uid=user.id)
        return PikaResponse.success(
            data=DataHand.chain_all([user_infos, {"token": uuid_jwt}]),
            message=PromptEnum.LOGIN_SUCCEED.value)

    @classmethod
    async def email_login(cls, request, oauth2_login):
        """
        邮箱登录
        Args:
            request:
            oauth2_login:
        Returns:
        """
        user_ip = await client_ip(request)
        if oauth2_login.email is None:
            raise ValidException(detail="字段：email不能为空")
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = select(UserModel).where(
                    UserModel.email == oauth2_login.email)
                users = await session.execute(sql)
                user = users.scalars().first()
                if user:
                    await cls.has_mail_verify_code(verify_code=oauth2_login.dynamic_code,
                                                   model=2,
                                                   emp_no=user.emp_no)
                    user_admins = await session.execute(
                        select(SysUserAdminModel).where(SysUserAdminModel.uid == user.id))
                    user_admin = user_admins.scalars().first()
                    if user_admin:
                        await cls.account_status_verify(uid=user_admin.uid,
                                                        is_activate=user_admin.is_activate,
                                                        delete_flag=user_admin.delete_flag,
                                                        enabled_flag=user_admin.enabled_flag,
                                                        pwd_valid_date=str(
                                                            user_admin.pwd_valid_date))
                    else:
                        await cls.pwd_mistake_limit(uid=user.id)
                    old_token = await async_redis.get(
                        f'{RedisKeyEnum.AUTH_TOKEN}:{user_admin.emp_no}')
                    if old_token and PikaAppConfig.JWT_MPOP:
                        uuid_jwt = old_token
                    else:
                        # 生成uuid_jwt并同步至redis
                        valid_time = ValidTimeEnum.AUTH_VALID_TIME
                        uuid_jwt = await cls.generate_uuid_jwt(emp_no=user.emp_no,
                                                               valid_time=valid_time,
                                                               password=user_admin.password)
                        await cls.uuid_jwt_sync_redis(
                            key=f'{RedisKeyEnum.AUTH_TOKEN}:{user.emp_no}',
                            value=uuid_jwt,
                            ex=valid_time)
                else:
                    raise AuthException(code=ExcCodeEnum.EMAIL_NOT_REGISTER,
                                        detail="该邮箱暂未被注册,请使用正常的账户登录！")
        await cls.update_last_login_field(uid=user.id, last_login_ip=user_ip)
        async with async_db_session_generator as session:
            async with session.begin():
                sql = update(SysUserAdminModel).where(
                    or_(SysUserAdminModel.emp_no == user.emp_no)).values({"err_pwd_count": 0})
                await session.execute(sql)
                session.execute()
        user_infos = await cls.query_user_info(uid=user.id)
        return PikaResponse.success(
            data=DataHand.chain_all([user_infos, {"token": uuid_jwt}]),
            message=PromptEnum.LOGIN_SUCCEED.value)

    @classmethod
    async def account_logout(cls, request, oauth2_logout):
        await cls.verify_token(oauth2_logout)
        key_t = f'{RedisKeyEnum.AUTH_TOKEN}:{oauth2_logout.emp_no}'
        last_logout_ip = await client_ip(request)
        await cls.delete_redis_token(key=key_t)
        await cls.update_last_logout_field(emp_no=oauth2_logout.emp_no,
                                           last_logout_ip=last_logout_ip)
        return PikaResponse.success(message="注销登录成功！")

    @classmethod
    async def verify_token(cls, request):
        """
        验证token
        Args:
            request:
        Returns:
        """
        key_t = f'{RedisKeyEnum.AUTH_TOKEN}:{request.emp_no}'
        exists_token = await async_redis.get(key_t)
        if exists_token == request.token:
            user_infos = await cls.query_user_info(emp_no=request.emp_no)
            try:
                await cls.account_status_verify(uid=user_infos["uid"],
                                                is_activate=user_infos["is_activate"],
                                                delete_flag=user_infos["delete_flag"],
                                                enabled_flag=user_infos["enabled_flag"],
                                                pwd_valid_date=str(
                                                    user_infos["pwd_valid_date"]),
                                                err_pwd_count=int(user_infos["err_pwd_count"]))
            except Exception as account_err:
                await cls.delete_redis_token(key=key_t)
                raise account_err
            else:
                return user_infos
        else:
            raise AuthException()

    @classmethod
    async def add_user(cls, request, user_info):
        """
        添加用户
        Args:
            request:
            user_info:
        Returns:
        """
        await regex_register_str(email=request.email)
        async with async_db_session_generator() as session:
            async with session.begin():
                users = await session.execute(select(UserModel).where(
                    or_(UserModel.username == request.username,
                        UserModel.email == request.email)))
                emp_no, pwd = await cls.create_users_epd(users, request)
                user = UserModel(emp_no=emp_no, username=request.username,
                                 identity=request.identity, email=request.email)
                session.add(user)
            await session.refresh(user)
            user_admin = SysUserAdminModel(uid=user.id, emp_no=user.emp_no, is_activate=1,
                                           password=pwd,
                                           pwd_valid_date=PikaGlobalVarEnum.PWD_VALID_DATE,
                                           create_emp_no=user_info.get(
                                               "emp_no", None),
                                           registration_date=Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS))
            session.add(user_admin)
            return PikaResponse.success(data=user, message=PromptEnum.REGISTER_SUCCEED.value)

    @classmethod
    async def update_user_info(cls, modify_user_info, user_info):
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
                       'location': modify_user_info.location,
                       'email': modify_user_info.email,
                       'gender': modify_user_info.gender,
                       # 'identity': modify_user_info.identity,
                       'mobile': modify_user_info.mobile,
                       'plane': modify_user_info.plane,
                       'user_alias': modify_user_info.user_alias,
                       'username': modify_user_info.username}

        async with async_db_session_generator() as session:
            async with session.begin():
                sel_sql = select(UserModel).where(
                    and_(or_(UserModel.email == modify_user_info.email,
                             UserModel.mobile == modify_user_info.mobile,
                             UserModel.plane == modify_user_info.plane),
                         UserModel.emp_no != user_info.get("emp_no")))
                sel_res = await session.execute(sel_sql)
                exists_users = sel_res.scalars().first()
                if exists_users:
                    await cls.assert_user_info(username=modify_user_info.username,
                                               exists_username=exists_users.username,
                                               email=modify_user_info.email,
                                               exists_email=exists_users.email)
                sql = update(UserModel).where(UserModel.id == user_info.get("uid")).values(
                    update_info)
                await session.execute(sql)
        return PikaResponse.success()

    @staticmethod
    async def query_user_info_list(db, request):
        if str(request.query_type) == '0':
            return await paginate(db, select(UserModel))
        elif str(request.query_type) == '1':
            return await paginate(db, select(UserModel).where(
                or_(UserModel.id == request.id, UserModel.emp_no == request.emp_no,
                    UserModel.email == request.email,
                    UserModel.username.like(f"%{request.username}%"),
                    UserModel.user_alias.like(f"%{request.user_alias}%"),
                    UserModel.identity == request.identity,
                    UserModel.mobile.like(f"%{request.mobile}%")),
                and_(UserModel.create_date >= request.create_date,
                     UserModel.update_date <= request.update_date)
            ))
        else:
            return PikaResponse.failed(code=ExcCodeEnum.VAR_ERROR,
                                       detail=f"query_type值不对,仅可传0：全部数据,1：条件查询")

    @staticmethod
    async def rand_dynamic_code(request):
        try:
            user_ip = await client_ip(request)
            dynamic_code = MockHelper.rand_verify_code(6, 1).upper()
            key_name = f"{RedisKeyEnum.DYNAMIC_CODE}:{dynamic_code}"
            await async_redis.set(key_name, str(user_ip),
                                  ValidTimeEnum.DYNAMIC_CODE_VALID_TIME.value)
            return PikaResponse.success(data=dynamic_code)
        except Exception as redis_err:
            raise RedisException(detail=str(redis_err))

    @staticmethod
    async def has_dynamic_code(dynamic_code):
        """
        检查动态验证码是否存在
        Args:
            dynamic_code:

        Returns:

        Example::
            >>> UserDao.has_dynamic_code(8888)
            >>> UserDao.has_dynamic_code(888888)
        """
        redis_dynamic_code_ = f"{RedisKeyEnum.DYNAMIC_CODE}:{dynamic_code}"
        has_key = await async_redis.exists(redis_dynamic_code_)
        if dynamic_code in PikaGlobalVarEnum.VERIFY_CODE_WHITE_LIST or has_key:
            return await async_redis.delete(redis_dynamic_code_)
        else:
            raise SystemException(
                code=ExcCodeEnum.DYNAMIC_ERROR, detail="验证码已过期或不存在")

    @staticmethod
    async def has_mail_verify_code(verify_code, model=1, emp_no=None, addressee=None):
        """
        检查邮箱验证码是否存在
            verify_code:
            model:
            emp_no:
        Returns:
        Example::
            >>> UserDao.has_mail_verify_code(8888)
            >>> UserDao.has_mail_verify_code("QbLXMk")
        """
        if model == 1:
            redis_verify_code_ = f"{RedisKeyEnum.FORGET_PWD_VERIFYCODE}"
        elif model == 2:
            redis_verify_code_ = f"{RedisKeyEnum.EMAIL_LOGIN_VERIFYCODE}:{emp_no}"
        elif model == 3:
            redis_verify_code_ = f"{RedisKeyEnum.REGISTER_VERIFYCODE}:{addressee}"
        else:
            raise ValidException(detail="暂不支持该model！")
        has_key = await async_redis.get(redis_verify_code_)
        if verify_code in PikaGlobalVarEnum.VERIFY_CODE_WHITE_LIST or has_key == verify_code:
            return await async_redis.delete(redis_verify_code_)
        else:
            raise SystemException(
                code=ExcCodeEnum.DYNAMIC_ERROR, detail="验证码已过期或不存在")

    @staticmethod
    async def get_verifycode(request, user_info):
        if request.models is VerifyCodeEnum.FORGET_PWD.value:
            await Email.rand_mail_code(emp_no=user_info["emp_no"], username=user_info["username"],
                                       addressee=user_info["email"])
        else:
            raise ValidException(detail="暂不支持该models！")
        return PikaResponse.success(message=PromptEnum.GET_VERIFY_SUCCEED.value)

    @staticmethod
    async def send_email_verify_code(request):
        if request.model == 2:
            async with async_db_session_generator() as session:
                async with session.begin():
                    sel_sql = select(UserModel).where(
                        UserModel.email == request.email)
                    sel_res = await session.execute(sel_sql)
                    exists_users = sel_res.scalars().first()
                    if not exists_users:
                        raise AuthException(detail="该邮箱暂未注册使用！")
            await Email.rand_mail_code(emp_no=exists_users.emp_no, username=exists_users.username,
                                       addressee=exists_users.email, model=2)
        elif request.model == 3:
            await regex_register_str(email=request.email)
            await Email.rand_mail_code(addressee=request.email, model=3)
        else:
            raise ValidException(detail="暂不支持该model！")
        return PikaResponse.success(message=PromptEnum.GET_VERIFY_SUCCEED.value)

    @staticmethod
    async def update_pwd(**kwargs):
        emp_no, new_password = kwargs["emp_no"], kwargs["new_password"]
        pwd = Kerberos.md5_encode(decode_msg=new_password)
        pwd_valid_date = PikaGlobalVarEnum.PWD_VALID_DATE
        update_info = {'password': pwd, 'pwd_valid_date': pwd_valid_date}
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = update(SysUserAdminModel).where(SysUserAdminModel.emp_no == emp_no).values(
                    update_info)
                await session.execute(sql)

    @classmethod
    async def old_value_update_pwd(cls, **kwargs):
        emp_no = kwargs["emp_no"]
        old_password, new_password = kwargs["old_password"], kwargs["new_password"]
        async with async_db_session_generator() as session:
            async with session.begin():
                user_admins = await session.execute(
                    select(SysUserAdminModel).where(
                        and_(SysUserAdminModel.password == old_password,
                             SysUserAdminModel.emp_no == emp_no)))
                user_admin = user_admins.scalars().first()
                if user_admin:
                    await cls.update_pwd(new_password=new_password, emp_no=emp_no)
                else:
                    raise AuthException(
                        code=ExcCodeEnum.PASSWORD_ERROR, detail="请检查旧密码是否正确")

    @staticmethod
    async def add_security(**kwargs):
        emp_no, uid = kwargs["user_info"]["emp_no"], kwargs["user_info"]["uid"]
        pending_begin = [{**index, **{"create_emp_no": kwargs["emp_no"]}} for index in
                         [dict(element) for element in kwargs["security"].security]]
        min_begin_number, max_begin_number = ByteSizeEnum.LENGTH_03, ByteSizeEnum.LENGTH_06
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin),
                                        min_begin_number=min_begin_number,
                                        max_begin_number=max_begin_number)
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = select(func.count(PikaSecurityRelIssues.id)).where(
                    PikaSecurityRelIssues.emp_no == emp_no)
                execute_select = await session.execute(sql)
                if execute_select.scalars().first() != 0:
                    return PikaResponse.failed(code=ExcCodeEnum.VAR_ERROR, detail="密保问题已设置,无需添加")
                await session.execute(PikaSecurityRelIssues.__table__.insert(), pending_begin)
                return PikaResponse.success()

    @staticmethod
    async def empty_security(**kwargs):
        ids, emp_no = kwargs["request"].ids.split(","), kwargs["emp_no"]
        async with async_db_session_generator() as session:
            sel_res = await session.execute(select(PikaSecurityRelIssues.id).where(
                and_(PikaSecurityRelIssues.id.in_(ids), PikaSecurityRelIssues.emp_no == emp_no)))
            sel_res_ids = sel_res.scalars().all()
            intersection = list(set(ids).difference(
                set(str(index) for index in sel_res_ids)))
            if not sel_res_ids:
                return PikaResponse.failed(detail="删除失败,id验签不通过")
            elif len(intersection) > 0:
                return PikaResponse.failed(detail="非管理员仅可删除自身的密保",
                                           data={"intersection": intersection})
            elif len(sel_res_ids) < 3:
                raise ValidException(detail="需一次传入所有有效密保id才可以清除")
        del_sql = delete(PikaSecurityRelIssues).where(
            and_(PikaSecurityRelIssues.id.in_(ids), PikaSecurityRelIssues.emp_no == emp_no))
        return await AsyncDbSession.delete(ids=ids, do_sql=del_sql)

    @staticmethod
    async def update_security(**kwargs):
        emp_no, uid = kwargs["user_info"]["emp_no"], kwargs["user_info"]["uid"]
        pending_begin = kwargs["request"].security
        success, failed, not_funded = [], [], []
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin))
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = select(distinct(PikaSecurityRelIssues.id)).where(
                    and_(PikaSecurityRelIssues.id.in_([index.id for index in pending_begin]),
                         PikaSecurityRelIssues.emp_no == emp_no))
                execute_exists_id = await session.execute(sql)
                exists_id = [index[0]
                             for index in [id_ for id_ in execute_exists_id.all()]]
                # 遍历更新
                for pb in pending_begin:
                    if pb.id in exists_id:
                        sql = update(PikaSecurityRelIssues).where(
                            PikaSecurityRelIssues.id == pb.id).values(
                            {"question": pb.question, "answers": pb.answers})
                        try:
                            await session.execute(sql)
                        except Exception as e:
                            failed.append(e)
                        else:
                            success.append(pb)
                    else:
                        not_funded.append(pb)
            if len(failed) <= 0 and 0 >= len(not_funded):
                return PikaResponse.success(message=f"修改成功！")
            else:
                if len(success) <= 0 and (0 < len(failed) or len(not_funded) > 0):
                    msg = "修改失败"
                else:
                    msg = "部分修改成功"
                return PikaResponse.success(code=ExcCodeEnum.SQL_OPERATION_ERROR,
                                            message=f'{msg},详情请查阅返回值！',
                                            data={"success": success, "failed": failed,
                                                  "not_funded": not_funded})

    @staticmethod
    async def query_security(db, emp_no):
        return await paginate(db, select(PikaSecurityRelIssues).where(
            PikaSecurityRelIssues.emp_no == emp_no))

    @classmethod
    @RedisHelper.cache("user_list", ValidTimeEnum.USER_LIST_TIME.value)
    async def query_all_users(cls):
        try:
            async with async_session() as session:
                # TODO 需要解构,简化下字段
                query_sql = select(UserModel.id, UserModel.username,
                                   UserModel.email, UserModel.emp_no,
                                   UserModel.create_emp_no, UserModel.user_alias,
                                   UserModel.update_date, UserModel.roles, UserModel.avatar,
                                   UserModel.gender, UserModel.identity, UserModel.location,
                                   UserModel.update_emp_no, UserModel.mobile, UserModel.plane,
                                   SysUserAdminModel.delete_flag, SysUserAdminModel.enabled_flag,
                                   SysUserAdminModel.is_activate, SysUserAdminModel.err_pwd_count,
                                   SysUserAdminModel.last_login_date, SysUserAdminModel.last_login_ip,
                                   SysUserAdminModel.last_login_location, SysUserAdminModel.last_logout_date,
                                   SysUserAdminModel.last_logout_ip, SysUserAdminModel.registration_date,
                                   SysUserAdminModel.registration_ip, SysUserAdminModel.create_date
                                   ) \
                    .join(SysUserAdminModel, UserModel.id == SysUserAdminModel.uid)
                query_sql_execute = await session.execute(query_sql)
                query_result = query_sql_execute.all()
                return query_result
        except Exception as e:
            cls.__log__.error(f"获取用户列表失败: {str(e)}")
            raise SystemException(detail="获取用户列表失败")

    @classmethod
    @RedisHelper.cache("user_detail", ValidTimeEnum.USER_DETAIL_TIME.value)
    async def query_user(cls, id: str):
        async with async_session() as session:
            query_sql = select(UserModel) \
                .outerjoin(SysUserAdminModel, UserModel.id == SysUserAdminModel.uid).where(UserModel.id == id)
            query_result = await session.execute(query_sql)
            return query_result.scalars().first()

    @classmethod
    @RedisHelper.cache("user_touch")
    async def list_user_touch(cls, *user):
        try:
            if not user:
                return []
            async with async_session() as session:
                query_user = await session.execute(
                    select(UserModel).where(UserModel.id.in_(user)))
                return [{"email": quser.email, "phone": quser.phone} for quser in
                        query_user.scalars().all()]
        except Exception as e:
            cls.__log__.error(f"获取用户联系方式失败: {str(e)}")
            raise SystemException(detail=f"获取用户联系方式失败: {e}")
