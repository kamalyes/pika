from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.schema.script import PyScriptForm
from app.service import Permission

router = APIRouter()


@router.post("/pyscript", name="Python脚本")
def execute_py_script(data: PyScriptForm, user_info=Depends(Permission())):
    try:
        loc = dict()
        exec(data.command, loc)
        value = loc.get(data.value)
        return PikaResponse.success(result=value)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
