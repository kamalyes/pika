from abc import ABC

from app.crud import PikaMdWrapper, PikaWrapper
from app.models.minioss import OssFileModel


@PikaMdWrapper(OssFileModel)
class PikaOssDao(PikaWrapper, ABC):
    pass
