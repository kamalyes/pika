from typing import List

from pydantic import BaseModel


class NotificationSchema(BaseModel):
    personal: List[int] = None
    broadcast: List[int] = None
