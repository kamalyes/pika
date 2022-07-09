from pydantic import validator, BaseModel

from app.excpetions.business.ParamsException import VariablesNullError


class ProjectForm(BaseModel):
    name: str
    app: str
    owner: str
    private: bool = False
    description: str = ''
    dingtalk_url: str = None
    qy_wx_url: str = None

    # noinspection PyMethodParameters
    @validator('name', 'app', 'owner')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        return v


class ProjectEditForm(BaseModel):
    id: int
    name: str
    app: str
    owner: str
    private: bool = False
    description: str = ''
    dingtalk_url: str = None
    qy_wx_url: str = None

    # noinspection PyMethodParameters
    @validator('id', 'name', 'app', 'owner')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        return v


class ProjectRoleModelForm(BaseModel):
    emp_no: str
    project_role: int
    project_id: int

    # noinspection PyMethodParameters
    @validator('emp_no', 'project_role', 'project_id')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        return v


class ProjectRoleModelEditForm(BaseModel):
    id: int
    emp_no: str
    project_role: int
    project_id: int

    # noinspection PyMethodParameters
    @validator('id', 'emp_no', 'project_role', 'project_id')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        return v


class ProjectDelForm(BaseModel):
    id: int

    # noinspection PyMethodParameters
    @validator('id')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise VariablesNullError("不能为空")
        return v
