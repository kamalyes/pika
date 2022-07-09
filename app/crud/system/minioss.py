from abc import ABC

from sqlalchemy.orm import Mapper

from app.core.handler.logger import PikaLogger
from app.models.minioss import OssFileModel
from app.utils.decorator import dao


@dao(OssFileModel, PikaLogger("PikaOssDao"))
class PikaOssDao(Mapper, ABC):
    pass
