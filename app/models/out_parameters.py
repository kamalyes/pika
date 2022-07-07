from sqlalchemy import Column, String, INT, UniqueConstraint

from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase


class PikaTestCaseOutParameters(PikaLargeBase):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_out_parameters"
    __table_args__ = (UniqueConstraint('case_id', 'name'), {"comment": "用例出参数据表，与用例绑定"})
    case_id = Column(INT, nullable=False, comment="用例id")
    name = Column(String(24), nullable=False, comment="参数名")
    source = Column(INT, nullable=False, default=0,
                    comment="来源类型 0: Body(TEXT) 1: Body(JSON) 2: Header 3: Cookie 4: HTTP状态码")
    expression = Column(String(128), comment="表达式")
    match_index = Column(String(16), comment="获取结果索引, 可以是random，也可以是all，还可以是数字")

    def __init__(self, name, source, case_id, operator, expression=None, match_index=None, id=None):
        super().__init__(operator, id)
        self.name = name
        self.case_id = case_id
        self.expression = expression
        self.match_index = match_index
        self.source = source
