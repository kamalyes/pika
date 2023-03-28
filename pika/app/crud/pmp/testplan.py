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
from copy import deepcopy

from app.core.handler.jsonres import PikaModelEncoder
from app.crud import PikaMdWrapper, PikaWrapper
from app.crud.pmp.project import ProjectDao
from app.enums.OperationEnum import SqlOperationTypeEnum
from app.models import async_session
from app.models.api_test_report import ApiTestReportModel
from app.models.api_testplan import ApiTestPlanModel
from app.models.testplan_follow_user import ApiTestPlanFollowUserRelModel
from app.schema.api_testplan import ApiTestPlanSchema
from custard.time import Moment
from sqlalchemy import and_, null, or_, select


@PikaMdWrapper(ApiTestPlanModel)
class ApiTestPlanDao(PikaWrapper):
    @classmethod
    async def list_test_plan(
        cls,
        paging,
        project_id: str = None,
        name: str = None,
        priority: str = None,
        operator_identity: str = None,
        operator: str = None,
        follow: bool = None,
    ):
        try:
            async with async_session() as session:
                conditions = [ApiTestPlanModel.delete_flag == 0]
                if project_id:
                    ApiTestPlanModel.where(project_id, ApiTestPlanModel.project_id == project_id, conditions)
                else:
                    # 找出用户能看到的项目
                    projects = await ProjectDao.list_project_id_by_user(session, operator, operator_identity)
                    if projects is None:
                        # 说明用户一个项目都没有,不需要继续查询了
                        return [], 0
                    if len(projects) > 0:
                        cls.where(projects, ApiTestPlanModel.project_id.in_(projects), conditions)
                cls.where(name, ApiTestPlanModel.name.like(f"%{name}%"), conditions).where(
                    priority, ApiTestPlanModel.priority == priority, conditions,
                ).where(operator, ApiTestPlanModel.create_emp_no == operator, conditions)
                if follow is None:
                    sql = (
                        select(ApiTestPlanModel, ApiTestPlanFollowUserRelModel.id)
                        .outerjoin(
                            ApiTestPlanFollowUserRelModel,
                            and_(
                                ApiTestPlanFollowUserRelModel.emp_no == operator,
                                ApiTestPlanFollowUserRelModel.delete_flag == 0,
                                ApiTestPlanFollowUserRelModel.plan_id == ApiTestPlanModel.id,
                            ),
                        )
                        .where(*conditions)
                    )
                elif follow:
                    sql = (
                        select(ApiTestPlanModel, ApiTestPlanFollowUserRelModel.id)
                        .outerjoin(
                            ApiTestPlanFollowUserRelModel,
                            ApiTestPlanFollowUserRelModel.plan_id == ApiTestPlanModel.id,
                        )
                        .where(
                            *conditions,
                            ApiTestPlanFollowUserRelModel.emp_no == operator,
                            ApiTestPlanFollowUserRelModel.delete_flag == 0,
                        )
                    )
                else:
                    sql = (
                        select(ApiTestPlanModel, null().label("null_bar"))
                        .outerjoin(
                            ApiTestPlanFollowUserRelModel, ApiTestPlanFollowUserRelModel.plan_id == ApiTestPlanModel.id,
                        )
                        .where(
                            *conditions,
                            or_(
                                ApiTestPlanFollowUserRelModel.id is None, ApiTestPlanFollowUserRelModel.delete_flag == 0,
                            ),
                        )
                    )
                result, total = await cls.pagination(paging.page_index, paging.page_size, session, sql, False)
                return result, total
        except Exception as e:
            err_detail = f"获取测试计划失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def insert_test_plan(cls, plan: ApiTestPlanSchema, operator: str) -> ApiTestPlanModel:
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ApiTestPlanModel).where(
                            ApiTestPlanModel.project_id == plan.project_id,
                            ApiTestPlanModel.name == plan.name,
                            ApiTestPlanModel.delete_flag == 0,
                        ),
                    )
                    if query.scalars().first() is not None:
                        raise Exception("测试计划已存在")
                    test_plan = ApiTestPlanModel(**plan.dict(), operator=operator)
                    session.add(test_plan)
                    await session.flush()
                    await session.refresh(test_plan)
                    session.expunge(test_plan)
                    return test_plan
        except Exception as e:
            err_detail = f"新增测试计划失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def update_test_plan(cls, plan: ApiTestPlanSchema, operator: str, log=True):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ApiTestPlanModel).where(
                            ApiTestPlanModel.id == plan.id, ApiTestPlanModel.delete_flag == 0,
                        ),
                    )
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("测试计划不存在")
                    before = deepcopy(data)
                    plan.env_list = ",".join(map(str, plan.env_list))
                    plan.receiver = ",".join(map(str, plan.receiver))
                    plan.case_list = ",".join(map(str, plan.case_list))
                    plan.msg_type = ",".join(map(str, plan.msg_type))
                    cls.update_model(data, plan, operator)
                    await session.flush()
                    session.expunge(data)
                if log:
                    before_, changed_ = PikaModelEncoder.model_to_dict(before), PikaModelEncoder.model_to_dict(plan)
                    async with session.begin():
                        await asyncio.create_task(
                            cls.insert_log(
                                session,
                                operator=operator,
                                mode=SqlOperationTypeEnum.ONLY_UPDATE,
                                before=before_,
                                changed=changed_,
                            ),
                        )
        except Exception as e:
            err_detail = f"编辑测试计划失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def update_test_plan_state(cls, id: str, state: int):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ApiTestPlanModel).where(ApiTestPlanModel.id == id, ApiTestPlanModel.delete_flag == 0),
                    )
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("测试计划不存在")
                    data.state = state
                    await session.flush()
                    session.expunge(data)
                    return data
        except Exception as e:
            err_detail = f"编辑测试计划失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def query_test_plan(cls, id: str) -> ApiTestPlanModel:
        try:
            async with async_session() as session:
                sql = select(ApiTestPlanModel).where(ApiTestPlanModel.delete_flag == 0, ApiTestPlanModel.id == id)
                data = await session.execute(sql)
                return data.scalars().first()
        except Exception as e:
            err_detail = f"获取测试计划失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def delete_test_plan(cls, id: str, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ApiTestPlanModel).where(ApiTestPlanModel.id == id, ApiTestPlanModel.delete_flag == 0),
                    )
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("测试计划不存在")
                    cls.delete_model(data, operator)
        except Exception as e:
            err_detail = f"删除测试计划失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @staticmethod
    async def follow_test_plan(plan_id: str, operator: str):
        """
        关注测试计划
        Args:
            plan_id:
            operator:

        Returns:

        """
        async with async_session() as session:
            async with session.begin():
                sql = select(ApiTestPlanFollowUserRelModel).where(
                    ApiTestPlanFollowUserRelModel.plan_id == plan_id, ApiTestPlanFollowUserRelModel.emp_no == operator,
                )
                data = await session.execute(sql)
                ans = data.scalars().first()
                if ans is not None:
                    ans.delete_flag = 0
                    ans.delete_date = None
                else:
                    model = ApiTestPlanFollowUserRelModel(plan_id, operator)
                    session.add(model)

    @staticmethod
    async def unfollow_test_plan(plan_id: str, operator: str):
        """
        取关测试计划
        Args:
            plan_id:
            operator:

        Returns:

        """
        async with async_session() as session:
            async with session.begin():
                sql = select(ApiTestPlanFollowUserRelModel).where(
                    ApiTestPlanFollowUserRelModel.delete_flag == 0,
                    ApiTestPlanFollowUserRelModel.plan_id == plan_id,
                    ApiTestPlanFollowUserRelModel.emp_no == operator,
                )
                data = await session.execute(sql)
                ans = data.scalars().first()
                if ans is None:
                    raise Exception("已取关过此测试计划")
                ans.delete_flag = 1
                ans.delete_date = Moment.get_now_time()

    @staticmethod
    async def query_user_follow_test_plan(operator: str):
        """
        根据用户id查询出用户关注的测试计划执行数据
        Args:
            operator:    操作者员工编号

        Returns:

        """
        ans = []
        async with async_session() as session:
            # 找到最近7次通过率
            sql = (
                select(ApiTestPlanModel, ApiTestPlanFollowUserRelModel.id)
                .outerjoin(
                    ApiTestPlanFollowUserRelModel,
                    ApiTestPlanFollowUserRelModel.plan_id == ApiTestPlanModel.id,
                )
                .where(
                    ApiTestPlanFollowUserRelModel.emp_no == operator,
                    ApiTestPlanFollowUserRelModel.delete_flag == 0,
                    ApiTestPlanModel.delete_flag == 0,
                )
            )
            data = await session.execute(sql)
            for d in data.scalars().all():
                reports = []
                query = await session.execute(
                    select(ApiTestReportModel)
                    .where(ApiTestReportModel.plan_id == d.id)
                    .order_by(ApiTestReportModel.start_date.desc())
                    .limit(7),
                )
                for report in query.scalars().all():
                    reports.append(report)
                ans.append(
                    {
                        "plan": d,
                        "report": reports,
                    },
                )
        return ans
