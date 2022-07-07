from typing import Optional

from fastapi import Body
from pydantic import BaseModel, validator

from app.enums.bytesize import ByteSizeEnum
from app.excpetions.ParamsException import ParamsError
from app.schema.base import PikaBaseModel


class ConstructorForm(BaseModel):
    id: Optional[int] = Body(0, title="id")
    value: Optional[str] = Body("", title="", max_length=ByteSizeEnum.LENGTH_255)
    type: Optional[int] = Body(0, title="类型 0: testcase 1: sqlscript 2: redis 3: py脚本 4: 其它")
    name: Optional[str] = Body("", title="", max_length=ByteSizeEnum.LENGTH_255)
    index: Optional[int] = Body(0, title="前置条件顺序")
    constructor_json: Optional[str] = Body("", title="constructor_json")
    enable: Optional[bool] = Body(None, title="密保问题")
    case_id: Optional[int] = Body(0, title="所属用例id")
    public: Optional[bool] = Body(False, title="是否共享")
    suffix: Optional[bool] = Body(False, title="是否是后置条件，默认为否")

    @validator("name", "constructor_json", "type", "public", "enable", "suffix")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        if not isinstance(v, int):
            if not v:
                raise ParamsError("不能为空")
        return v


class ConstructorIndex(BaseModel):
    id: Optional[int] = Body(0, title="id")
    index: Optional[int] = Body(0, title="前置条件顺序")

    @validator("id", "index")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)
