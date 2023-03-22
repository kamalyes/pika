import json
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
from app.crud.pmp.project import ProjectRoleDao
from app.enums.ConvertorEnum import CaseConvertorTypeEnum
from app.middleware.xredis import RedisHelper
from app.models import async_db_session_iterator
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.schema.api_testcase import TestCaseAssertsForm, TestCaseSchema, TestCaseInfo, TestCaseGeneratorForm
from app.schema.api_testcase_data import ApiTestCaseDataSchema
from app.schema.api_testcase_directory import ApiTestCaseDirectorySchema, MoveApiTestCaseSchema
from app.schema.api_testcase_out_parameters import (
    ApiTestCaseOutParametersSchema,
    ApiTestCaseParametersSchema,
    ApiTestCaseVariablesSchema,
)
from app.schema.base import BaseOnlyPagingSchema
from app.schema.constructor import ConstructorSchema, ConstructorIndexSchema
from app.schema.report import ApiTestReportSchema
from app.service import Permission

router = APIRouter()


@router.get("/list", summary="用例列表查询")
async def list_testcase(paging: BaseOnlyPagingSchema = Depends(), directory_id: int = None, name: str = "", operator: str = ""):
    data, total = await ApiTestCaseDao.list_testcase(paging, directory_id, name, operator)
    return PikaResponse.success_with_size(data=data, total=total)


@router.post("/insert", summary="新增接口用例")
async def insert_testcase(data: TestCaseSchema, user_info=Depends(Permission())):
    try:
        record = await ApiTestCaseDao.query_record(name=data.name, directory_id=data.directory_id)
        if record is not None:
            return PikaResponse.failed(detail="用例已存在")
        model = ApiTestCaseModel(**data.dict(), operator=user_info["emp_no"])
        model = await ApiTestCaseDao.insert(model=model, log=True)
        return PikaResponse.success(data=model.id)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/create", summary="v2版本创建用例接口")
async def create_testcase(data: TestCaseInfo, user_info=Depends(Permission()), session=Depends(async_db_session_iterator)):
    async with session.begin():
        await ApiTestCaseDao.insert_test_case(session, data, user_info["emp_no"])
    return PikaResponse.success()


@router.post("/update", summary="更新测试用例")
async def update_testcase(form: TestCaseSchema, user_info=Depends(Permission())):
    try:
        data = await ApiTestCaseDao.update_test_case(form, user_info["emp_no"])
        result = await ApiTestCaseOutParametersDao.update_many(form.id, form.out_parameters, user_info["emp_no"])
        return PikaResponse.success(data=dict(case_info=data, out_parameters=result))
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.delete("/delete", summary="删除测试用例")
async def delete_testcase(id_list: List[int], user_info=Depends(Permission()), session=Depends(async_db_session_iterator)):
    operator = user_info["emp_no"]
    try:
        async with session.begin():
            await ApiTestCaseDao.delete_records(session, user_info["emp_no"], id_list, title="删除case")
            await ApiTestCaseAssertsDao.delete_records(
                session=session, operator=operator, id_list=id_list, column="case_id", title="删除断言"
            )
            await ApiTestCaseDataDao.delete_records(
                session=session, operator=operator, id_list=id_list, column="case_id", title="删除测试数据"
            )
            return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/query", summary="查询测试用例")
async def query_testcase(caseId: int, user_info=Depends(Permission())):
    try:
        data = await ApiTestCaseDao.query_test_case(caseId)
        return PikaResponse.success(data=PikaResponse.dict_model_to_dict(data))
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/asserts/insert", summary="增加用例断言")
async def insert_testcase_asserts(data: TestCaseAssertsForm, user_info=Depends(Permission())):
    try:
        new_assert = await ApiTestCaseAssertsDao.insert_test_case_asserts(data, operator=user_info["emp_no"])
        return PikaResponse.success(data=new_assert)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/asserts/update", summary="更新用例断言")
async def update_testcase_asserts(data: TestCaseAssertsForm, user_info=Depends(Permission())):
    try:
        updated = await ApiTestCaseAssertsDao.update_test_case_asserts(data, operator=user_info["emp_no"])
        return PikaResponse.success(data=updated)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/asserts/delete", summary="删除用例断言")
async def delete_test_case_asserts(id: int, user_info=Depends(Permission())):
    await ApiTestCaseAssertsDao.delete_test_case_asserts(id, operator=user_info["emp_no"])
    return PikaResponse.success()


@router.post("/constructor/insert", summary="增加前置条件")
async def insert_constructor(data: ConstructorSchema, user_info=Depends(Permission())):
    await ConstructorDao.insert_constructor(data, operator=user_info["emp_no"])
    return PikaResponse.success()


@router.post("/constructor/update", summary="更新前置条件")
async def update_constructor(data: ConstructorSchema, user_info=Depends(Permission())):
    await ConstructorDao.update_constructor(data, operator=user_info["emp_no"])
    return PikaResponse.success()


