from typing import List

from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel


class ApiTestPlanSchema(BaseModel):
    id: int = None
    project_id: int
    name: str
    priority: str
    env: List[int]
    cron: str
    ordered: bool
    case_list: List[int]
    pass_rate: int
    receiver: List[int] = list()
    msg_type: List[int] = list()
    retry_minutes: int = 0

    # noinspection PyMethodParameters
    @validator("case_list", "project_id", "env", "cron", "ordered", "priority", "name", "pass_rate")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
