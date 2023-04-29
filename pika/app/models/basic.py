# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  basic.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  公共基础字段
"""
from uuid import uuid4

from sqlalchemy import BOOLEAN, DATETIME, INT, SMALLINT, TEXT, Column, String, text

from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.models import Base


class OnlyPrimaryKeyAndDesc(Base):
    id = Column(BinaryUUID, primary_key=True, default=uuid4, comment="id")
    description = Column(String(ByteSizeEnum.LENGTH_600), default=None, comment="备注信息")
    __abstract__ = True

    def __init__(self, id=None, description=None):
        self.id = id
        self.description = description


class MinBaseModel(OnlyPrimaryKeyAndDesc):
    operator = Column(String(ByteSizeEnum.LENGTH_20), comment="操作者emp_no")
    operator_date = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="操作时间",
    )
    __abstract__ = True

    def __init__(self, id=None, operator=None, description=None):
        super().__init__(id=id, description=description)
        self.operator = operator


class NormBaseModel(OnlyPrimaryKeyAndDesc):
    create_emp_no = Column(String(ByteSizeEnum.LENGTH_20), comment="创建者emp_no")
    update_emp_no = Column(String(ByteSizeEnum.LENGTH_20), comment="修改者emp_no")
    create_date = Column(
        DATETIME,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="创建日期",
    )
    update_date = Column(
        DATETIME,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        comment="修改时间",
    )
    __abstract__ = True

    def __init__(self, id=None, description=None, operator=None):
        super().__init__(id=id, description=description)
        self.create_emp_no = operator
        self.update_emp_no = operator


class LargeBaseModel(NormBaseModel):
    enabled_flag = Column(BOOLEAN, server_default="1", comment="启用标识 1:启用,0:禁用")
    delete_flag = Column(BOOLEAN, server_default="0", comment="删除标识 1:已删除,0:未删除")
    delete_date = Column(DATETIME, nullable=True, comment="删除时间")
    __abstract__ = True

    def __init__(
        self,
        id=None,
        operator=None,
        description=None,
        delete_date=None,
        enabled_flag=True,
        delete_flag=False,
    ):
        super().__init__(id=id, operator=operator, description=description)
        self.enabled_flag = enabled_flag
        self.delete_flag = delete_flag
        if isinstance(delete_date, DATETIME):
            self.delete_date = delete_date


class ApiGBaseModel(LargeBaseModel):
    url = Column(TEXT, comment="请求URL")
    order = Column(INT, server_default="1", comment="排序")
    level = Column(SMALLINT, server_default="1", nullable=False, comment="等级")
    base_gateway = Column(BinaryUUID, nullable=True, comment="请求base_gateway")
    protocol = Column(SMALLINT, server_default="1", comment="请求类型 1: http 2: grpc 3: dubbo")
    request_body_type = Column(SMALLINT, comment="请求类型, 0: none 1: json 2: form 3: x-form 4: binary 5: GraphQL")
    request_method = Column(String(ByteSizeEnum.LENGTH_12), nullable=True, comment="请求方式, 如果非http可为空")
    request_headers = Column(TEXT, comment="请求headers, 可为空")
    request_params = Column(TEXT, comment="请求params(form表单类)")
    request_body = Column(TEXT, comment="请求Body")
    response_headers = Column(TEXT, comment="响应头部")
    response = Column(TEXT, comment="返回参数")
    cost = Column(String(ByteSizeEnum.LENGTH_08), server_default="0", comment="花费时间")
    tag = Column(String(ByteSizeEnum.LENGTH_100), comment="标签")
    priority = Column(String(ByteSizeEnum.LENGTH_03), comment="用例优先级: P0-P3")
    __abstract__ = True

    def __init__(
        self,
        url=None,
        id=None,
        level=1,
        base_gateway=None,
        protocol=1,
        operator=None,
        tag=None,
        priority="P1",
        order=1,
        request_body_type=None,
        request_method=None,
        request_headers=None,
        request_params=None,
        request_body=None,
        response=None,
        response_headers=None,
        delete_flag=0,
        delete_date=None,
        cost=0,
    ):
        super().__init__(id=id, operator=operator, delete_flag=delete_flag, delete_date=delete_date)
        self.url = url
        self.order = order
        self.base_gateway = base_gateway
        self.protocol = protocol
        self.request_body_type = request_body_type
        self.tag = tag
        self.level = level
        self.priority = priority
        self.request_method = request_method
        self.request_headers = request_headers
        self.request_params = request_params
        self.request_body = request_body
        self.response = response
        self.response_headers = response_headers
        self.cost = cost
