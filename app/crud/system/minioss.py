from sqlalchemy.orm import Mapper

from app.core.handler.logger import PikaLogger
from app.models.minioss import PikaOssFile
from app.utils.decorator import dao


@dao(PikaOssFile, PikaLogger("PikaOssDao"))
class PikaOssDao(Mapper):
    pass
