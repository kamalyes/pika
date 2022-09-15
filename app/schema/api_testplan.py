from typing import List, Optional

from fastapi import Body
from pydantic import BaseModel, validator

from app.schema.base import PikaBaseModel, BaseQuerySchema, BaseOnlyIdSchema


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


class QueryApiTestPlanInSchema(BaseQuerySchema):
    project_id: int = Body(None, title="是否关注")
    name: str = Body(None, title="是否关注")
    priority: str = Body(None, title="是否关注")
    env: List[int] = Body(None, title="是否关注")
    cron: str = Body(None, title="是否关注")
    ordered: bool = Body(None, title="是否关注")
    case_list: List[int] = Body(None, title="是否关注")
    pass_rate: int = Body(None, title="是否关注")
    receiver: List[int] = Body(list(), title="是否关注")
    msg_type: List[int] = Body(list(), title="是否关注")
    retry_minutes: int = Body(None, title="是否关注")
    follow: Optional[bool] = Body(False, title="是否关注")
    pass
