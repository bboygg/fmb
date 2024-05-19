# The entry point of the application where the FastAPI app is created and router are included.

from fastapi import FastAPI
from app.api.routes import battle

app = FastAPI()

app.include_router(battle.router)

@app.get("/")
def get_root():
    return {"Don't miss out your battle!"}
