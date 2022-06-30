# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  admin.py
@Time    :  2022/5/2 10:25 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from sqlalchemy import ForeignKey
from sqlalchemy import INT, Column, DATETIME, String
from sqlalchemy.orm import relationship, backref

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase
from app.models.user import PikaUser


class PikaUserAdmin(PikaLargeBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_sys_admin"
    __table_args__ = {"comment": "账号管理表"}
    uid = Column(
        INT,
        ForeignKey(PikaUser.id, ondelete="cascade", onupdate="cascade"),
        nullable=False,
        comment="员工编号",
    )
    emp_no = Column(
        String(ByteSizeEnum.LENGTH_16),
        ForeignKey(PikaUser.emp_no, ondelete="cascade", onupdate="cascade"),
        comment="员工编号",
        nullable=False,
    )
    password = Column(String(ByteSizeEnum.LENGTH_255), comment="密码")
    pwd_valid_time = Column(DATETIME, server_default=None, comment="密码有效截止时间")
    is_activate = Column(INT, server_default="0", comment="激活状态，0：未激活、1：激活")
    private_key = Column(String(ByteSizeEnum.LENGTH_255), comment="令牌")
    open_id = Column(String(ByteSizeEnum.LENGTH_255), comment="开放者平台id")
    err_pwd_count = Column(INT, server_default="0", comment="错误密码登录的次数")
    registration_ip = Column(String(ByteSizeEnum.LENGTH_30), comment="注册时所在IP")
    registration_at = Column(DATETIME, comment="注册时间")
    last_login_ip = Column(String(ByteSizeEnum.LENGTH_30), comment="最后一次登录所在IP")
    last_logout_ip = Column(String(ByteSizeEnum.LENGTH_30), comment="最后一次退出登录的所在IP")
    last_login_city = Column(String(ByteSizeEnum.LENGTH_30), comment="最后一次登录所在城市")
    last_login_at = Column(DATETIME, server_default=None, comment="最后一次登录时间")
    last_logout_at = Column(DATETIME, server_default=None, comment="最后一次退出登录时间")
    relationship(PikaUser, backref=backref("children", cascade="all, delete"))

    def __init__(self, uid, emp_no, password, is_activate=0, create_emp_no=None,
                 registration_ip=None, registration_at=None, pwd_valid_time=PikaGlobalVarEnum.PWD_VALID_TIME):
        self.uid = uid
        self.emp_no = emp_no
        self.password = password
        self.is_activate = is_activate
        self.create_emp_no = create_emp_no
        self.registration_ip = registration_ip
        self.registration_at = registration_at
        self.pwd_valid_time = pwd_valid_time
