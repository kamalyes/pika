from fastapi import APIRouter, File, Depends, UploadFile
from app.core.handler.exceres import KeyUndefinedException

from app.core.handler.jsonres import PikaResponse
from app.crud.rbac.user import UserDao
from app.crud.system.minioss import PikaOssDao
from app.enums.RbacEnum import RoleEnum
from app.middleware.oss import OssClient
from app.models import async_db_session_iterator
from app.models.minioss import OssFileModel
from app.service import Permission

router = APIRouter()


@router.post("/upload", summary="文件上传")
async def create_oss_file(filepath: str, file: UploadFile = File(...),
                          user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        file_content = await file.read()
        client = OssClient.get_oss_client()
        # oss上传 WARNING: 可能存在数据不同步的问题,oss成功本地失败
        file_url, file_size = await client.upload_file(filepath, file_content)
        # 本地数据也要备份一份
        model = OssFileModel(operator=user_info['emp_no'], file_path=filepath, view_url=file_url,
                             file_size=OssFileModel.get_size(file_size))
        record = await PikaOssDao.query_record(file_path=filepath, delete_flag=False)
        if record is not None:
            record.file_path = filepath
            record.view_url = file_url
            record.file_size = file_size
            await PikaOssDao.update_record_by_id(user_info['emp_no'], record)
        else:
            await PikaOssDao.insert(model=model, log=True)
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=f"上传失败: {e}")


@router.post("/avatar", summary="上传用户头像")
async def upload_avatar(file: UploadFile = File(...),
                        user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        file_content = await file.read()
        suffix = file.filename.split(".")[-1]
        filepath = f"user_{user_info['emp_no']}.{suffix}"
        client = OssClient.get_oss_client()
        file_url, _ = await client.upload_file(filepath, file_content, base_path="avatar")
        await UserDao.update_avatar(emp_no=user_info['emp_no'], avatar=file_url)
        return PikaResponse.success(data=file_url)
    except Exception as e:
        return PikaResponse.failed(detail=f"上传头像失败: {e}")


@router.get("/list", summary="查询文件")
async def list_oss_file(filepath: str = None, user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        records = await PikaOssDao.select_list(
            condition=[OssFileModel.file_path.like(f'%{filepath}%')])
        return PikaResponse.records(records)
    except Exception as e:
        return PikaResponse.failed(detail=f"获取失败: {e}")


@router.get("/delete", summary="删除文件")
async def delete_oss_file(filepath: str, user_info=Depends(Permission(RoleEnum.MANAGER)),
                          session=Depends(async_db_session_iterator)):
    try:
        # 先获取到本地的记录,拿到sha值
        record = await PikaOssDao.query_record(file_path=filepath, delete_flag=False)
        if record is None:
            raise KeyUndefinedException(detail="文件不存在或已被删除")
        await PikaOssDao.delete_record_by_id(session, user_info["emp_no"], record.id, log=True)
        client = OssClient.get_oss_client()
        await client.remove_file(filepath)
        return PikaResponse.success()
    except Exception as e:
        return PikaResponse.failed(detail=f"删除失败: {e}")


@router.get("/download", summary="下载文件")
async def download_oss_file(filepath: str):
    try:
        client = OssClient.get_oss_client()
        # 切割获取文件名
        path, filename = await client.download_file(filepath)
        return PikaResponse.file(path, filename)
    except Exception as e:
        return PikaResponse.failed(detail=f"下载失败: {e}")
