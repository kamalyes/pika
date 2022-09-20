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

from sqlalchemy import select, and_

from app.core.handler.execres import SystemException
from app.crud import PikaWrapper, PikaMdWrapper
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.organization import OrganizationModel
from app.schema.organization import OrganizationFormSchema


@PikaMdWrapper(OrganizationModel)
class OrganizationDao(PikaWrapper):

    @classmethod
    @RedisHelper.up_cache("dao")
    async def insert_organization(cls, form: OrganizationFormSchema, operator: str) -> None:
        async with async_session() as session:
            async with session.begin():
                await cls.parity_field(session=session, name=form.name,
                                       organization_id=form.id, parent_id=form.parent_id)
                config = OrganizationModel(**form.dict(), operator=operator)
                session.add(config)

    @classmethod
    async def match_org_id(cls, session, organization_id):
        """
        校验org_id是否存在
        Args:
            session:
            organization_id:

        Returns:

        """
        query_exists_parent_id = await session.execute(
            select(OrganizationModel).where(OrganizationModel.id == organization_id))
        exists_id = query_exists_parent_id.scalars().first()
        if exists_id is None and organization_id != 0:
            raise SystemException(detail=f"组织id: {organization_id}不存在")

    @classmethod
    async def match_org_parent_id(cls, session, parent_id):
        """
        校验org_parent_id是否存在
        Args:
            session:
            parent_id:

        Returns:

        """
        query_exists_parent_id = await session.execute(
            select(OrganizationModel).where(
                and_(OrganizationModel.id == parent_id)))
        exists_parent_id = query_exists_parent_id.scalars().first()
        if exists_parent_id is None and parent_id != 0:
            raise SystemException(detail=f"组织父id: {parent_id}不存在")

    @classmethod
    async def match_org_name(cls, session, name):
        """
        校验org_name是否存在
        Args:
            session:
            name:

        Returns:

        """
        query_exists_name = await session.execute(
            select(OrganizationModel).where(OrganizationModel.name == name))
        exists_name = query_exists_name.scalars().first()
        if exists_name is not None:
            raise SystemException(detail=f"组织名称: {name}已存在")

    @classmethod
    async def parity_field(cls, session, name, organization_id, parent_id):
        """
        检查字段
        Args:
            session:
            name:
            organization_id:
            parent_id:

        Returns:

        """
        await cls.match_org_id(session, organization_id)
        await cls.match_org_parent_id(session, parent_id)
        await cls.match_org_name(session, name)
