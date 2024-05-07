
from pydantic import BaseModel
from typing import List


# 定義資料模型
class Strategy(BaseModel):
    strategy_name: str
    parameters: dict


class RunRequest(BaseModel):
    file_name: str
    strategy: Strategy
    data: List
    webhook_url: str
    webhook_time: str


class TerminateRequest(BaseModel):
    file_name: str


class SettingRequest(BaseModel):
    file_name: str
    strategy: Strategy
    data: List
    webhook_url: str
    webhook_time: str
