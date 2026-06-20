from pydantic import BaseModel


class EventCreate(BaseModel):
    event_id: str
    user_id: str
    event_type: str
    amount: float