from typing import TypeVar

from fastapi import WebSocket

from app.core.handler.logger import PikaLogger
from app.core.notice.wss_msg import WebSocketMessage
from app.crud.system.notification import PikaNotificationDao
from app.models.notification import NotificationModel

MsgType = TypeVar('MsgType', str, dict, bytes)


class ConnectionManager:
    BROADCAST = "-1"
    logger = PikaLogger("wss_manager")

    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}
        self.log = PikaLogger("websocket")

    def get_clients(self):
        return {key: True for key in self.active_connections.keys()}

    async def connect(self, websocket: WebSocket, operator: str) -> None:
        await websocket.accept()
        exist: WebSocket = self.active_connections.get(operator)
        if exist:
            await exist.close()
            self.active_connections[operator]: WebSocket = websocket
        else:
            self.active_connections[operator]: WebSocket = websocket
            self.log.debug(F"websocket: 用户[{operator}]建立连接成功！")

    def disconnect(self, operator: str) -> None:
        del self.active_connections[operator]
        self.log.debug(F"websocket: 用户[{operator}] 已安全断开！")

    @staticmethod
    async def pusher(sender: WebSocket, message: MsgType) -> None:
        """
        根据不同的消息类型,调用不同方法发送消息
        Args:
            sender:
            message:

        Returns:

        """
        msg_mapping: dict = {
            str: sender.send_text,
            dict: sender.send_json,
            bytes: sender.send_bytes
        }
        func_push_msg = msg_mapping.get(type(message))
        if func_push_msg:
            await func_push_msg(message)
        else:
            raise TypeError(F"websocket不能发送{type(message)}的内容！")

    async def send_personal_message(self, operator: str, message: MsgType) -> None:
        """
        发送个人信息
        Args:
            operator:
            message:

        Returns:

        """
        conn = self.active_connections.get(operator)
        if conn:
            await self.pusher(sender=conn, message=message)

    async def broadcast(self, message: MsgType) -> None:
        """
        广播
        Args:
            message:

        Returns:

        """
        for connection in self.active_connections.values():
            await self.pusher(sender=connection, message=message)

    async def send_data(self, emp_no, msg_type, record_msg):
        msg = dict(type=msg_type, record_msg=record_msg)
        await self.send_personal_message(emp_no, msg)

    async def notify(self, operator, title=None, content=None, notice: NotificationModel = None):
        """
        根据user_id推送对应的
        Args:
            operator:
            title:
            content:
            notice:

        Returns:

        """
        try:
            # 判断是否为桌面通知
            if title is not None:
                msg = WebSocketMessage.desktop_msg(title, content)
                if operator == ConnectionManager.BROADCAST:
                    await self.broadcast(msg)
                else:
                    await self.send_personal_message(operator, msg)
            else:
                # 说明不是桌面消息,直接给出消息数量即可
                if operator == ConnectionManager.broadcast:
                    await self.broadcast(WebSocketMessage.msg_count())
                else:
                    await self.send_personal_message(operator, WebSocketMessage.msg_count())
            # 判断是否要落入推送表
            if notice is not None:
                await PikaNotificationDao.insert(notice)
        except Exception as e:
            ConnectionManager.logger.error(f"发送消息失败, {e}")


ws_manage = ConnectionManager()
