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

from sqlalchemy import and_, or_, select

from app.core.handler.asyncsql import AsyncDbSession
from app.core.handler.exceres import ValidException
from app.crud import PikaMdWrapper, PikaWrapper
from app.enums.SysVarEnum import ValidTimeEnum
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
                await cls.parity_field(
                    session=session, name=form.name, organization_id=form.id, parent_id=form.parent_id,
                )
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
            select(OrganizationModel).where(OrganizationModel.id == organization_id),
        )
        exists_id = query_exists_parent_id.scalars().first()
        if exists_id is None and organization_id is not None:
            raise Exception(f"组织id: {organization_id}不存在")

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
            select(OrganizationModel).where(and_(OrganizationModel.id == parent_id)),
        )
        exists_parent_id = query_exists_parent_id.scalars().first()
        if exists_parent_id is None and parent_id is not None:
            raise Exception(f"组织父id: {parent_id}不存在")

    @classmethod
    async def match_org_name(cls, session, name):
        """
        校验org_name是否存在
        Args:
            session:
            name:

        Returns:

        """
        if name is None or len(name) < 3:
            raise ValidException(detail="组织名称不能为空,或长度不能<3个字符")
        query_exists_name = await session.execute(select(OrganizationModel).where(OrganizationModel.name == name))
        exists_name = query_exists_name.scalars().first()
        if exists_name is not None:
            raise Exception(f"组织名称: {name}已存在")

    @classmethod
    async def match_org_id_equal_parent_id(cls, organization_id, parent_id):
        """
        校验org_id与parent_id是否相同
        Args:
            organization_id:
            parent_id:

        Returns:

        """
        if organization_id == parent_id and organization_id is not None:
            raise ValidException(detail=f"组织id: {organization_id}与父节点{parent_id}相同")

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
        await cls.match_org_id_equal_parent_id(organization_id=organization_id, parent_id=parent_id)
        await cls.match_org_id(session, organization_id)
        await cls.match_org_parent_id(session, parent_id)
        await cls.match_org_name(session, name)

    @classmethod
    @RedisHelper.cache("query:cache", expired_time=ValidTimeEnum.QUERY_ORGANIZATION_TIME.value)
    async def limit(cls, db, request):
        all_do_sql = select(OrganizationModel)
        dim_do_sql = select(OrganizationModel).where(
            or_(
                OrganizationModel.id == request.id,
                OrganizationModel.name == request.name,
                OrganizationModel.parent_id == request.parent_id,
                OrganizationModel.sort_id == request.sort_id,
                OrganizationModel.create_emp_no.like(f"%{request.create_emp_no}%"),
                OrganizationModel.update_emp_no.like(f"%{request.update_emp_no}%"),
                and_(
                    OrganizationModel.create_date >= request.create_date,
                    OrganizationModel.update_date <= request.update_date,
                ),
            ),
        )
        do_sql = all_do_sql if request.query_type == 0 else dim_do_sql
        return await AsyncDbSession.query(db, do_sql)
