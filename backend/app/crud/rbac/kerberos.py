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

from sqlalchemy import select, distinct, delete, update, or_, and_

from app.core.handler.asyncsql import AsyncDbSession
from app.core.handler.jsonres import PikaResponse
from app.core.handler.logger import Log
from app.enums.bytesize import ByteSizeEnum
from app.enums.statuscode import SysFailedCodeEnum
from app.models import async_db_session
from app.models.kerberos import SecurityNominateIssue


class KerberosDao(object):
    log = Log("KerberosDao")

    @staticmethod
    async def add_encrypt_issue(**kwargs):
        pending_begin = [{**index, **{"create_emp_no": kwargs["emp_no"]}} for index in
                         [dict(element) for element in kwargs["security"].security]]
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin), max_begin_number=100)
        new_begin_key, new_questions_list = [index["question"] for index in pending_begin], []
        async with async_db_session() as session:
            async with session.begin():
                sql = select(distinct(SecurityNominateIssue.question)).where(
                    SecurityNominateIssue.question.in_(new_begin_key))
                execute_exists_question = await session.execute(sql)
                exists_question = [index[0] for index in [question for question in execute_exists_question.all()]]
                for index in pending_begin:
                    if index.get("question", None) not in exists_question:
                        new_questions_list.append(index)
                if len(new_questions_list) > 0:
                    await session.execute(SecurityNominateIssue.__table__.insert(), new_questions_list)
                elif not new_questions_list:
                    return PikaResponse.failed(code=SysFailedCodeEnum.VAR_ERROR, detail="数据均已存在！",
                                               result={"exists_question": exists_question})
                if not exists_question:
                    return PikaResponse.success()
                elif len(exists_question) > 0 and len(new_questions_list):
                    return PikaResponse.failed(code=SysFailedCodeEnum.VAR_ERROR,
                                               detail=f"部分添加成功！",
                                               result={"exists_question": exists_question})

    @staticmethod
    async def delete_encrypt_issue(**kwargs):
        ids = kwargs["request"].ids.split(",")
        del_sql = delete(SecurityNominateIssue).where(SecurityNominateIssue.id.in_(ids))
        return await AsyncDbSession.delete(ids=ids, do_sql=del_sql)

    @staticmethod
    async def update_encrypt_issue(**kwargs):
        pending_begin, update_emp_no = kwargs["request"].security, kwargs["emp_no"]
        pending_index, dispose_index = 0, 100
        success, failed, not_funded = [], [], []
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin),
                                        max_begin_number=ByteSizeEnum.LENGTH_100)
        floor_count = math.floor(len(pending_begin) / dispose_index)
        pending_count = 1 if floor_count < 1 else floor_count
        async with async_db_session() as session:
            async with session.begin():
                for index in range(pending_count):
                    pending_begin_ = pending_begin[pending_index:dispose_index]
                    pending_index += dispose_index
                    dispose_index += pending_index
                    # 查询是否存在
                    sql = select(distinct(SecurityNominateIssue.id)).where(
                        SecurityNominateIssue.id.in_([index.id for index in pending_begin_]))
                    execute_exists_id = await session.execute(sql)
                    exists_id = [index[0] for index in [id_ for id_ in execute_exists_id.all()]]
                    # 遍历更新
                    for pb in pending_begin_:
                        if pb.id in exists_id:
                            sql = update(SecurityNominateIssue).where(
                                SecurityNominateIssue.id == pb.id).values(
                                {"update_emp_no": update_emp_no, "question": pb.question,
                                 "description": pb.description})
                            try:
                                await session.execute(sql)
                            except Exception as e:
                                failed.append(e)
                            else:
                                success.append(pb)
                        else:
                            not_funded.append(pb)
                if len(failed) <= 0 and len(not_funded) <= 0:
                    return PikaResponse.success(message=f"修改成功！")
                else:
                    if len(success) <= 0 and (len(failed) >= 0 or len(not_funded) >= 0):
                        msg = "修改失败"
                    else:
                        msg = "部分修改成功"
                    return PikaResponse.success(code=SysFailedCodeEnum.MYSQL_ERROR,
                                                message=f'{msg},详情请查阅返回值！',
                                                result={"success": success, "failed": failed, "not_funded": not_funded})

    @staticmethod
    async def query_encrypt_issue(db, request):
        all_do_sql = select(SecurityNominateIssue)
        dim_do_sql = select(SecurityNominateIssue).where(
            or_(SecurityNominateIssue.id == request.id, SecurityNominateIssue.question == request.question,
                SecurityNominateIssue.create_emp_no.like(f"%{request.create_emp_no}%"),
                SecurityNominateIssue.update_emp_no.like(f"%{request.update_emp_no}%"),
                and_(SecurityNominateIssue.create_time >= request.create_time,
                     SecurityNominateIssue.update_time <= request.update_time)
                ))
        return await AsyncDbSession.query(db, str(request.query_type), all_do_sql, dim_do_sql)
