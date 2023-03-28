from typing import Optional

from fastapi import Body
from pydantic import BaseModel, validator

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.exceptions.business.ParamsException import VariablesNullError
from app.schema.base import BaseOnlyDelSchema, BaseOnlyIdSchema, PikaBaseModel


class ConstructorSchema(BaseOnlyIdSchema):
    value: Optional[str] = Body(
        "", title="", max_length=ByteSizeEnum.LENGTH_255)
    type: Optional[int] = Body(
        0, title="类型 0: testcase 1: sqlscript 2: redis 3: py脚本 4: 其它")
    name: Optional[str] = Body(
        "", title="", max_length=ByteSizeEnum.LENGTH_255)
    constructor_json: Optional[str] = Body("", title="constructor_json")
    enabled_flag: Optional[bool] = Body(True, title="是否可用")
    case_id: Optional[int] = Body(0, title="所属用例id")
    public: Optional[bool] = Body(False, title="是否共享")
    suffix: Optional[bool] = Body(False, title="是否是后置条件，默认为否")

    # noinspection PyMethodParameters
    @validator("name", "constructor_json", "type", "public", "enabled_flag", "suffix")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        if not isinstance(v, int):
            if not v:
                raise VariablesNullError("不能为空")
        return v


class IndexConstructorSchema(ConstructorSchema):
    index: Optional[int] = Body(0, title="前置条件顺序")


class ConstructorIndexSchema(IndexConstructorSchema, BaseOnlyDelSchema):
    pass

    # noinspection PyMethodParameters
    @validator("index")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
