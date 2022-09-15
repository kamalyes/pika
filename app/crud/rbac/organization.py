# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  department.py
@Time    :  2022/9/15 11:27
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from sqlalchemy import select

from app.crud import PikaWrapper, PikaMdWrapper
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.organization import OrganizationModel
from app.schema.organization import OrganizationFormSchema


@PikaMdWrapper(OrganizationModel)
class OrganizationDao(PikaWrapper):

    @classmethod
    @RedisHelper.up_cache("dao")
    async def insert_organization(cls, form: OrganizationFormSchema, operator: int) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(OrganizationModel).where(OrganizationModel.name == form.name))
                    data = query.scalars().first()
                    if data is not None:
                        raise Exception(f"部门名称: {data.name}已存在")
                    config = OrganizationModel(**form.dict(), operator=operator)
                    session.add(config)
        except Exception as e:
            cls.__log__.error(f"新增部门: {form.name}失败, {e}")
            raise Exception(f"新增部门: {form.name}失败")
