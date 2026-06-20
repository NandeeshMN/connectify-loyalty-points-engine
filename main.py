from fastapi import FastAPI

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