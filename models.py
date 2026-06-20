from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(String, unique=True, nullable=False)

    user_id = Column(String, nullable=False)

    event_type = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )