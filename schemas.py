from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    event_id: str
    user_id: str
    event_type: str
    amount: float

class RedeemRequest(BaseModel):
    user_id: str
    reward_name: str

class ReverseRequest(BaseModel):
    event_id: str

class EventCreate(BaseModel):
    event_id: str
    user_id: str
    event_type: str
    amount: float
    event_date: datetime