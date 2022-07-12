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

from sqlalchemy import or_, select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.handler.execres import AuthException, OperationException
from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.enums.OperationEnum import SqlOperationTypeEnum
from app.enums.RbacEnum import RoleEnum
from app.models import async_session, DatabaseHelper
from app.models.project import ProjectModel, ProjectRoleModel
from app.schema.project import ProjectRoleEditForm
from app.utils.decorator import dao


@dao(ProjectModel, PikaLogger("ProjectDao"))
class ProjectDao(PikaMapper):

    @classmethod
    async def list_project(cls, operator_emp_no: str, operator_identity: int, page: int,
                           size: int, name: str = None) -> (List[ProjectModel], int):
        """
        查询/获取项目列表
        Args:
            operator_emp_no:    操作者员工编号
            operator_identity:  操作者身份
            page:   页数
            size:   父页量
            name:   项目名称

        Returns:

        """
        try:
            search = [ProjectModel.is_delete == 0]
            async with async_session() as session:
                if operator_identity != RoleEnum.ADMIN:
                    project_list = await ProjectRoleDao.list_project_by_user(operator_emp_no)
                    # 找出用户能看到的公开项目
                    search.append(
                        or_(ProjectModel.id.in_(project_list), ProjectModel.owner == operator_emp_no,
                            ProjectModel.private is False))
                if name:
                    search.append(ProjectModel.name.like("%{}%".format(name)))
                sql = select(ProjectModel).where(*search).order_by(desc(ProjectModel.update_date))
                data = await session.execute(sql)
                sql = sql.offset((page - 1) * size).limit(size)
                total = data.raw.rowcount
                data = await session.execute(sql)
                return data.scalars().all(), total
        except Exception as e:
            cls.log.error(f"获取用户: {operator_emp_no}项目列表失败, {e}")
            raise Exception(f"获取用户: {operator_emp_no}项目列表失败")

    @classmethod
    async def list_project_id_by_user(cls, session, operator_emp_no, role):
        """
        获取用户可见的项目
        :return:
        """
        if role == RoleEnum.ADMIN:
            return []
        ans = set()
        # 找到包含用户的角色
        sel_role2user = select(ProjectRoleModel.project_id).where(ProjectRoleModel.emp_no == operator_emp_no)
        roles = await session.execute(sel_role2user)
        for r in roles.all():
            ans.add(r[0])
        # 找到未删除的项目
        sel_not_del_dt = select(ProjectModel.id).where(
            or_(ProjectModel.private is False, ProjectModel.owner == operator_emp_no),
            ProjectModel.is_delete == 0)
        roles = await session.execute(sel_not_del_dt)
        for r in roles.all():
            ans.add(r[0])
        return list(ans) if len(ans) > 0 else None

    @classmethod
    async def is_project_admin(cls, session, project_id: int, operator_emp_no: str):
        query = await session.execute(
            select(ProjectModel.owner).where(ProjectModel.id == project_id))
        return query.scalars().first() == operator_emp_no

    @classmethod
    async def add_project(cls, name, app, owner, operator_emp_no, private, description, dingtalk_url='',
                          qy_wx_url=''):
        async with async_session() as session:
            async with session.begin():
                data = await session.execute(
                    select(ProjectModel).where(ProjectModel.name == name,
                                               ProjectModel.is_delete == 0))
                if data.scalars().first() is not None:
                    err = f"新增项目: {name}失败, 失败原因：项目已存在"
                    cls.log.error(err)
                    raise OperationException(detail=err)
                pr = ProjectModel(name, app, owner, operator_emp_no, description, private, dingtalk_url,
                                  qy_wx_url)
                session.add(pr)

    @classmethod
    async def update_avatar(cls, project_id: int, operator_emp_no: str, operator_identity: int, file_url: [str, int]):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ProjectModel).where(ProjectModel.id == project_id,
                                                   ProjectModel.is_delete == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("项目不存在")
                    if data.owner != operator_emp_no and operator_identity < RoleEnum.ADMIN:
                        raise Exception("你没有权限修改项目头像")
                    # 如果修改人不是owner或者超管
                    data.avatar = file_url
                    data.update_date = datetime.now()
                    data.update_user = operator_emp_no
        except Exception as e:
            cls.log.error(f"修改项目头像失败, 项目: {project_id}, error: {e}")
            raise Exception(e)

    @classmethod
    async def update_project(cls, id: int, operator_emp_no, operator_identity: int, name: str, app: str,
                             owner: int,
                             private: bool, description: str,
                             dingtalk_url: str = '', qy_wx_url: str = '') -> None:
        """
        修改项目
        Args:
            id: 项目id
            operator_emp_no: 修改者员工编号
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
                                                   ProjectModel.is_delete == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("项目不存在")
                    data.name = name
                    data.app = app
                    # 如果修改人不是owner或者超管
                    if data.owner != owner and operator_identity < RoleEnum.ADMIN and operator_emp_no != data.owner:
                        raise Exception("您没有权限修改项目负责人")
                    data.owner = owner
                    data.private = private
                    data.description = description
                    data.update_date = datetime.now()
                    data.update_emp_no = operator_emp_no
                    data.dingtalk_url = dingtalk_url
                    data.qy_wx_url = qy_wx_url
        except Exception as e:
            cls.log.error(f"编辑项目: {name}失败, {e}")
            raise Exception(f"编辑项目: {name}失败, {e}")

    @classmethod
    async def query_project(cls, project_id: int) -> (List[ProjectModel], List[ProjectRoleModel]):
        try:
            async with async_session() as session:
                query = await session.execute(
                    select(ProjectModel).where(ProjectModel.id == project_id,
                                               ProjectModel.is_delete == 0))
                data = query.scalars().first()
                if data is None:
                    raise Exception("项目不存在")
                roles = await ProjectRoleDao.list_role(project_id)
                return data, roles
        except Exception as e:
            cls.log.error(f"查询项目: {project_id}失败, {e}")
            raise Exception(f"查询项目: {project_id}失败, {e}")

    @staticmethod
    async def query_user_project(emp_no: int) -> int:
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
                project_sql = select(ProjectModel).where(ProjectModel.is_delete == 0)
                projects = await session.execute(project_sql)
                project_list = []
                # 将数据放入列表，把owner等于该用户的放入列表
                for r in projects.scalars().all():
                    project_list.append(r.id)
                    if r.owner == emp_no:
                        ans.add(r.id)
                # 接着查询项目角色表有该用户的角色，把角色的项目id放入列表
                # 由于是set，所以不会重复
                query = await session.execute(
                    select(ProjectRoleModel).where(ProjectRoleModel.is_delete == 0,
                                                   ProjectRoleModel.emp_no == emp_no))
                for q in query.scalars().all():
                    ans.add(q.project_id)
        return len(ans)


@dao(ProjectRoleModel, PikaLogger("ProjectRoleDao"))
class ProjectRoleDao(PikaMapper):

    @classmethod
    async def list_project_by_user(cls, emp_no: int) -> List[int]:
        """
        通过emp_no获取项目列表
        Args:
            emp_no:

        Returns:

        """
        try:
            async with async_session() as session:
                data = await session.execute(
                    select(ProjectRoleModel.project_id).where(ProjectRoleModel.emp_no == emp_no,
                                                              ProjectRoleModel.is_delete == 0))
                return data.scalars().all()
        except Exception as e:
            cls.log.error(f"查询用户: {emp_no}项目失败, {e}")
            raise Exception("获取项目失败")

    @staticmethod
    async def list_role(project_id: int) -> List[ProjectRoleModel]:
        try:
            async with async_session() as session:
                query = await session.execute(
                    select(ProjectRoleModel).where(ProjectRoleModel.project_id == project_id,
                                                   ProjectRoleModel.is_delete == 0))
                return query.scalars().all()
        except Exception as e:
            ProjectRoleDao.log.error(f"查询项目: {project_id}角色列表失败, {e}")
            raise Exception(f"获取项目角色列表失败")

    @staticmethod
    async def judge_permission(session: AsyncSession, project_id: int, emp_no: str,
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
            raise Exception("该项目不存在")
        if project.owner != emp_no:
            if project_admin and project_role == RoleEnum.MANAGER:
                raise Exception("不能修改组长的权限")
            query = await session.execute(select(ProjectRoleModel)
                                          .where(ProjectRoleModel.emp_no == emp_no,
                                                 ProjectRoleModel.project_id == project_id,
                                                 ProjectRoleModel.is_delete == 0))
            updater_role = query.scalars().first()
            if updater_role is None or updater_role.project_role == RoleEnum.MANAGER:
                raise Exception("对不起，你没有权限")

    @staticmethod
    async def access(operator_emp_no: int, operator_identity: str, roles: List[ProjectRoleModel],
                     project: ProjectModel = None):
        if operator_identity == RoleEnum.ADMIN or not project.private or operator_emp_no == project.owner:
            return
        if not any([r.operator == operator_emp_no for r in roles]):
            raise AuthException(detail="没有权限访问项目")

    @staticmethod
    async def read_permission(project_id: int, operator_emp_no: str, operator_identity: str):
        """
        判断用户是否有读取项目的权限
        Args:
            project_id:
            operator_emp_no:
            operator_identity:

        Returns:

        """
        if operator_identity == RoleEnum.ADMIN:
            # 超管不需要判断权限
            return
        async with async_session() as session:
            query = await session.execute(
                select(ProjectModel).where(ProjectModel.id == project_id,
                                           ProjectModel.is_delete == 0))
            project = query.scalars().first()
            if project is None:
                raise Exception("项目不存在")
            if project.private and project.owner != operator_emp_no:
                query = await session.execute(
                    select(ProjectRoleModel).where(ProjectRoleModel.emp_no == operator_emp_no,
                                                   ProjectRoleModel.project_id == project_id,
                                                   ProjectRoleModel.is_delete == 0))
                role = query.scalars().first()
                if role is None:
                    raise AuthException(detail="没有权限访问项目")

    @staticmethod
    async def has_permission(project_id: int, project_role: int, operator_emp_no: str, operator_identity: int,
                             project_admin: bool = False, session: AsyncSession = None):
        """
        判断用户是否有该项目的权限
        Args:
            project_id:
            project_role:
            operator_emp_no:
            operator_identity:
            project_admin:
            session:

        Returns:

        """
        if operator_identity != RoleEnum.ADMIN:
            if session is not None:
                await ProjectRoleDao.judge_permission(session, project_id, operator_emp_no, project_role,
                                                      project_admin)
            async with async_session() as session:
                await ProjectRoleDao.judge_permission(session, project_id, operator_emp_no, project_role,
                                                      project_admin)

    @classmethod
    async def update_project_role(cls, prole: ProjectRoleEditForm, operator_emp_no: str, operator_identity: int):
        """
        更改用户角色
        Args:
            prole:
            operator_emp_no:
            operator_identity:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    original = await ProjectRoleDao.query_record(session=session, id=prole.id,
                                                                 is_delete=0)
                    if original is None:
                        raise Exception("该用户角色不存在")
                    await ProjectRoleDao.has_permission(original.project_id, original.project_role,
                                                        operator_emp_no,
                                                        operator_identity, True, session=session)
                    old = deepcopy(original)
                    changed = DatabaseHelper.update_model(original, prole, operator_emp_no)
                    await session.flush()
                    session.expunge(original)
                async with session.begin():
                    await asyncio.create_task(
                        ProjectRoleDao.insert_log(session, operator_emp_no, SqlOperationTypeEnum.ONLY_UPDATE,
                                                  original, old,
                                                  prole.id,
                                                  changed=changed))
        except Exception as e:
            cls.log.error(f"更新用户角色失败: {e}")
            raise Exception(f"更新用户角色失败: {e}")

    @staticmethod
    async def delete_project_role(prole_id: int, operator_emp_no: str, operator_identity: int) -> None:
        """
        删除用户角色
        Args:
            prole_id:
            operator_emp_no:
            operator_identity:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    role = await ProjectRoleDao.query_record(session=session, id=prole_id,
                                                             is_delete=0)
                    if role is None:
                        raise Exception("用户角色不存在")
                    await ProjectRoleDao.has_permission(role.project_id, role.project_role,
                                                        operator_emp_no, operator_identity, True)
                    DatabaseHelper.delete_model(role, operator_emp_no)
                    await session.flush()
                    session.expunge(role)
                async with session.begin():
                    await asyncio.create_task(
                        ProjectRoleDao.insert_log(session, operator_emp_no,
                                                  SqlOperationTypeEnum.ONLY_DELETE, role,
                                                  key=prole_id))
        except Exception as e:
            raise Exception(f"删除用户角色失败: {e}")
