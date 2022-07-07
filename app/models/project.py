from sqlalchemy import INT, Column, String, BOOLEAN

from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase


class PikaProject(PikaLargeBase):
    __tablename__ = f'{PikaGlobalVarEnum.APP_NAME_LOWER}_project'
    __table_args__ = {"comment": "项目管理表"}
    name = Column(String(16), unique=True, index=True, comment="项目名称")
    owner = Column(INT, comment="项目所有者")
    app = Column(String(32), index=True, comment="项目所属应用")
    private = Column(BOOLEAN, default=False, comment="是否私有")
    description = Column(String(200), comment="项目描述")
    avatar = Column(String(128), nullable=True, comment="项目头像")
    dingtalk_url = Column(String(128), nullable=True, comment="钉钉通知url")
    qy_wx_url = Column(String(128), nullable=True, comment="企微通知url")

    def __init__(self, name, app, owner, operator, description="",
                 private=False, avatar=None, dingtalk_url='', qy_wx_url=''):
        super().__init__(operator)
        self.name = name
        self.app = app
        self.owner = owner
        self.private = private
        self.description = description
        self.avatar = avatar
        self.dingtalk_url = dingtalk_url
        self.qy_wx_url = qy_wx_url


class ProjectRole(PikaLargeBase):
    __tablename__ = f'{PikaGlobalVarEnum.APP_NAME_LOWER}_project_role'
    __table_args__ = {"comment": "项目人员关联表"}
    member_no = Column(INT, index=True, comment="项目成员编号（用户编号）")
    project_id = Column(INT, index=True, comment="项目id")
    project_role = Column(INT, index=True, comment="角色")

    def __init__(self, member_no, project_id, project_role, operator):
        super().__init__(operator)
        self.member_no = member_no
        self.project_id = project_id
        self.project_role = project_role
