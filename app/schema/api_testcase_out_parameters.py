from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel


class ApiTestCaseOutParametersSchema(BaseModel):
    id: int = None
    # case_id: int = None
    name: str
    expression: str = None
    match_index: str = None
    source: int

    # noinspection PyMethodParameters
    @validator("name", "source")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class ApiTestCaseParametersSchema(ApiTestCaseOutParametersSchema):
    case_id: int = None


class ApiTestCaseVariablesSchema(BaseModel):
    case_id: int
    step_name: str
