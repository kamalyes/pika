from abc import ABC

from app.crud import PikaWrapper, PikaMdWrapper
from app.models.minioss import OssFileModel


@PikaMdWrapper(OssFileModel)
class PikaOssDao(PikaWrapper, ABC):
    pass
