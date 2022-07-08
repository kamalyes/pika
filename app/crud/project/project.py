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
from app.enums.gebruikersrol import RoleEnum
from app.enums.operation import SqlOperationTypeEnum
from app.models import async_session, DatabaseHelper
from app.models.project import PikaProject, ProjectRole
from app.schema.project import ProjectRoleEditForm
from app.utils.decorator import dao


@dao(PikaProject, PikaLogger("ProjectDao"))
class ProjectDao(PikaMapper):

    @classmethod
    async def list_project(cls, emp_no: int, role: int, page: int,
                           size: int, name: str = None) -> (List[PikaProject], int):
        """
        查询/获取项目列表
        :param emp_no: 当前用户
        :param role: 当前用户角色
        :param page: 当前页码
        :param size: 当前size
        :param name: 项目名称
        :return: 项目列表和总数
        """
        try:
            search = [PikaProject.is_delete == 0]
            async with async_session() as session:
                if role != RoleEnum.ADMIN:
                    project_list = await ProjectRoleDao.list_project_by_user(emp_no)
                    # 找出用户能看到的公开项目
                    search.append(
                        or_(PikaProject.id.in_(project_list), PikaProject.owner == emp_no,
                            PikaProject.private is False))
                if name:
                    search.append(PikaProject.name.like("%{}%".format(name)))
                sql = select(PikaProject).where(*search).order_by(desc(PikaProject.update_date))
                data = await session.execute(sql)
                sql = sql.offset((page - 1) * size).limit(size)
                total = data.raw.rowcount
                data = await session.execute(sql)
                return data.scalars().all(), total
        except Exception as e:
            cls.log.error(f"获取用户: {emp_no}项目列表失败, {e}")
            raise Exception(f"获取用户: {emp_no}项目列表失败")

    @classmethod
    async def list_project_id_by_user(cls, session, emp_no, role):
        """
        获取用户可见的项目
        :return:
        """
        if role == RoleEnum.ADMIN:
            return []
        ans = set()
        # 找到包含用户的角色
        sel_role2user = select(ProjectRole.project_id).where(ProjectRole.emp_no == emp_no)
        roles = await session.execute(sel_role2user)
        for r in roles.all():
            ans.add(r[0])
        # 找到未删除的项目
        sel_not_del_dt = select(PikaProject.id).where(or_(PikaProject.private is False, PikaProject.owner == emp_no),
                                                      PikaProject.is_delete == 0)
        roles = await session.execute(sel_not_del_dt)
        for r in roles.all():
            ans.add(r[0])
        return list(ans) if len(ans) > 0 else None

    @classmethod
    async def is_project_admin(cls, session, project_id: int, operator: int):
        query = await session.execute(select(PikaProject.owner).where(PikaProject.id == project_id))
        return query.scalars().first() == operator

    @classmethod
    async def add_project(cls, name, app, owner, operator, private, description, avatar, dingtalk_url='', qy_wx_url=''):
        async with async_session() as session:
            async with session.begin():
                data = await session.execute(
                    select(PikaProject).where(PikaProject.name == name, PikaProject.is_delete == 0))
                if data.scalars().first() is not None:
                    err = f"新增项目: {name}失败, 失败原因：项目已存在"
                    cls.log.error(err)
                    raise OperationException(detail=err)
                pr = PikaProject(name, app, owner, operator, description, private, avatar, dingtalk_url, qy_wx_url)
                session.add(pr)

    @classmethod
    async def update_avatar(cls, project_id: int, operator: int, user_role: int, file_url: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(PikaProject).where(PikaProject.id == project_id, PikaProject.is_delete == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("项目不存在")
                    if data.owner != operator and user_role < RoleEnum.ADMIN:
                        raise Exception("你没有权限修改项目头像")
                    # 如果修改人不是owner或者超管
                    data.avatar = file_url
                    data.update_date = datetime.now()
                    data.update_user = operator
        except Exception as e:
            cls.log.error(f"修改项目头像失败, 项目: {project_id}, error: {e}")
            raise Exception(e)

    @classmethod
    async def update_project(cls, id: int, update_emp_no, identity: int, name: str, app: str, owner: int,
                             private: bool, description: str,
                             dingtalk_url: str = '', qy_wx_url: str = '') -> None:
        """
        修改项目
        Args:
            id:
            update_emp_no:
            identity:
            name:
            app:
            owner:
            private:
            description:
            dingtalk_url:
            qy_wx_url:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(PikaProject).where(PikaProject.id == id, PikaProject.is_delete == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("项目不存在")
                    data.name = name
                    data.app = app
                    # 如果修改人不是owner或者超管
                    if data.owner != owner and identity < RoleEnum.ADMIN and update_emp_no != data.owner:
                        raise Exception("您没有权限修改项目负责人")
                    data.owner = owner
                    data.private = private
                    data.description = description
                    data.update_date = datetime.now()
                    data.update_emp_no = update_emp_no
                    data.dingtalk_url = dingtalk_url
                    data.qy_wx_url = qy_wx_url
        except Exception as e:
            cls.log.error(f"编辑项目: {name}失败, {e}")
            raise Exception(f"编辑项目: {name}失败, {e}")

    @classmethod
    async def query_project(cls, project_id: int) -> (List[PikaProject], List[ProjectRole]):
        try:
            async with async_session() as session:
                query = await session.execute(
                    select(PikaProject).where(PikaProject.id == project_id, PikaProject.is_delete == 0))
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
        :param emp_no: 用户id
        :return: 返回项目数量
        """
        ans = set()
        async with async_session() as session:
            async with session.begin():
                # 先选出未被删除的用户
                project_sql = select(PikaProject).where(PikaProject.is_delete == 0)
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
                    select(ProjectRole).where(ProjectRole.is_delete == 0, ProjectRole.emp_no == emp_no))
                for q in query.scalars().all():
                    ans.add(q.project_id)
        return len(ans)


@dao(ProjectRole, PikaLogger("ProjectRoleDao"))
class ProjectRoleDao(PikaMapper):

    @classmethod
    async def list_project_by_user(cls, emp_no: int) -> List[int]:
        """
        通过emp_no获取项目列表
        :param emp_no:
        :return:
        """
        try:
            async with async_session() as session:
                data = await session.execute(
                    select(ProjectRole.project_id).where(ProjectRole.emp_no == emp_no,
                                                         ProjectRole.is_delete == 0))
                return data.scalars().all()
        except Exception as e:
            cls.log.error(f"查询用户: {emp_no}项目失败, {e}")
            raise Exception("获取项目失败")

    @staticmethod
    async def list_role(project_id: int) -> List[ProjectRole]:
        try:
            async with async_session() as session:
                query = await session.execute(
                    select(ProjectRole).where(ProjectRole.project_id == project_id, ProjectRole.is_delete == 0))
                return query.scalars().all()
        except Exception as e:
            ProjectRoleDao.log.error(f"查询项目: {project_id}角色列表失败, {e}")
            raise Exception(f"获取项目角色列表失败")

    @staticmethod
    async def judge_permission(session: AsyncSession, project_id: int, emp_no: int, project_role: int,
                               project_admin: bool) -> None:
        """
        判断用户是否有某个项目的权限
        :param session:
        :param project_id:
        :param emp_no:
        :param project_role:
        :param project_admin: 是否是项目管理员
        :return:
        """
        query = await session.execute(select(PikaProject).where(PikaProject.id == project_id))
        project = query.scalars().first()
        if project is None:
            raise Exception("该项目不存在")
        if project.owner != emp_no:
            if project_admin and project_role == RoleEnum.MANAGER:
                raise Exception("不能修改组长的权限")
            query = await session.execute(select(ProjectRole)
                                          .where(ProjectRole.emp_no == emp_no,
                                                 ProjectRole.project_id == project_id,
                                                 ProjectRole.is_delete == 0))
            updater_role = query.scalars().first()
            if updater_role is None or updater_role.project_role == RoleEnum.MANAGER:
                raise Exception("对不起，你没有权限")

    @staticmethod
    async def access(user: int, user_role: int, roles: List[ProjectRole], project: PikaProject = None):
        if user_role == RoleEnum.ADMIN or not project.private or user == project.owner:
            return
        if not any([r.operator == user for r in roles]):
            raise AuthException(detail="没有权限访问项目")

    @staticmethod
    async def read_permission(project_id: int, emp_no: int, user_role: int):
        """
        判断用户是否有读取项目的权限
        :param user_role:
        :param project_id:
        :param emp_no:
        :return:
        """
        if user_role == RoleEnum.ADMIN:
            # 超管不需要判断权限
            return
        async with async_session() as session:
            query = await session.execute(
                select(PikaProject).where(PikaProject.id == project_id, PikaProject.is_delete == 0))
            project = query.scalars().first()
            if project is None:
                raise Exception("项目不存在")
            if project.private and project.owner != emp_no:
                query = await session.execute(select(ProjectRole).where(ProjectRole.emp_no == emp_no,
                                                                        ProjectRole.project_id == project_id,
                                                                        ProjectRole.is_delete == 0))
                role = query.scalars().first()
                if role is None:
                    raise AuthException(detail="没有权限访问项目")

    @staticmethod
    async def has_permission(project_id: int, project_role: int, emp_no: int, user_role: int,
                             project_admin: bool = False, session: AsyncSession = None):
        """
        判断用户是否有该项目的权限
        :param project_id:
        :param project_role:
        :param emp_no:
        :param user_role:
        :param project_admin:
        :param session:
        :return:
        """
        if user_role != RoleEnum.ADMIN:
            if session is not None:
                await ProjectRoleDao.judge_permission(session, project_id, emp_no, project_role, project_admin)
            async with async_session() as session:
                await ProjectRoleDao.judge_permission(session, project_id, emp_no, project_role, project_admin)

    @classmethod
    async def update_project_role(cls, role: ProjectRoleEditForm, emp_no: int, user_role: int):
        """
        更改用户角色
        :param role:
        :param emp_no:
        :param user_role:
        :return:
        """
        try:
            async with async_session() as session:
                async with session.begin():
                    original = await ProjectRoleDao.query_record(session=session, id=role.id, is_delete=0)
                    if original is None:
                        raise Exception("该用户角色不存在")
                    await ProjectRoleDao.has_permission(original.project_id, original.project_role, emp_no,
                                                        user_role, True, session=session)
                    old = deepcopy(original)
                    changed = DatabaseHelper.update_model(original, role, emp_no)
                    await session.flush()
                    session.expunge(original)
                async with session.begin():
                    await asyncio.create_task(
                        ProjectRoleDao.insert_log(session, emp_no, SqlOperationTypeEnum.ONLY_UPDATE, original, old,
                                                  role.id,
                                                  changed=changed))
        except Exception as e:
            cls.log.error(f"更新用户角色失败: {e}")
            raise Exception(f"更新用户角色失败: {e}")

    @staticmethod
    async def delete_project_role(role_id: int, operator: int, user_role: int) -> None:
        """
        删除用户角色
        :param role_id:
        :param operator:
        :param user_role:
        :return:
        """
        try:
            async with async_session() as session:
                async with session.begin():
                    role = await ProjectRoleDao.query_record(session=session, id=role_id, is_delete=0)
                    if role is None:
                        raise Exception("用户角色不存在")
                    await ProjectRoleDao.has_permission(role.project_id, role.project_role, operator, user_role, True)
                    DatabaseHelper.delete_model(role, operator)
                    await session.flush()
                    session.expunge(role)
                async with session.begin():
                    await asyncio.create_task(
                        ProjectRoleDao.insert_log(session, operator, SqlOperationTypeEnum.ONLY_DELETE, role,
                                                  key=role_id))
        except Exception as e:
            raise Exception(f"删除用户角色失败: {e}")
