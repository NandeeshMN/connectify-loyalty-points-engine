from pydantic import BaseModel


class EventCreate(BaseModel):
    event_id: str
    user_id: str
    event_type: str
    amount: float

class RedeemRequest(BaseModel):
    user_id: str
    reward_name: str