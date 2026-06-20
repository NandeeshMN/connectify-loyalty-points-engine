from fastapi import FastAPI
from sqlalchemy import func
from rules import calculate_points
from database import engine, SessionLocal
from models import Base, Event, Ledger, Reward
from schemas import EventCreate, RedeemRequest, ReverseRequest

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
        db.close()
        return {
            "message": "Event already processed"
        }

    new_event = Event(
        event_id=event.event_id,
        user_id=event.user_id,
        event_type=event.event_type,
        amount=event.amount,
        event_date=event.event_date
    )

    db.add(new_event)
    db.commit()

        # Calculate points using rules engine
    points = calculate_points(
    event.event_type,
    event.event_date
)
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


@app.get("/balance/{user_id}")
def get_balance(user_id: str):

    db = SessionLocal()

    balance = db.query(
        func.sum(Ledger.points)
    ).filter(
        Ledger.user_id == user_id
    ).scalar()

    db.close()

    return {
        "user_id": user_id,
        "balance": balance or 0
    }

@app.post("/add-rewards")
def add_rewards():

    db = SessionLocal()

    reward1 = Reward(
        reward_name="₹100 Coupon",
        points_required=10
    )

    reward2 = Reward(
        reward_name="₹500 Coupon",
        points_required=50
    )

    reward3 = Reward(
        reward_name="Free Delivery",
        points_required=5
    )

    db.add_all([reward1, reward2, reward3])
    db.commit()

    db.close()

    return {
        "message": "Sample rewards added successfully"
    }

@app.post("/redeem")
def redeem_reward(request: RedeemRequest):

    db = SessionLocal()

    # Find reward
    reward = db.query(Reward).filter(
        Reward.reward_name == request.reward_name
    ).first()

    if not reward:
        db.close()
        return {
            "message": "Reward not found"
        }

    # Calculate balance
    balance = db.query(
        func.sum(Ledger.points)
    ).filter(
        Ledger.user_id == request.user_id
    ).scalar()

    balance = balance or 0

    # Check sufficient balance
    if balance < reward.points_required:
        db.close()
        return {
            "message": "Insufficient points",
            "current_balance": balance
        }

    # Deduct points
    ledger_entry = Ledger(
        user_id=request.user_id,
        event_id=f"REDEEM_{reward.id}",
        points=-reward.points_required,
        transaction_type="DEBIT"
    )

    points_deducted = reward.points_required

    db.add(ledger_entry)
    db.commit()

    db.close()

    return {
        "message": "Reward redeemed successfully",
        "points_deducted": points_deducted
    }

@app.post("/reverse")
def reverse_event(request: ReverseRequest):

    db = SessionLocal()

    # Find original event
    event = db.query(Event).filter(
        Event.event_id == request.event_id
    ).first()

    if not event:
        db.close()
        return {
            "message": "Event not found"
        }

    # Check if already reversed
    existing_reversal = db.query(Ledger).filter(
        Ledger.event_id == f"REVERSAL_{request.event_id}"
    ).first()

    if existing_reversal:
        db.close()
        return {
            "message": "Event already reversed"
        }

    # Find original ledger entry
    original_ledger = db.query(Ledger).filter(
        Ledger.event_id == request.event_id
    ).first()

    if not original_ledger:
        db.close()
        return {
            "message": "Ledger entry not found"
        }

    reversal_points = -original_ledger.points

    reversal_entry = Ledger(
        user_id=event.user_id,
        event_id=f"REVERSAL_{request.event_id}",
        points=reversal_points,
        transaction_type="DEBIT"
    )

    db.add(reversal_entry)
    db.commit()

    db.close()

    return {
        "message": "Event reversed successfully",
        "points_reversed": abs(reversal_points)
    }