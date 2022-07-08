# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testplan.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import asyncio
import time
from copy import deepcopy

from sqlalchemy import select, and_, or_, null

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.crud.project.project import ProjectDao
from app.enums.operation import SqlOperationTypeEnum
from app.models import async_session, DatabaseHelper
from app.models.test_plan import PikaTestPlan
from app.models.test_report import PikaTestReport
from app.models.testplan_follow_user import PikaTestPlanFollowUserRel
from app.schema.test_plan import PikaTestPlanForm
from app.utils.decorator import dao


@dao(PikaTestPlan, PikaLogger("PikaTestPlanDao"))
class PikaTestPlanDao(PikaMapper):

    @staticmethod
    async def list_test_plan(page: int, size: int, project_id: int = None, name: str = '', priority: str = '',
                             role: str = None, operator: int = None,
                             emp_no: int = None, follow: bool = None):
        try:
            async with async_session() as session:
                conditions = [PikaTestPlan.is_delete == 0]
                if project_id:
                    DatabaseHelper.where(project_id, PikaTestPlan.project_id == project_id, conditions)
                else:
                    # 找出用户能看到的项目
                    projects = await ProjectDao.list_project_id_by_user(session, operator, role)
                    if projects is None:
                        # 说明用户一个项目都没有，不需要继续查询了
                        return [], 0
                    if len(projects) > 0:
                        DatabaseHelper.where(projects, PikaTestPlan.project_id.in_(projects), conditions)
                DatabaseHelper.where(name, PikaTestPlan.name.like(f"%{name}%"), conditions) \
                    .where(priority, PikaTestPlan.priority == priority, conditions) \
                    .where(operator, PikaTestPlan.operator == operator, conditions)
                if follow is None:
                    sql = select(PikaTestPlan, PikaTestPlanFollowUserRel.id) \
                        .outerjoin(PikaTestPlanFollowUserRel,
                                   and_(
                                       PikaTestPlanFollowUserRel.operator == operator,
                                       PikaTestPlanFollowUserRel.is_delete == 0,
                                       PikaTestPlanFollowUserRel.plan_id == PikaTestPlan.id)) \
                        .where(*conditions)
                elif follow:
                    sql = select(PikaTestPlan, PikaTestPlanFollowUserRel.id) \
                        .outerjoin(PikaTestPlanFollowUserRel,
                                   PikaTestPlanFollowUserRel.plan_id == PikaTestPlan.id,
                                   ).where(
                        *conditions, PikaTestPlanFollowUserRel.operator == operator,
                                     PikaTestPlanFollowUserRel.is_delete == 0)
                else:
                    sql = select(PikaTestPlan, null().label('null_bar')) \
                        .outerjoin(PikaTestPlanFollowUserRel,
                                   PikaTestPlanFollowUserRel.plan_id == PikaTestPlan.id).where(
                        *conditions, or_(PikaTestPlanFollowUserRel.id == None,
                                         PikaTestPlanFollowUserRel.delete_date != 0))
                result, total = await DatabaseHelper.pagination(page, size, session, sql, False)
                return result, total
        except Exception as e:
            PikaTestPlanDao.log.error(f"获取测试计划失败: {str(e)}")
            raise Exception(f"获取测试计划失败: {str(e)}")

    @staticmethod
    async def insert_test_plan(plan: PikaTestPlanForm, user: int) -> PikaTestPlan:
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(select(PikaTestPlan).where(PikaTestPlan.project_id == plan.project_id,
                                                                             PikaTestPlan.name == plan.name,
                                                                             PikaTestPlan.is_delete == 0))
                    if query.scalars().first() is not None:
                        raise Exception("测试计划已存在")
                    test_plan = PikaTestPlan(**plan.dict(), user=user)
                    session.add(test_plan)
                    await session.flush()
                    await session.refresh(test_plan)
                    session.expunge(test_plan)
                    return test_plan
        except Exception as e:
            PikaTestPlanDao.log.error(f"新增测试计划失败: {str(e)}")
            raise Exception(f"添加失败: {str(e)}")

    @classmethod
    async def update_test_plan(cls, plan: PikaTestPlanForm, user: int, log=False):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(PikaTestPlan).where(PikaTestPlan.id == plan.id, PikaTestPlan.is_delete == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("测试计划不存在")
                    old = deepcopy(data)
                    plan.env = ",".join(map(str, plan.env))
                    plan.receiver = ",".join(map(str, plan.receiver))
                    plan.case_list = ",".join(map(str, plan.case_list))
                    plan.msg_type = ",".join(map(str, plan.msg_type))
                    changed = DatabaseHelper.update_model(data, plan, user)
                    await session.flush()
                    session.expunge(data)
                if log:
                    async with session.begin():
                        await asyncio.create_task(
                            cls.insert_log(session, user, SqlOperationTypeEnum.ONLY_UPDATE, data, old, plan.id,
                                           changed))
        except Exception as e:
            PikaTestPlanDao.log.exception(f"编辑测试计划失败: {str(e)}")
            PikaTestPlanDao.log.error(f"编辑测试计划失败: {str(e)}")
            raise Exception(f"编辑失败: {str(e)}")

    @staticmethod
    async def update_test_plan_state(id: int, state: int):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(PikaTestPlan).where(PikaTestPlan.id == id, PikaTestPlan.is_delete == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("测试计划不存在")
                    data.state = state
                    # await session.flush()
                    # session.expunge(data)
                    # return data
        except Exception as e:
            PikaTestPlanDao.log.error(f"编辑测试计划失败: {str(e)}")
            raise Exception(f"编辑失败: {str(e)}")

    @staticmethod
    async def query_test_plan(id: int) -> PikaTestPlan:
        try:
            async with async_session() as session:
                sql = select(PikaTestPlan).where(PikaTestPlan.is_delete == 0, PikaTestPlan.id == id)
                data = await session.execute(sql)
                return data.scalars().first()
        except Exception as e:
            PikaTestPlanDao.log.error(f"获取测试计划失败: {str(e)}")
            raise Exception(f"获取测试计划失败: {str(e)}")

    # @staticmethod
    # async def delete_test_plan(id: int, user: int):
    #     try:
    #         async with async_session() as session:
    #             async with session.begin():
    #                 query = await session.execute(
    #                     select(PikaTestPlan).where(PikaTestPlan.id == id, PikaTestPlan.is_delete == 0))
    #                 data = query.scalars().first()
    #                 if data is None:
    #                     raise Exception("测试计划不存在")
    #                 DatabaseHelper.delete_model(data, user)
    #     except Exception as e:
    #         PikaTestPlanDao.log.error(f"删除测试计划失败: {str(e)}")
    #         raise Exception(f"删除失败: {str(e)}")

    @staticmethod
    async def follow_test_plan(plan_id: int, operator: int):
        """
        关注测试计划
        :param plan_id:
        :param operator:
        :return:
        """
        async with async_session() as session:
            async with session.begin():
                sql = select(PikaTestPlanFollowUserRel).where(PikaTestPlanFollowUserRel.is_delete == 0,
                                                              PikaTestPlanFollowUserRel.plan_id == plan_id,
                                                              PikaTestPlanFollowUserRel.operator == operator)
                data = await session.execute(sql)
                ans = data.scalars().first()
                if ans is not None:
                    raise Exception("已关注过此测试计划")
                model = PikaTestPlanFollowUserRel(plan_id, operator, operator)
                session.add(model)

    @staticmethod
    async def unfollow_test_plan(plan_id: int, operator: int):
        """
        取关测试计划
        :param plan_id:
        :param operator:
        :return:
        """
        async with async_session() as session:
            async with session.begin():
                sql = select(PikaTestPlanFollowUserRel).where(PikaTestPlanFollowUserRel.is_delete == 0,
                                                              PikaTestPlanFollowUserRel.plan_id == plan_id,
                                                              PikaTestPlanFollowUserRel.operator == operator)
                data = await session.execute(sql)
                ans = data.scalars().first()
                if ans is None:
                    raise Exception("已取关过此测试计划")
                ans.delete_date = int(time.time() * 1000)

    @staticmethod
    async def query_user_follow_test_plan(operator: int):
        """
        根据用户id查询出用户关注的测试计划执行数据
        :param operator:
        :return:
        """
        ans = []
        async with async_session() as session:
            # 找到最近7次通过率
            sql = select(PikaTestPlan, PikaTestPlanFollowUserRel.id) \
                .outerjoin(PikaTestPlanFollowUserRel,
                           PikaTestPlanFollowUserRel.plan_id == PikaTestPlan.id,
                           ).where(
                PikaTestPlanFollowUserRel.emp_no == operator,
                PikaTestPlanFollowUserRel.is_delete == 0,
                PikaTestPlan.is_delete == 0)
            data = await session.execute(sql)
            for d in data.scalars().all():
                reports = list()
                query = await session.execute(select(PikaTestReport).where(PikaTestReport.plan_id == d.id).order_by(
                    PikaTestReport.start_at.desc()).limit(7))
                for report in query.scalars().all():
                    reports.append(report)
                ans.append({
                    "plan": d,
                    "report": reports,
                })
        return ans
