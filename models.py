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
    event_date = Column(DateTime, nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class Ledger(Base):
    __tablename__ = "ledger"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(String, nullable=False)

    event_id = Column(String, nullable=False)

    points = Column(Integer, nullable=False)

    transaction_type = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, index=True)

    reward_name = Column(String, nullable=False)

    points_required = Column(Integer, nullable=False)