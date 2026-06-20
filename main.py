from fastapi import FastAPI

from database import engine
from models import Base

from database import engine, SessionLocal
from models import Base, Event, Ledger
from schemas import EventCreate

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Loyalty Points Engine",
    description="Backend Assignment for Connectify Global",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Loyalty Points Engine is running"
    }

@app.post("/events")
def create_event(event: EventCreate):

    db = SessionLocal()

    # Check if event already exists
    existing_event = db.query(Event).filter(
        Event.event_id == event.event_id
    ).first()

    if existing_event:
        return {
            "message": "Event already processed"
        }

    new_event = Event(
        event_id=event.event_id,
        user_id=event.user_id,
        event_type=event.event_type,
        amount=event.amount
    )

    db.add(new_event)
    db.commit()

    # Award points based on event type
    points = 0

    if event.event_type == "purchase":
        points = 10

    elif event.event_type == "referral":
        points = 50


    ledger_entry = Ledger(
        user_id=event.user_id,
        event_id=event.event_id,
        points=points,
        transaction_type="CREDIT"
    )

    db.add(ledger_entry)
    db.commit()
    db.close()

    return {
        "message": "Event created successfully"
    }