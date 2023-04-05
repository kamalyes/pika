# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  user.py
@Time    :  2022/5/2 9:32 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import Column, String, INT, UniqueConstraint

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel


class UserModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_sys_user"
    __table_args__ = (UniqueConstraint("emp_no", "email", "mobile"), {"comment": "用户表"})
    emp_no = Column(String(ByteSizeEnum.LENGTH_16), comment="员工编号")
    username = Column(String(ByteSizeEnum.LENGTH_36), comment="正式名称（登录使用）")
    user_alias = Column(String(ByteSizeEnum.LENGTH_16), comment="花名")
    identity = Column(
        String(ByteSizeEnum.LENGTH_11),
        server_default="0",
        comment="用户身份： 最高权限：999,管理员：888,普通成员：0",
    )
    roles = Column(String(ByteSizeEnum.LENGTH_255), server_default="0", comment='用户角色')
    avatar = Column(String(ByteSizeEnum.LENGTH_255), comment="头像")
    gender = Column(INT, server_default="0", comment="性别：0-未填写,1-男,2-女")
    plane = Column(String(ByteSizeEnum.LENGTH_16), comment="座机")
    mobile = Column(String(ByteSizeEnum.LENGTH_16), comment="手机号码")
    email = Column(String(ByteSizeEnum.LENGTH_255), comment="邮箱地址")
    location = Column(String(ByteSizeEnum.LENGTH_255), server_default=None, comment="所在城市名称")

    def __init__(self, emp_no, username=None, email=None, user_alias=None, identity=0, roles=None, avatar=None,
                 gender=None,
                 plane=None, mobile=None, location=None, operator=None):
        super().__init__(operator=operator)
        self.emp_no = emp_no
        self.username = username
        self.email = email
        self.user_alias = user_alias
        self.identity = identity
        self.roles = roles
        self.avatar = avatar
        self.gender = gender
        self.plane = plane
        self.mobile = mobile
        self.location = location
