from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel


class ApiTestCaseDataSchema(BaseModel):
    id: int = None
    case_id: int = None
    name: str
    json_data: str
    env: int

    # noinspection PyMethodParameters
    @validator("env", "name", "json_data")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
