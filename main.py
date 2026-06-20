from fastapi import FastAPI

from database import engine
from models import Base

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