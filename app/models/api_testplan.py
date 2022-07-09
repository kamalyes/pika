from sqlalchemy import Column, String, TEXT, BOOLEAN, SMALLINT, INT

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel

_notice_type = {
    '0': '邮件',
    '1': '钉钉',
    '2': '企业微信',
    '3': '飞书'
}


class ApiTestPlanModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_test_plan"
    __table_args__ = {"comment": "测试计划表"}
    project_id = Column(INT, nullable=False, comment="测试计划执行环境, 可以多选")
    env = Column(String(ByteSizeEnum.LENGTH_64), nullable=False, comment="测试计划名称")
    name = Column(String(ByteSizeEnum.LENGTH_32), nullable=False, comment="名称")
    priority = Column(String(ByteSizeEnum.LENGTH_03), nullable=False, comment="测试计划优先级")
    cron = Column(String(ByteSizeEnum.LENGTH_24), nullable=False, comment="cron表达式")
    case_list = Column(TEXT, nullable=False, comment="用例列表")
    ordered = Column(BOOLEAN, default=False, comment="并行/串行(是否顺序执行)")
    pass_rate = Column(SMALLINT, default=70, comment="通过率低于这个数会自动发通知")
    receiver = Column(TEXT, comment="通知人 目前只有邮箱，后续用户表可能要完善手机号字段，为了通知")
    msg_type = Column(TEXT, comment="通知方式 0: 邮件 1: 钉钉 2: 企业微信 3: 飞书 支持多选")
    retry_minutes = Column(SMALLINT, nullable=False, default=0, comment="重试时间 单次case失败重试间隔，默认2分钟")
    state = Column(SMALLINT, default=0, comment="测试计划是否正在执行中 0: 未开始 1: 运行中")

    def __init__(self, project_id, env, case_list, name, priority, cron, ordered, pass_rate,
                 receiver, msg_type,
                 operator, state=0, retry_minutes=0, id=None):
        super().__init__(operator, id)
        self.env = ",".join(map(str, env))
        self.case_list = ",".join(map(str, case_list))
        self.name = name
        self.project_id = project_id
        self.priority = priority
        self.ordered = ordered
        self.cron = cron
        self.pass_rate = pass_rate
        self.receiver = ",".join(map(str, receiver))
        self.msg_type = ",".join(map(str, msg_type))
        self.retry_minutes = retry_minutes
        self.state = state

    @staticmethod
    def get_msg_type(msg_type):
        return ",".join(_notice_type.get(str(x), '未知') for x in msg_type.split(","))
