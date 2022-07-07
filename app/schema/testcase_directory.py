from typing import List

from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel


class PikaTestCaseDirectoryForm(BaseModel):
    id: int = None
    name: str
    project_id: int
    parent: int = None

    @validator("name", "project_id")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class PikaMoveTestCaseDto(BaseModel):
    project_id: int
    id_list: List[int]
    directory_id: int

    @validator("id_list", "project_id", "directory_id")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
