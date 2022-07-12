import json
from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, UploadFile, File, Request

from app.core.handler.execres import AuthException
from app.core.handler.jsonres import PikaResponse
from app.core.request import get_convertor
from app.core.request.generator import CaseGenerator
from app.crud.itst.api.constructor import ConstructorDao
from app.crud.itst.api.testcase import ApiTestCaseDao
from app.crud.itst.api.testcase_assert import ApiTestCaseAssertsDao
from app.crud.itst.api.testcase_data import ApiTestCaseDataDao
from app.crud.itst.api.testcase_directory import ApiTestCaseDirectoryDao
from app.crud.itst.api.testcase_out_params import ApiTestCaseOutParametersDao
from app.crud.itst.api.testreport import ApiTestReportDao
from app.crud.project.project import ProjectRoleDao
from app.enums.ConvertorEnum import CaseConvertorTypeEnum
from app.middleware.xredis import RedisHelper
from app.models import get_async_session
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.schema.api_testcase import TestCaseAssertsForm, TestCaseForm, TestCaseInfo, \
    TestCaseGeneratorForm
from app.schema.api_testcase_data import ApiTestCaseDataForm
from app.schema.api_testcase_directory import ApiTestCaseDirectoryForm, MoveApiTestCaseFrom
from app.schema.api_testcase_out_parameters import ApiTestCaseOutParametersForm
from app.schema.constructor import ConstructorForm, ConstructorIndex
from app.service import Permission

router = APIRouter()


@router.get("/list", summary="用例列表查询")
async def list_testcase(directory_id: int = None, name: str = "", operator: str = ''):
    data = await ApiTestCaseDao.list_testcase(directory_id, name, operator)
    return PikaResponse.success(data=data)


@router.post("/insert", summary="新增接口用例")
async def insert_testcase(data: TestCaseForm, user_info=Depends(Permission())):
    try:
        record = await ApiTestCaseDao.query_record(name=data.name, directory_id=data.directory_id)
        if record is not None:
            return PikaResponse.failed(detail="用例已存在")
        model = ApiTestCaseModel(**data.dict(), operator=user_info['emp_no'])
        model = await ApiTestCaseDao.insert_record(model, True)
        return PikaResponse.success(data=model.id)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


# v2版本创建用例接口
@router.post("/create", summary="创建接口测试用例")
async def create_testcase(data: TestCaseInfo, user_info=Depends(Permission()),
                          session=Depends(get_async_session)):
    async with session.begin():
        await ApiTestCaseDao.insert_test_case(session, data, user_info['emp_no'])
    return PikaResponse.success()


@router.post("/update")
async def update_testcase(form: TestCaseForm, user_info=Depends(Permission())):
    try:
        data = await ApiTestCaseDao.update_test_case(form, user_info['emp_no'])
        result = await ApiTestCaseOutParametersDao.update_many(form.id, form.out_parameters,
                                                               user_info['emp_no'])
        return PikaResponse.success(data=dict(case_info=data, out_parameters=result))
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.delete("/delete", summary="删除测试用例")
async def delete_testcase(id_list: List[int], user_info=Depends(Permission()),
                          session=Depends(get_async_session)):
    try:
        # 删除case
        async with session.begin():
            await ApiTestCaseDao.delete_records(session, user_info['emp_no'], id_list)
            # 删除断言
            await ApiTestCaseAssertsDao.delete_records(session, user_info['emp_no'], id_list,
                                                       column="case_id")
            # 删除测试数据
            await ApiTestCaseDataDao.delete_records(session, user_info['emp_no'], id_list,
                                                    column="case_id")
            return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/query")
async def query_testcase(caseId: int, _=Depends(Permission())):
    try:
        data = await ApiTestCaseDao.query_test_case(caseId)
        return PikaResponse.success(data=PikaResponse.dict_model_to_dict(data))
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


# @router.get("/list")
# async def query_testcase(user_info=Depends(Permission())):
#     try:
#         projects, _, _ = ProjectDao.list_project(user_info["role"], user_info["emp_no"], 1, 2000)
#         data = ApiTestCaseDao.list_testcase_tree(projects)
#         return dict(code=0, data=data, msg="操作成功")
#     except Exception as e:
#         return dict(code=110, msg=str(e))


@router.post("/asserts/insert")
async def insert_testcase_asserts(data: TestCaseAssertsForm, user_info=Depends(Permission())):
    try:
        new_assert = await ApiTestCaseAssertsDao.insert_test_case_asserts(data, operator_emp_no=user_info["emp_no"])
        return PikaResponse.success(data=new_assert)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/asserts/update")
async def insert_testcase_asserts(data: TestCaseAssertsForm, user_info=Depends(Permission())):
    try:
        updated = await ApiTestCaseAssertsDao.update_test_case_asserts(data, operator_emp_no=user_info["emp_no"])
        return PikaResponse.success(data=updated)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/asserts/delete")
async def delete_test_case_asserts(id: int, user_info=Depends(Permission())):
    await ApiTestCaseAssertsDao.delete_test_case_asserts(id, operator_emp_no=user_info["emp_no"])
    return PikaResponse.success()


