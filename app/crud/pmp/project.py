# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  project.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import asyncio
from copy import deepcopy
from datetime import datetime
from typing import List

from sqlalchemy import or_, select, desc, func, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.handler.exceres import AuthException, KeyExistException, KeyUndefinedException, SystemException
from app.crud import PikaWrapper, PikaMdWrapper
from app.enums.OperationEnum import SqlOperationTypeEnum
from app.enums.RbacEnum import RoleEnum
from app.models import async_session
from app.models.project import ProjectModel, ProjectRoleModel
from app.schema.project import ProjectRoleEditSchema


@PikaMdWrapper(ProjectModel)
class ProjectDao(PikaWrapper):

    @classmethod
    async def list_project(cls, operator: str, operator_identity: int, paging,
                           name: str = None) -> (List[ProjectModel]):
        """
        查询/获取项目列表
        Args:
            operator:    操作者员工编号
            operator_identity:  操作者身份
            paging:   分页
            name:   项目名称

        Returns:

        """
        try:
            search = [ProjectModel.delete_flag == 0]
            async with async_session() as session:
                if operator_identity != RoleEnum.ADMIN:
                    project_list = await ProjectRoleDao.list_project_by_user(operator)
                    # 找出用户能看到的公开项目
                    search.append(
                        or_(ProjectModel.id.in_(project_list), ProjectModel.owner == operator,
                            ProjectModel.private == 0))
                if name:
                    search.append(ProjectModel.name.like("%{}%".format(name)))
                sql = select(ProjectModel).where(
                    *search).order_by(desc(ProjectModel.update_date))
                data = await session.execute(sql)
                sql = sql.offset((paging.page_index - 1) *
                                 paging.page_size).limit(paging.page_size)
                total = data.raw.rowcount
                data = await session.execute(sql)
                return data.scalars().all(), total
        except Exception as e:
            cls.__log__.error(f"获取用户: {operator}项目列表失败, {e}")
            raise SystemException(detail=f"获取用户: {operator}项目列表失败")

    @classmethod
    async def list_project_id_by_user(cls, session, operator, role):
        """
        获取用户可见的项目
        :return:
        """
        if role == RoleEnum.ADMIN:
            return []
        ans = set()
        # 找到包含用户的角色
        sel_role2user = select(ProjectRoleModel.project_id).where(
            ProjectRoleModel.member_no == operator)
        roles = await session.execute(sel_role2user)
        for r in roles.all():
            ans.add(r[0])
        # 找到未删除的项目
        sel_not_del_dt = select(ProjectModel.id).where(
            or_(ProjectModel.private is False, ProjectModel.owner == operator),
            ProjectModel.delete_flag == 0)
        roles = await session.execute(sel_not_del_dt)
        for r in roles.all():
            ans.add(r[0])
        return list(ans) if len(ans) > 0 else None

    @classmethod
    async def is_project_admin(cls, session, project_id: str, operator: str):
        query = await session.execute(
            select(ProjectModel.owner).where(ProjectModel.id == project_id))
        return query.scalars().first() == operator

    @classmethod
    async def add_project(cls, name, app, owner, operator, private, description, dingtalk_url='',
                          qy_wx_url=''):
        async with async_session() as session:
            async with session.begin():
                data = await session.execute(
                    select(ProjectModel).where(ProjectModel.name == name,
                                               ProjectModel.delete_flag == 0))
                if data.scalars().first() is not None:
                    err = f"新增项目: {name}失败, 失败原因：项目已存在"
                    cls.__log__.error(err)
                    raise KeyExistException(detail=err)
                pr = ProjectModel(name, app, owner, operator, description, private, dingtalk_url,
                                  qy_wx_url)
                session.add(pr)

    @classmethod
    async def update_avatar(cls, project_id: str, operator: str, operator_identity: int,
                            file_url: [str, int]):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ProjectModel).where(ProjectModel.id == project_id,
                                                   ProjectModel.delete_flag == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise KeyUndefinedException(detail="项目不存在")
                    if data.owner != operator and operator_identity < RoleEnum.ADMIN:
                        raise SystemException(detail="你没有权限修改项目头像")
                    # 如果修改人不是owner或者超管
                    data.avatar = file_url
                    data.update_date = datetime.now()
                    data.update_user = operator
        except Exception as e:
            cls.__log__.error(f"修改项目头像失败, 项目: {project_id}, error: {e}")
            raise SystemException(detail=e)

    @classmethod
    async def update_project(cls, id: str, operator, operator_identity: int, name: str, app: str,
                             owner: str,
                             private: bool, description: str,
                             dingtalk_url: str = None, qy_wx_url: str = None) -> None:
        """
        修改项目
        Args:
            id: 项目id
            operator: 修改者员工编号
            operator_identity:  操作者身份
            name:   项目名称
            app:    项目所属应用
            owner:  项目所有者
            private:    是否私有
            description:    项目描述
            dingtalk_url:   钉钉通知url
            qy_wx_url:  企微通知url

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ProjectModel).where(ProjectModel.id == id,
                                                   ProjectModel.delete_flag == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise KeyUndefinedException(detail="项目不存在")
                    data.name = name
                    data.app = app
                    # 如果修改人不是owner或者超管
                    if data.owner != owner and operator_identity < RoleEnum.ADMIN and operator != data.owner:
                        raise SystemException(detail="您没有权限修改项目负责人")
                    data.owner = owner
                    data.private = private
                    data.description = description
                    data.update_date = datetime.now()
                    data.update_emp_no = operator
                    data.dingtalk_url = dingtalk_url
                    data.qy_wx_url = qy_wx_url
        except Exception as e:
            cls.__log__.error(f"编辑项目: {name}失败, {e}")
            raise SystemException(detail=f"编辑项目: {name}失败, {e}")

    @classmethod
    async def query_project(cls, project_id: str) -> (List[ProjectModel], List[ProjectRoleModel]):
        try:
            async with async_session() as session:
                query = await session.execute(
                    select(ProjectModel).where(ProjectModel.id == project_id,
                                               ProjectModel.delete_flag == 0))
                data = query.scalars().first()
                if data is None:
                    raise KeyUndefinedException(detail="项目不存在")
                roles = await ProjectRoleDao.list_role(project_id)
                return data, roles
        except Exception as e:
            cls.__log__.error(f"查询项目: {project_id}失败, {e}")
            raise SystemException(detail=f"查询项目: {project_id}失败, {e}")

    @staticmethod
    async def query_user_project(emp_no: str) -> int:
        """
        查询用户有多少项目
        Args:
            emp_no:

        Returns:

        """
        ans = set()
        async with async_session() as session:
            async with session.begin():
                # 先选出未被删除的用户
                project_sql = select(ProjectModel).where(
                    ProjectModel.delete_flag == 0)
                projects = await session.execute(project_sql)
                project_list = []
                # 将数据放入列表,把owner等于该用户的放入列表
                for r in projects.scalars().all():
                    project_list.append(r.id)
                    if r.owner == emp_no:
                        ans.add(r.id)
                # 接着查询项目角色表有该用户的角色,把角色的项目id放入列表,由于是set,所以不会重复
                query = await session.execute(
                    select(ProjectRoleModel).where(ProjectRoleModel.delete_flag == 0,
                                                   ProjectRoleModel.member_no == emp_no))
                for q in query.scalars().all():
                    ans.add(q.project_id)
        return len(ans)


@PikaMdWrapper(ProjectRoleModel)
class ProjectRoleDao(PikaWrapper):

    @classmethod
    async def list_project_by_user(cls, emp_no: str) -> List[str]:
        """
        通过emp_no获取项目列表
        Args:
            emp_no:

        Returns:

        """
        try:
            async with async_session() as session:
                data = await session.execute(
                    select(ProjectRoleModel.project_id).where(ProjectRoleModel.member_no == emp_no,
                                                              ProjectRoleModel.delete_flag == 0))
                return data.scalars().all()
        except Exception as e:
            cls.__log__.error(f"查询用户: {emp_no}项目失败, {e}")
            raise SystemException(detail="获取项目失败")

    @classmethod
    def query_number_count_by_emp_no(cls, emp_no):
        """
        通过emp_no查询旗下所有的用户数
        Args:
            emp_no:

        Returns:

        """
        return select(func.count(ProjectRoleModel.member_no)) \
            .outerjoin(ProjectModel, and_(ProjectModel.delete_flag == 0,
                                          ProjectModel.id == ProjectRoleModel.project_id)).where(
            or_(ProjectModel.owner == emp_no, ProjectRoleModel.member_no == emp_no)).group_by(
            ProjectRoleModel.project_id)

    @classmethod
    async def list_role(cls, project_id: str) -> List[ProjectRoleModel]:
        try:
            async with async_session() as session:
                query = await session.execute(
                    select(ProjectRoleModel).where(ProjectRoleModel.project_id == project_id,
                                                   ProjectRoleModel.delete_flag == 0))
                return query.scalars().all()
        except Exception as e:
            cls.__log__.error(f"查询项目: {project_id}角色列表失败, {e}")
            raise SystemException(detail="获取项目角色列表失败")

    @classmethod
    async def judge_permission(cls, session: AsyncSession, project_id: str, emp_no: str,
                               project_role: int,
                               project_admin: bool) -> None:
        """
        判断用户是否有某个项目的权限
        Args:
            session:
            project_id:
            emp_no:
            project_role:
            project_admin:

        Returns:

        """
        query = await session.execute(select(ProjectModel).where(ProjectModel.id == project_id))
        project = query.scalars().first()
        if project is None:
            raise KeyUndefinedException(detail="该项目不存在")
        if project.owner != emp_no:
            if project_admin and project_role == RoleEnum.MANAGER:
                raise SystemException(detail="不能修改组长的权限")
            query = await session.execute(select(ProjectRoleModel)
                                          .where(ProjectRoleModel.member_no == emp_no,
                                                 ProjectRoleModel.project_id == project_id,
                                                 ProjectRoleModel.delete_flag == 0))
            updater_role = query.scalars().first()
            if updater_role is None or updater_role.project_role == RoleEnum.MANAGER:
                raise SystemException(detail="对不起,你没有权限")

    @staticmethod
    async def access(operator: str, operator_identity: str, roles: List[ProjectRoleModel],
                     project: ProjectModel = None):
        if operator_identity == RoleEnum.ADMIN or not project.private or operator == project.owner:
            return
        if not any([r.operator == operator for r in roles]):
            raise AuthException(detail="没有权限访问项目")

    @classmethod
    async def read_permission(cls, project_id: str, operator: str, operator_identity: str):
        """
        判断用户是否有读取项目的权限
        Args:
            project_id:
            operator:
            operator_identity:

        Returns:

        """
        if operator_identity == RoleEnum.ADMIN:
            # 超管不需要判断权限
            return
        async with async_session() as session:
            query = await session.execute(
                select(ProjectModel).where(ProjectModel.id == project_id,
                                           ProjectModel.delete_flag == 0))
            project = query.scalars().first()
            if project is None:
                raise KeyUndefinedException(detail="项目不存在")
            if project.private and project.owner != operator:
                query = await session.execute(
                    select(ProjectRoleModel).where(ProjectRoleModel.member_no == operator,
                                                   ProjectRoleModel.project_id == project_id,
                                                   ProjectRoleModel.delete_flag == 0))
                role = query.scalars().first()
                if role is None:
                    raise AuthException(detail="没有权限访问项目")

    @classmethod
    async def has_permission(cls, project_id: str, project_role: int, operator: str,
                             operator_identity: int,
                             project_admin: bool = False, session: AsyncSession = None):
        """
        判断用户是否有该项目的权限
        Args:
            project_id:
            project_role:
            operator:
            operator_identity:
            project_admin:
            session:

        Returns:

        """
        if operator_identity != RoleEnum.ADMIN:
            if session is not None:
                await cls.judge_permission(session, project_id, operator, project_role,
                                           project_admin)
            async with async_session() as session:
                await cls.judge_permission(session, project_id, operator, project_role,
                                           project_admin)

    @classmethod
    async def update_project_role(cls, prole: ProjectRoleEditSchema, operator: str,
                                  operator_identity: int):
        """
        更改用户角色
        Args:
            prole:
            operator:
            operator_identity:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    original = await cls.query_record(session=session, id=prole.id, delete_flag=False)
                    if original is None:
                        raise KeyUndefinedException(detail="该用户角色不存在")
                    await cls.has_permission(original.project_id, original.project_role,
                                             operator,
                                             operator_identity, True, session=session)
                    old = deepcopy(original)
                    changed = cls.update_model(original, prole, operator)
                    await session.flush()
                    session.expunge(original)
                async with session.begin():
                    await asyncio.create_task(
                        cls.insert_log(session=session, operator=operator,
                                       mode=SqlOperationTypeEnum.ONLY_UPDATE.value,
                                       before=old,
                                       changed=changed))
        except Exception as e:
            cls.__log__.error(f"更新用户角色失败: {e}")
            raise SystemException(detail=f"更新用户角色失败: {e}")

    @classmethod
    async def delete_project_role(cls, prole_id: str, operator: str,
                                  operator_identity: int) -> None:
        """
        删除用户角色
        Args:
            prole_id:
            operator:
            operator_identity:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    role = await cls.query_record(session=session, id=prole_id,
                                                  delete_flag=False)
                    if role is None:
                        raise KeyUndefinedException(detail="用户角色不存在")
                    await cls.has_permission(role.project_id, role.project_role, operator,
                                             operator_identity, True)
                    cls.delete_model(role, operator)
                    await session.flush()
                    session.expunge(role)
                async with session.begin():
                    await asyncio.create_task(
                        cls.insert_log(session=session, operator=operator,
                                       mode=SqlOperationTypeEnum.ONLY_DELETE.value, before=role,
                                       key=prole_id))
        except Exception as e:
            cls.__log__.error(f"删除用户角色失败: {e}")
            raise SystemException(detail=f"删除用户角色失败: {e}")
