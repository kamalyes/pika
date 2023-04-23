import asyncio
import json
import random
import sys
import uuid
from json import JSONDecodeError
from typing import List, Dict

from fastapi import Depends, APIRouter

from app.core.handler.executor import Executor
from app.core.handler.jsonres import PikaResponse
from app.crud.itst.api.testcase_data import ApiTestCaseDataDao
from app.enums.CertEnum import CertType
from app.middleware.async_ask import AsyncRequest
from app.schema.http import HttpRequestSchema
from app.service import Permission

router = APIRouter()

CERT_URL = "http://mitm.it/cert/"


@router.post("/request/http", summary="发起http请求")
async def http_request(data: HttpRequestSchema, user_info=Depends(Permission())):
    r = await AsyncRequest.client(data.url, data.content_type, headers=data.headers,
                                      request_body=data.request_body)
    response = await r.invoke(data.method)
    if response.get("status"):
        return PikaResponse.success(response)
    return PikaResponse.failed(detail=response.get("msg"), data=response)


@router.get("/request/cert", summary="下载proxy证书")
async def http_request(cert: CertType):
    try:
        suffix = cert.get_suffix()
        client = AsyncRequest(CERT_URL + suffix)
        content = await client.download()
        shuffle = list(range(0, 9))
        random.shuffle(shuffle)
        filename = f"{''.join(map(lambda x: str(x), shuffle))}mitmproxy.{suffix}"
        with open(filename, 'wb') as f:
            f.write(content)
        return PikaResponse.file(filename, f"mitmproxy.{suffix}")
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/request/run", summary="执行用例")
async def execute_case(env: str, case_id: str, user_info=Depends(Permission())):
    try:
        executor = Executor()
        test_data = await ApiTestCaseDataDao.list_testcase_data_by_env(env, case_id)
        ans = dict()
        if not test_data:
            result, _ = await executor.run(env, case_id)
            ans["默认数据"] = result
        else:
            for data in test_data:
                params = json.loads(data.json_data)
                result, _ = await executor.run(env, case_id, request_param=params)
                ans[data.name] = result
        return PikaResponse.success(ans)
    except JSONDecodeError:
        return PikaResponse.failed(detail="测试数据不为合法的JSON")
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/request/retry", summary="根据测试数据重新运行测试用例")
async def re_run_case(env:str, case_id:str, data_id:str, retry_id:str, report_id:str, user_info=Depends(Permission())):
    try:
        executor = Executor()
        params = dict()
        test_data = await ApiTestCaseDataDao.query_record(id=data_id)
        if test_data is not None:
            params = json.loads(test_data.json_data)
        result = await executor.run_with_test_data(env=env, case_id=case_id, report_id=report_id, request_param=params, retry_id=retry_id)
        return PikaResponse.success(result)
    except JSONDecodeError:
        return PikaResponse.failed(detail="测试数据不为合法的JSON")


@router.post("/request/run/async", summary="异步执行用例")
async def execute_case(env: str, case_id: List[str], user_info=Depends(Permission())):
    data = dict()
    # s = time.perf_counter()
    await asyncio.gather(*(run_single(env, c, data) for c in case_id))
    # elapsed = time.perf_counter() - s
    # print(f"async executed in {elapsed:0.2f} seconds.")
    return PikaResponse.success()


@router.post("/request/run/sync", summary="同步执行用例")
async def execute_case(env: str, case_id: List[str], user_info=Depends(Permission())):
    data = dict()
    task_id = uuid.uuid5(uuid.NAMESPACE_URL, "task")
    # s = time.perf_counter()
    for c in case_id:
        executor = Executor()
        data[c] = await executor.run(env, c)
    # elapsed = time.perf_counter() - s
    # print(f"sync executed in {elapsed:0.2f} seconds.")
    return PikaResponse.success(data)


@router.post("/request/run/multiple", summary="作为报告执行")
async def execute_as_report(env: str, case_id: List[str], user_info=Depends(Permission())):
    report_id = await Executor.run_multiple(user_info['emp_no'], env, case_id)
    return PikaResponse.success(report_id)
    # task = asyncio.create_task(Executor.run_multiple(user_info['id'], env, case_id))
    # random_id = uuid.uuid5(uuid.NAMESPACE_URL, "task")
    # random_dict[random_id] = task
    # return PikaResponse.success(data=random_id, msg="任务正在后台运行中, 请静静等待🎉")


# @router.post("/cancel")
# async def execute_as_report(random_id: str, user_info=Depends(Permission())):
#     if not random_dict.get(random_id):
#         return PikaResponse.failed("未找到该任务, 可能已结束")
#     task = random_dict.pop(random_id)
#     # 取消任务
#     task.cancel()
#     return PikaResponse.success(data=random_id, msg="操作已停止")


async def run_single(env: str, case_id: str, data: Dict[int, tuple]):
    executor = Executor()
    data[case_id] = await executor.run(env, case_id)