@router.post("/constructor/insert")
async def insert_constructor(data: ConstructorForm, user_info=Depends(Permission())):
    await ConstructorDao.insert_constructor(data, operator_emp_no=user_info["emp_no"])
    return PikaResponse.success()


@router.post("/constructor/update")
async def update_constructor(data: ConstructorForm, user_info=Depends(Permission())):
    await ConstructorDao.update_constructor(data, operator_emp_no=user_info["emp_no"])
    return PikaResponse.success()


@router.get("/constructor/delete")
async def update_constructor(id: int, user_info=Depends(Permission())):
    await ConstructorDao.delete_constructor(id, operator_emp_no=user_info["emp_no"])
    return PikaResponse.success()


@router.post("/constructor/order")
async def update_constructor_index(data: List[ConstructorIndex], user_info=Depends(Permission())):
    await ConstructorDao.update_constructor_index(data)
    return PikaResponse.success()


@router.get("/constructor/tree")
async def get_constructor_tree(suffix: bool, name: str = "", user_info=Depends(Permission())):
    result = await ConstructorDao.get_constructor_tree(name, suffix)
    return PikaResponse.success(data=result)


@router.get("/constructor")
async def get_constructor_tree(id: int, user_info=Depends(Permission())):
    """
    获取数据构造器树
    Args:
        id:
        user_info:

    Returns:

    """
    result = await ConstructorDao.get_constructor_data(id)
    return PikaResponse.success(data=result)


@router.get("/constructor/list")
async def list_case_and_constructor(constructor_type: int, suffix: bool):
    """
    获取所有数据构造器
    Args:
        constructor_type:
        suffix:

    Returns:

    """
    ans = await ConstructorDao.get_case_and_constructor(constructor_type, suffix)
    return PikaResponse.success(ans)


@router.get("/report")
async def query_report(id: int, user_info=Depends(Permission())):
    """
    根据id查询具体报告内容
    Args:
        id:
        user_info:

    Returns:

    """
    report, case_list, plan_name = await ApiTestReportDao.query(id)
    return PikaResponse.success(data=dict(report=report, plan_name=plan_name, case_list=case_list))


# 获取构建历史记录
@router.get("/report/list")
async def list_report(page: int, size: int, start_time: str, end_time: str, executor: int = None,
                      _=Depends(Permission())):
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    report_list, total = await ApiTestReportDao.list_report(page, size, start, end, executor)
    return PikaResponse.success_with_size(data=report_list, total=total)


# 获取脑图数据
@router.get("/xmind")
async def get_xmind_data(case_id: int, user_info=Depends(Permission())):
    tree_data = await ApiTestCaseDao.get_xmind_data(case_id)
    return PikaResponse.success(data=tree_data)


# 获取case目录
@router.get("/directory")
async def get_testcase_directory(project_id: int, move: bool = False,
                                 user_info=Depends(Permission())):
    # 如果是move，则不需要禁用树
    tree_data, _ = await ApiTestCaseDirectoryDao.get_directory_tree(project_id, move=move)
    return PikaResponse.success(data=tree_data)


@router.get("/tree")
async def get_directory_and_case(project_id: int, user_info=Depends(Permission())):
    """
    获取case目录+case
    Args:
        project_id:
        user_info:

    Returns:

    """
    try:
        directory_tree_map = {"project_id": project_id, "case_node": ApiTestCaseDao.get_test_case_by_directory_id}
        tree_data, cs_map = await ApiTestCaseDirectoryDao.get_directory_tree(**directory_tree_map)
        return PikaResponse.success(data=dict(tree=tree_data, case_map=cs_map))
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/directory/query")
async def query_testcase_directory(directory_id: int, escarole=Depends(Permission(escarole=True))):
    operator_emp_no, operator_identity = escarole
    try:
        data = await ApiTestCaseDirectoryDao.query_directory(directory_id)
        await ProjectRoleDao.read_permission(data.project_id, operator_emp_no, operator_identity)
        return PikaResponse.success(data=data)
    except AuthException:
        return PikaResponse.forbidden()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/directory/insert")
async def insert_testcase_directory(form: ApiTestCaseDirectoryForm,
                                    user_info=Depends(Permission())):
    try:
        await ApiTestCaseDirectoryDao.insert_directory(form, user_info['emp_no'])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/directory/update")
async def insert_testcase_directory(form: ApiTestCaseDirectoryForm,
                                    user_info=Depends(Permission())):
    try:
        await ApiTestCaseDirectoryDao.update_directory(form, user_info['emp_no'])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/directory/delete")
async def insert_testcase_directory(id: int, user_info=Depends(Permission())):
    try:
        await ApiTestCaseDirectoryDao.delete_directory(id, user_info['emp_no'])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/data/insert")
async def insert_testcase_data(form: ApiTestCaseDataForm, user_info=Depends(Permission())):
    try:
        data = await ApiTestCaseDataDao.insert_testcase_data(form, user_info['emp_no'])
        return PikaResponse.success(data=data)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/data/update")
