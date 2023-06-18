# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  jmeter.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import APIRouter, Depends
from app.core.handler.jsonres import PikaResponse
from app.models import async_db_session_iterator
from app.service import Permission
from app.utils.ws_manager import ws_manage
from app.schema.jmeter import (
    JmeterBatchNoSchema,
    JmeterLatestBuildSchema,
    JmeterChartDataSchema,
    JmeterSummarySchema,
    JmeterUploadResultSchema,
)
from app.crud.itst.api.jmeter import JmeterDao

router = APIRouter()


@router.post("/upload_result", summary="上传报告")
async def upload_result(request: JmeterUploadResultSchema):
    await JmeterDao.upload_result(request)
    return PikaResponse.success()



@router.get("/base_info", summary="查询基础信息")
async def query_base_info(user_info=Depends(Permission()), session=Depends(async_db_session_iterator)):
    data = await JmeterDao.query_base_info()
    return PikaResponse.success(data=data)


@router.get("/latest_build", summary="最新构建")
async def query_latest_build(
    request: JmeterLatestBuildSchema = Depends(),
    user_info=Depends(Permission()),
    session=Depends(async_db_session_iterator),
):
    # TODO document why this method is empty
    pass


@router.get("/chart_data", summary="查询图表数据")
async def query_chart_data(
    request: JmeterChartDataSchema = Depends(),
    user_info=Depends(Permission()),
    session=Depends(async_db_session_iterator),
):
    # TODO document why this method is empty
    pass


@router.get("/summary_list", summary="查询构建信息列表")
async def query_summary_list(
    request: JmeterSummarySchema = Depends(),
    user_info=Depends(Permission()),
    session=Depends(async_db_session_iterator),
):
    # TODO document why this method is empty
    pass


@router.get("/case_detail", summary="查询测试详情")
async def query_case_detail(
    request: JmeterBatchNoSchema = Depends(),
    user_info=Depends(Permission()),
    session=Depends(async_db_session_iterator),
):
    # TODO document why this method is empty
    pass
