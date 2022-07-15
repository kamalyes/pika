# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  redis_config.py
@Time    :  2021/10/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  redis配置
"""
from sqlalchemy import Column, INT, String, Boolean, UniqueConstraint

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel


class RedisModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_redis_info"
    __table_args__ = (
        UniqueConstraint('env', 'name'),
        {"comment": "Redis配置"}
    )
    env = Column(INT, nullable=False, comment="对应环境id")
    name = Column(String(ByteSizeEnum.LENGTH_24), nullable=False, comment="redis描述名称")
    addr = Column(String(ByteSizeEnum.LENGTH_128), nullable=False, comment="连接地址")
    username = Column(String(ByteSizeEnum.LENGTH_50), nullable=False, comment="用户名")
    password = Column(String(ByteSizeEnum.LENGTH_200), nullable=False, comment="用户密码")
    db = Column(INT, nullable=False, comment="库号")
    cluster = Column(Boolean, default=False, nullable=False, comment="是否是集群，默认为false，集群可不输入用户密码")

    def __init__(self, env, name, addr, cluster, operator, username='', password='', db=0, id=None):
        super().__init__(operator, id)
        self.env = env
        self.name = name
        self.addr = addr
        self.password = password
        self.username = username
        self.db = db
        self.cluster = cluster