async def update_testcase_data(form: ApiTestCaseDataForm, user_info=Depends(Permission())):
    try:
        data = await ApiTestCaseDataDao.update_testcase_data(form, user_info['emp_no'])
        return PikaResponse.success(data=data)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/data/delete")
async def delete_testcase_data(id: int, user_info=Depends(Permission())):
    try:
        await ApiTestCaseDataDao.delete_testcase_data(id, user_info['emp_no'])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/move", summary="移动case到其他目录")
async def move_testcase(form: MoveApiTestCaseFrom, escarole=Depends(Permission(escarole=True))):
    try:
        # 判断是否有移动case的权限
        operator_emp_no, operator_identity = escarole
        await ProjectRoleDao.read_permission(form.project_id, operator_emp_no, operator_identity)
        await ApiTestCaseDao.update_by_map(operator_emp_no,
                                           ApiTestCaseModel.id.in_(form.id_list),
                                           directory_id=form.directory_id)
        return PikaResponse.success()
    except AuthException:
        return PikaResponse.forbidden()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/parameters/insert")
async def insert_testcase_out_parameters(form: ApiTestCaseOutParametersForm,
                                         user_info=Depends(Permission())):
    query = await ApiTestCaseOutParametersDao.query_record(name=form.name, case_id=form.case_id)
    if query is not None:
        return PikaResponse.failed(detail="参数名称已存在")
    data = ApiTestCaseOutParametersModel(**form.dict(), operator=user_info['emp_no'])
    data = await ApiTestCaseOutParametersDao.insert_record(data)
    return PikaResponse.success(data=data)


@router.post("/parameters/update/batch", summary="批量更新出参数据")
async def update_batch_testcase_out_parameters(case_id: int,
                                               form: List[ApiTestCaseOutParametersForm],
                                               user_info=Depends(Permission())):
    result = await ApiTestCaseOutParametersDao.update_many(case_id, form, user_info['emp_no'])
    return PikaResponse.success(data=result)


@router.post("/parameters/update")
async def update_testcase_out_parameters(form: ApiTestCaseOutParametersForm,
                                         user_info=Depends(Permission())):
    data = await ApiTestCaseOutParametersDao.update_record_by_id(user_info['emp_no'], form)
    return PikaResponse.success(data=data)


@router.get("/parameters/delete")
async def delete_testcase_out_parameters(id: int, user_info=Depends(Permission()),
                                         session=Depends(get_async_session)):
    await ApiTestCaseOutParametersDao.delete_record_by_id(session, user_info['emp_no'], id, log=False)
    return PikaResponse.success()


@router.get("/record/start", summary="开始录制接口请求")
async def record_requests(request: Request, regex: str, user_info=Depends(Permission())):
    await RedisHelper.set_address_record(user_info['emp_no'], request.client.host, regex)
    return PikaResponse.success(message="开始录制，可以在浏览器/app上操作啦！")


@router.get("/record/stop", summary="停止录制接口请求")
async def record_requests(request: Request, _=Depends(Permission())):
    await RedisHelper.remove_address_record(request.client.host)
    return PikaResponse.success(message="停止成功，快去生成用例吧~")


@router.get("/record/status", summary="获取录制接口请求状态")
async def record_requests(request: Request, _=Depends(Permission())):
    record = await RedisHelper.get_address_record(request.client.host)
    status = False
    regex = ''
    if record is not None:
        record_data = json.loads(record)
        regex = record_data.get('regex', '')
        status = True
    data = await RedisHelper.list_record_data(request.client.host)
    return PikaResponse.success(data=dict(data=data, regex=regex, status=status))


@router.get("/record/remove", summary="删除录制接口")
async def remove_record(index: int, request: Request, _=Depends(Permission())):
    await RedisHelper.remove_record_data(request.client.host, index)
    return PikaResponse.success()


@router.post("/generate", summary="生成用例")
async def generate_case(form: TestCaseGeneratorForm, user_info=Depends(Permission()),
                        session=Depends(get_async_session)):
    if len(form.requests) == 0:
        return PikaResponse.failed(detail="无http请求，请检查参数")
    CaseGenerator.extract_field(form.requests)
    cs = CaseGenerator.generate_case(form.directory_id, form.name, form.requests[-1])
    constructors = CaseGenerator.generate_constructors(form.requests)
    info = TestCaseInfo(constructor=constructors, case=cs)
    async with session.begin():
        ans = await ApiTestCaseDao.insert_test_case(session, info, user_info['emp_no'])
        return PikaResponse.success(data=ans)


@router.post("/import", summary="导入har或其他用例数据文件")
async def convert_case(import_type: CaseConvertorTypeEnum, file: UploadFile = File(...),
                       _=Depends(Permission())):
    convert, file_ext = get_convertor(import_type)
    if convert is None:
        return PikaResponse.failed(detail=f"不支持的导入数据")
    if not file.filename.endswith(f".{file_ext}"):
        return PikaResponse.failed(detail=f"请传入{file_ext}后缀文件")
    requests = convert(file.file)
    return PikaResponse.success(data=requests)
