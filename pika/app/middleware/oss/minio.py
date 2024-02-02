from typing import List

from awaits.awaitable import awaitable
from minio import Minio
from minio.error import InvalidResponseError

from app.middleware.oss.files import OssFile


class MinioOssClient(OssFile):
    """定义一个类,用于minio的操作"""

    def __init__(self, access_key: str, secret_key: str, bucket_name: str, endpoint: str, secure: bool):
        self.minioClient = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=secure)
        self.bucket_name = bucket_name

    @awaitable
    def upload_file(self, filepath: str, content: bytes, base_path: str = None):
        """
        上传文件,并返回文件的url
        Args:
            filepath: 文件路径
            content: 文件
            base_path: 基础路径
        Returns:
        """
        try:
            key = self.get_real_path(filepath, base_path)
            self.minioClient.fput_object(self.bucket_name, content, key)
            url = self.minioClient.presigned_get_object(self.bucket_name, content)
            return url
        except InvalidResponseError as err:
            raise Exception(f"上传文件出错: {err}")

    @awaitable
    def download_file(self, filepath: str, content: bytes, base_path: str = None):
        """
        下载文件
        Args:
            filepath: 文件路径
            content: 文件
            base_path: 基础路径
        Returns:
        """
        try:
            key = self.get_real_path(filepath, base_path)
            self.minioClient.fget_object(self.bucket_name, content, key)
        except InvalidResponseError as err:
            raise Exception(f"下载文件出错: {err}")

    @awaitable
    def remove_file(self, filepath: str, base_path: str = None):
        """
        删除文件
        Args:
            filepath: 文件路径
            base_path: 基础路径
        Returns:
        """
        try:
            key = self.get_real_path(filepath, base_path)
            self.minioClient.remove_object(self.bucket_name, key)
        except InvalidResponseError as err:
            raise Exception(f"删除文件失败: {err}")

    @awaitable
    def list_file(self) -> List:
        """
        列出桶中的文件
        Args:

        Returns:
        """
        try:
            objects = self.minioClient.list_objects(self.bucket_name, recursive=True)
            file_list = []
            for obj in objects:
                file_list.append(obj.object_name)
                print(
                    obj.bucket_name,
                    obj.object_name.encode("utf-8"),
                    obj.last_modified,
                    obj.etag,
                    obj.size,
                    obj.content_type,
                )
            return file_list
        except InvalidResponseError as err:
            raise Exception(f"删除文件失败: {err}")

    @awaitable
    def get_preview_url(self, filepath, base_path):
        """
        返回预览图片的url
        Args:
            filepath: 文件路径
            base_path: 基础路径
        Returns:
            _type_: _description_
        """
        try:
            key = self.get_real_path(filepath, base_path)
            url = self.minioClient.presigned_get_object(self.bucket_name, key)
            return url
        except InvalidResponseError as err:
            raise Exception(f"删除文件失败: {err}")


if __name__ == "__main__":
    minioOssClient = MinioOssClient()
    ## 删除文件
    minioOssClient.remove_file("cultural-data-base", "data5.txt")
    ## 列出桶中的文件
    minioOssClient.list_file("cultural-data-base")
    ## 上传文件
    upload_result = minioOssClient.upload_file("cultural-data-base", "3.png", "3.png")
    print("上传文件", upload_result)
    ## 下载文件
    minioOssClient.download_file("cultural-data-base", "2.png", "2.png")
    ## 返回预览图片的url
    get_preview_url = minioOssClient.get_preview_url("cultural-data-base", "2.png")
    print("获取预览图", get_preview_url)
