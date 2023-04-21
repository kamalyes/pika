# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_data.py
@Time    :  2022/9/15 11:01
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime
from typing import Optional

class ApiTestCaseResultSchema:
    def __init__(
            self,
            case_id: Optional[str], 
            report_id: Optional[str],
            case_name: Optional[str], 
            status: Optional[int],
            case_log: Optional[str],
            start_date:  Optional[datetime],
            finished_date:  Optional[datetime],
            url: Optional[str],
            request_body: Optional[str],
            request_method: Optional[str],
            request_headers: Optional[str],
            cost: Optional[str],
            asserts: Optional[str],
            response_headers: Optional[str],
            response: Optional[str],
            status_code: Optional[int],
            cookies: Optional[str],
            retry_times: Optional[int]= None ,
            request_params: Optional[str]= None ,
            data_name: Optional[str]= None ,
            data_id: Optional[str]= None):
        self.case_id = case_id
        self.report_id = report_id
        self.case_name = case_name
        self.status = status
        self.case_log = case_log
        self.start_date = start_date
        self.finished_date = finished_date
        self.url = url
        self.request_body = request_body
        self.request_method = request_method
        self.request_headers = request_headers
        self.cost = cost
        self.asserts = asserts
        self.response_headers = response_headers
        self.response = response
        self.status_code = status_code
        self.cookies = cookies
        self.retry_times = retry_times
        self.request_params = request_params
        self.data_name = data_name
        self.data_id = data_id