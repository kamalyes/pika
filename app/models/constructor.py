# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  constructor.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  数据构造器表, 包含前置条件和后置条件
"""
from uuid import uuid4
from sqlalchemy import Column, INT, String, BOOLEAN, UniqueConstraint, TEXT, select, desc
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel
from app.core.handler.sqlbin_uuid import BinaryUUID


class ConstructorModel(LargeBaseModel):
    __tablename__ = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_constructor'
    __table_args__ = (UniqueConstraint('case_id', 'suffix', 'name'), {"comment": "数据构造器表"})
    type = Column(INT, default=0, comment="0: testcase 1: sqlscript 2: redis 3: py脚本 4: 其它")
    name = Column(String(ByteSizeEnum.LENGTH_50), comment="名称")
    enabled_flag = Column(BOOLEAN, default=True, nullable=False)
    constructor_json = Column(TEXT, nullable=False)
    value = Column(String(ByteSizeEnum.LENGTH_16), comment="返回值")
    case_id = Column(BinaryUUID, default=uuid4,
                     nullable=False, comment="所属用例id")
    public = Column(BOOLEAN, default=False, comment="是否共享")
    index = Column(INT, comment="前置条件顺序")
    suffix = Column(BOOLEAN, default=False, comment="是否是后置条件,默认为否")

    def __init__(self, type, name, enabled_flag, constructor_json, case_id, public,
                 operator, value="", suffix=False, id=None, index=0):
        super().__init__(id=id, operator=operator)
        self.type = type
        self.name = name
        self.enabled_flag = enabled_flag
        self.constructor_json = constructor_json
        self.case_id = case_id
        self.public = public
        self.value = value
        self.suffix = suffix
        self.index = index

    @staticmethod
    async def get_index(session, case_id, suffix=False):
        sql = select(ConstructorModel).where(
            ConstructorModel.delete_flag == 0, ConstructorModel.case_id == case_id,
            ConstructorModel.suffix == suffix,
        ).order_by(desc(ConstructorModel.index))
        data = await session.execute(sql)
        query = data.scalars().first()
        # 如果没有查出来前/后置条件,那么给他0
        if query is None:
            return 0
        return query.index + 1

    def __str__(self):
        return f"[{'后置条件' if self.suffix else '前置条件'}: {self.name}]({self.id}))"