@router.get("/constructor/delete", summary="删除前置条件")
async def delete_constructor(id: int, user_info=Depends(Permission())):
    await ConstructorDao.delete_constructor(id, operator=user_info["emp_no"])
    return PikaResponse.success()


@router.post("/constructor/order", summary="更改前置条件顺序")
async def update_constructor_index(data: List[ConstructorIndexSchema], user_info=Depends(Permission())):
    await ConstructorDao.update_constructor_index(data)
    return PikaResponse.success()


@router.get("/constructor/tree", summary="获取所有构造器树")
async def get_constructor_tree(suffix: bool, name: str = "", user_info=Depends(Permission())):
    result = await ConstructorDao.get_constructor_tree(name, suffix)
    return PikaResponse.success(data=result)


@router.get("/constructor", summary="获取数据构造器树")
async def get_constructor_data(id: int, user_info=Depends(Permission())):
    """
    获取数据构造器树
    Args:
        id:
        user_info:

    Returns:

    """
    result = await ConstructorDao.get_constructor_data(id)
    return PikaResponse.success(data=result)


@router.get("/constructor/list", summary="获取所有数据构造器")
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


@router.get("/report", summary="根据id查询具体报告内容")
async def query_report(id: int, user_info=Depends(Permission())):
    """

    Args:
        id:
        user_info:

    Returns:

    """
    report, case_list, plan_name = await ApiTestReportDao.query(id)
    return PikaResponse.success(data=dict(report=report, plan_name=plan_name, case_list=case_list))


@router.get("/report/list", summary="获取构建历史记录")
async def list_report(
    paging: BaseOnlyPagingSchema = Depends(), request: ApiTestReportSchema = Depends(), user_info=Depends(Permission())
):
    report_list, total = await ApiTestReportDao.list_report(paging, request.start_date, request.finished_date, request.executor)
    return PikaResponse.success_with_size(data=report_list, total=total)


@router.get("/xmind", summary="获取脑图数据")
async def get_xmind_data(case_id: int, user_info=Depends(Permission())):
    tree_data = await ApiTestCaseDao.get_xmind_data(case_id)
    return PikaResponse.success(data=tree_data)


@router.get("/directory", summary="获取case目录")
async def get_testcase_directory(project_id: int, move: bool = False, user_info=Depends(Permission())):
    # 如果是move，则不需要禁用树
    tree_data, _ = await ApiTestCaseDirectoryDao.get_directory_tree(project_id, move=move)
    return PikaResponse.success(data=tree_data)


@router.get("/tree", summary="获取case目录+case")
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


@router.get("/directory/query", summary="查询测试用例类目")
async def query_testcase_directory(directory_id: int, escarole=Depends(Permission(escarole=True))):
    operator, operator_identity = escarole
    try:
        data = await ApiTestCaseDirectoryDao.query_directory(directory_id)
        await ProjectRoleDao.read_permission(data.project_id, operator, operator_identity)
        return PikaResponse.success(data=data)
    except AuthException:
        return PikaResponse.forbidden()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/directory/insert", summary="增加测试用例类目")
async def insert_testcase_directory(form: ApiTestCaseDirectorySchema, user_info=Depends(Permission())):
    try:
        await ApiTestCaseDirectoryDao.insert_directory(form, user_info["emp_no"])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/directory/update", summary="更新测试用例类目")
async def update_testcase_directory(form: ApiTestCaseDirectorySchema, user_info=Depends(Permission())):
    try:
        await ApiTestCaseDirectoryDao.update_directory(form, user_info["emp_no"])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/directory/delete", summary="删除测试用例类目")
async def insert_testcase_directory(id: int, user_info=Depends(Permission())):
    try:
        await ApiTestCaseDirectoryDao.delete_directory(id, user_info["emp_no"])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/data/insert", summary="增加测试用例数据")
async def insert_testcase_data(form: ApiTestCaseDataSchema, user_info=Depends(Permission())):
    try:
        data = await ApiTestCaseDataDao.insert_testcase_data(form, user_info["emp_no"])
        return PikaResponse.success(data=data)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/data/update", summary="更新测试用例数据")
async def update_testcase_data(form: ApiTestCaseDataSchema, user_info=Depends(Permission())):
    try:
        data = await ApiTestCaseDataDao.update_testcase_data(form, user_info["emp_no"])
        return PikaResponse.success(data=data)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/data/delete", summary="删除测试用例数据")
