from abc import ABC
from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.models.minioss import OssFileModel
from app.utils.decorator import dao


@dao(OssFileModel, PikaLogger("PikaOssDao"))
class PikaOssDao(PikaMapper, ABC):
    pass
