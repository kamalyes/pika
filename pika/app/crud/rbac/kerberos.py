# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  kerberos.py
@Time    :  2022/5/3 3:52 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import math

from sqlalchemy import and_, delete, distinct, or_, select, update

from app.core.handler.asyncsql import AsyncDbSession
from app.core.handler.jsonres import PikaResponse
from app.core.handler.logger import PikaLogger
from app.crud import PikaWrapper
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysCodeEnum import ExcCodeEnum
from app.models import async_db_session_generator
from app.models.kerberos import SecurityNominateIssueModel


class KerberosDao(PikaWrapper):
    log = PikaLogger("KerberosDao")

    @staticmethod
    async def add_encrypt_issue(**kwargs):
        pending_begin = [
            {**index, **{"create_emp_no": kwargs["emp_no"]}}
            for index in [dict(element) for element in kwargs["security"].security]
        ]
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin), max_begin_number=100)
        new_begin_key, new_questions_list = [index["question"] for index in pending_begin], []
        async with async_db_session_generator() as session:
            async with session.begin():
                sql = select(distinct(SecurityNominateIssueModel.question)).where(
                    SecurityNominateIssueModel.question.in_(new_begin_key),
                )
                execute_exists_question = await session.execute(sql)
                exists_question = [index[0] for index in list(execute_exists_question.all())]
                for index in pending_begin:
                    if index.get("question", None) not in exists_question:
                        new_questions_list.append(index)
                if len(new_questions_list) > 0:
                    await session.execute(SecurityNominateIssueModel.__table__.insert(), new_questions_list)
                elif not new_questions_list:
                    return PikaResponse.failed(
                        code=ExcCodeEnum.VAR_ERROR, detail="数据均已存在!", data={"exists_question": exists_question},
                    )
                if not exists_question:
                    return PikaResponse.success()
                elif len(exists_question) > 0 and len(new_questions_list):
                    return PikaResponse.failed(
                        code=ExcCodeEnum.VAR_ERROR, detail="部分添加成功!", data={"exists_question": exists_question},
                    )
                return None

    @staticmethod
    async def delete_encrypt_issue(**kwargs):
        ids = kwargs["request"].ids.split(",")
        del_sql = delete(SecurityNominateIssueModel).where(SecurityNominateIssueModel.id.in_(ids))
        return await AsyncDbSession.delete(ids=ids, do_sql=del_sql)

    @staticmethod
    async def update_encrypt_issue(**kwargs):
        pending_begin, update_emp_no = kwargs["request"].security, kwargs["emp_no"]
        pending_index, dispose_index = 0, 100
        success, failed, not_funded = [], [], []
        await AsyncDbSession.begin_lock(
            pending_begin_number=len(pending_begin), max_begin_number=ByteSizeEnum.LENGTH_100,
        )
        floor_count = math.floor(len(pending_begin) / dispose_index)
        pending_count = 1 if floor_count < 1 else floor_count
        async with async_db_session_generator() as session:
            async with session.begin():
                for index in range(pending_count):
                    pending_begin_ = pending_begin[pending_index:dispose_index]
                    pending_index += dispose_index
                    dispose_index += pending_index
                    # 查询是否存在
                    sql = select(distinct(SecurityNominateIssueModel.id)).where(
                        SecurityNominateIssueModel.id.in_([index.id for index in pending_begin_]),
                    )
                    execute_exists_id = await session.execute(sql)
                    exists_id = [index[0] for index in list(execute_exists_id.all())]
                    # 遍历更新
                    for pb in pending_begin_:
                        if pb.id in exists_id:
                            sql = (
                                update(SecurityNominateIssueModel)
                                .where(SecurityNominateIssueModel.id == pb.id)
                                .values(
                                    {
                                        "update_emp_no": update_emp_no,
                                        "question": pb.question,
                                        "description": pb.description,
                                    },
                                )
                            )
                            try:
                                await session.execute(sql)
                            except Exception as e:
                                failed.append(e)
                            else:
                                success.append(pb)
                        else:
                            not_funded.append(pb)
                if len(failed) <= 0 and len(not_funded) <= 0:
                    return PikaResponse.success(message="修改成功!")
                else:
                    if len(success) <= 0 and (len(failed) >= 0 or len(not_funded) >= 0):
                        msg = "修改失败"
                    else:
                        msg = "部分修改成功"
                    return PikaResponse.success(
                        code=ExcCodeEnum.SQL_OPERATION_ERROR,
                        message=f"{msg},详情请查阅返回值!",
                        data={"success": success, "failed": failed, "not_funded": not_funded},
                    )

    @staticmethod
    async def query_encrypt_issue(db, request):
        all_do_sql = select(SecurityNominateIssueModel)
        dim_do_sql = select(SecurityNominateIssueModel).where(
            or_(
                SecurityNominateIssueModel.id == request.id,
                SecurityNominateIssueModel.question == request.question,
                SecurityNominateIssueModel.create_emp_no.like(f"%{request.create_emp_no}%"),
                SecurityNominateIssueModel.update_emp_no.like(f"%{request.update_emp_no}%"),
                and_(
                    SecurityNominateIssueModel.create_date >= request.create_date,
                    SecurityNominateIssueModel.update_date <= request.update_date,
                ),
            ),
        )
        do_sql = all_do_sql if request.query_type == 0 else dim_do_sql
        return await AsyncDbSession.query(db, do_sql)
