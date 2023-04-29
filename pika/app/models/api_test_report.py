# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_test_report.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime
from uuid import uuid4

from sqlalchemy import BOOLEAN, DATETIME, INT, Column, ForeignKey, String
from sqlalchemy.dialects.mysql import SMALLINT

from app.core.handler.sqlbin_uuid import BinaryUUID
from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models import Base
from app.models.api_testplan import ApiTestPlanModel
from app.models.environment import EnvironmentModel


class ApiTestReportModel(Base):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_test_report"
    __table_args__ = {"comment": "测试报告表"}
    id = Column(BinaryUUID, default=uuid4, primary_key=True)
    executor = Column(String(ByteSizeEnum.LENGTH_16), server_default="0", index=True, comment="执行人 0则为CPU")
    env = Column(BinaryUUID, ForeignKey(EnvironmentModel.id, ondelete="cascade", onupdate="cascade"), comment="环境id")
    cost = Column(String(ByteSizeEnum.LENGTH_08), server_default="0", comment="花费时间")
    plan_id = Column(
        BinaryUUID,
        ForeignKey(ApiTestPlanModel.id, ondelete="cascade", onupdate="cascade"),
        nullable=True,
        index=True,
        comment="测试集合id,预留字段",
    )
    start_date = Column(DATETIME, nullable=False, comment="开始时间")
    finished_date = Column(DATETIME, comment="结束时间")
    success_count = Column(INT, nullable=False, server_default="0", comment="成功数量")
    error_count = Column(INT, nullable=False, server_default="0", comment="错误数量")
    failed_count = Column(INT, nullable=False, server_default="0", comment="失败数量")
    skipped_count = Column(INT, nullable=False, server_default="0", comment="跳过数量")
    status = Column(
        SMALLINT,
        nullable=False,
        comment="执行状态 0: pending, 1: running, 2: stopped, 3: finished",
        index=True,
    )
    mode = Column(SMALLINT, server_default="0", comment="case执行模式 0: 普通, 1: 测试集, 2: pipeline, 3: 其他")
    delete_flag = Column(BOOLEAN, server_default="0", comment="删除标识 1:已删除,0:未删除")

    def __init__(
        self,
        executor: str,
        env: str,
        success_count: int = 0,
        failed_count: int = 0,
        error_count: int = 0,
        skipped_count: int = 0,
        status: int = 0,
        mode: int = 0,
        plan_id: str = None,
        finished_date: datetime = None,
        cost=0,
    ):
        self.executor = executor
        self.env = env
        self.start_date = datetime.now()
        self.success_count = success_count
        self.cost = cost
        self.failed_count = failed_count
        self.error_count = error_count
        self.skipped_count = skipped_count
        self.status = status
        self.mode = mode
        self.status = status
        self.plan_id = plan_id
        self.finished_date = finished_date
        self.delete_flag = 0