async def delete_testcase_data(id: int, user_info=Depends(Permission())):
    try:
        await ApiTestCaseDataDao.delete_testcase_data(id, user_info["emp_no"])
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/move", summary="移动case到其他目录")
async def move_testcase(form: MoveApiTestCaseSchema, escarole=Depends(Permission(escarole=True))):
    try:
        # 判断是否有移动case的权限
        operator, operator_identity = escarole
        await ProjectRoleDao.read_permission(form.project_id, operator, operator_identity)
        await ApiTestCaseDao.update_by_map(operator, ApiTestCaseModel.id.in_(form.id_list), directory_id=form.directory_id)
        return PikaResponse.success()
    except AuthException:
        return PikaResponse.forbidden()
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.post("/parameters/insert", summary="新增出参数据")
async def insert_testcase_out_parameters(form: ApiTestCaseParametersSchema, user_info=Depends(Permission())):
    query = await ApiTestCaseOutParametersDao.query_record(name=form.name, case_id=form.case_id)
    if query is not None:
        return PikaResponse.failed(detail="参数名称已存在")
    data = ApiTestCaseOutParametersModel(**form.dict(), operator=user_info["emp_no"])
    data = await ApiTestCaseOutParametersDao.insert(data)
    return PikaResponse.success(data=data)


@router.post("/parameters/update/batch", summary="批量更新出参数据")
async def update_batch_testcase_out_parameters(
    case_id: int, form: List[ApiTestCaseOutParametersSchema], user_info=Depends(Permission())
):
    result = await ApiTestCaseOutParametersDao.update_many(case_id, form, user_info["emp_no"])
    return PikaResponse.success(data=result)


@router.post("/parameters/update", summary="更新出参数据")
async def update_testcase_out_parameters(form: ApiTestCaseOutParametersSchema, user_info=Depends(Permission())):
    data = await ApiTestCaseOutParametersDao.update_record_by_id(operator=user_info["emp_no"], model=form)
    return PikaResponse.success(data=data)


@router.get("/parameters/delete", summary="删除出参数据")
async def delete_testcase_out_parameters(id: int, user_info=Depends(Permission()), session=Depends(async_db_session_iterator)):
    await ApiTestCaseOutParametersDao.delete_record_by_id(session=session, operator=user_info["emp_no"], value=id, log=True)
    return PikaResponse.success()


@router.get("/record/start", summary="开始录制接口请求")
async def start_record_requests(request: Request, regex: str, retain_history=False, user_info=Depends(Permission())):
    await RedisHelper.set_address_record(user_info["emp_no"], request.client.host, regex, retain_history)
    return PikaResponse.success(message="开始录制，可以在浏览器/app上操作啦！")


@router.get("/record/stop", summary="停止录制接口请求")
async def stop_record_requests(request: Request, user_info=Depends(Permission())):
    await RedisHelper.remove_address_record(request.client.host)
    return PikaResponse.success(message="停止成功，快去生成用例吧~")


@router.get("/record/list", summary="获取录制数据列表")
async def list_record_data(request: Request, user_info=Depends(Permission())):
    record = await RedisHelper.get_address_record(request.client.host)
    status = False
    regex = ""
    if record is not None:
        record_data = json.loads(record)
        regex = record_data.get("regex", "")
        status = True
    data = await RedisHelper.list_record_data(request.client.host)
    return PikaResponse.success(data=dict(data=data, regex=regex, status=status))


@router.get("/record/remove", summary="删除录制接口")
async def remove_record(index: int, request: Request, user_info=Depends(Permission())):
    await RedisHelper.remove_record_data(request.client.host, index)
    return PikaResponse.success()


@router.post("/generate", summary="生成用例")
async def generate_case(form: TestCaseGeneratorForm, user_info=Depends(Permission()), session=Depends(async_db_session_iterator)):
    if len(form.requests) == 0:
        return PikaResponse.failed(detail="无http请求，请检查参数")
    CaseGenerator.extract_field(form.requests)
    cs = CaseGenerator.generate_case(form.directory_id, form.name, form.requests[-1])
    constructors = CaseGenerator.generate_constructors(form.requests)
    info = TestCaseInfo(constructor=constructors, case=cs)
    async with session.begin():
        ans = await ApiTestCaseDao.insert_test_case(session, info, user_info["emp_no"])
        return PikaResponse.success(data=ans)


@router.post("/import", summary="导入har或其他用例数据文件")
async def convert_case(import_type: CaseConvertorTypeEnum, file: UploadFile = File(...), user_info=Depends(Permission())):
    convert, file_ext = get_convertor(import_type)
    if convert is None:
        return PikaResponse.failed(detail=f"不支持的导入数据")
    if not file.filename.endswith(f".{file_ext}"):
        return PikaResponse.failed(detail=f"请传入{file_ext}后缀文件")
    requests = convert(file.file)
    return PikaResponse.success(data=requests)


@router.post("/variables/list", summary="根据前后置步骤查询变量名")
async def query_variables(
    steps: List[ApiTestCaseVariablesSchema], user_info=Depends(Permission()), session=Depends(async_db_session_iterator))
    var_list = list()
    await ApiTestCaseDao.query_test_case_out_parameters(session, steps, var_list=var_list)
    return PikaResponse.success(var_list)