from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel


class ApiTestCaseOutParametersForm(BaseModel):
    id: int = None
    case_id: int = None
    name: str
    expression: str = None
    match_index: str = None
    source: int

    # noinspection PyMethodParameters
    @validator("name", "source")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
