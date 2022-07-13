from fastapi import Body
from pydantic import BaseModel

from app.enums.ByteSizeEnum import ByteSizeEnum


class ProjectSchema(BaseModel):
    name: str = Body(..., name="项目名称", max_length=ByteSizeEnum.LENGTH_16)
    app: str = Body(..., name="项目名称", max_length=ByteSizeEnum.LENGTH_32)
    owner: str = Body(..., name="项目名称", max_length=ByteSizeEnum.LENGTH_16)
    private: bool = Body(False, name="项目名称")
    description: str = Body(None, name="项目名称", max_length=ByteSizeEnum.LENGTH_600)
    dingtalk_url: str = Body(None, name="项目名称", max_length=ByteSizeEnum.LENGTH_128)
    qy_wx_url: str = Body(None, name="项目名称", max_length=ByteSizeEnum.LENGTH_128)


class ProjectEditSchema(ProjectSchema):
    id: int = Body(..., name="项目id")


class ProjectDelSchema(BaseModel):
    id: int = Body(..., name="项目id")


class ProjectRoleSchema(BaseModel):
    emp_no: str = Body(..., name="员工编号", max_length=ByteSizeEnum.LENGTH_16)
    project_role: int = Body(..., name="项目角色")
    project_id: int = Body(..., name="项目id")


class ProjectRoleEditSchema(ProjectRoleSchema):
    id: int = Body(..., name="项目角色id")
