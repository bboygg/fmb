# The entry point of the application where the FastAPI app is created and router are included.

from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from app.api import schemas
from app.database import SesssionLocal, engine, Base
from backend.app.api.routes import user
from backend.app.api.routes import battle

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(battle.router, prefix="/battles", tags=["battles"])
app.include_router(user.router, prefix="/users", tags=["users"])

# Tag metadata
tags_metadata = [
    {
        "name": "battles",
        "description": "Operations with battles. The **create/read** logic is also here.",
        "externalDocs": {
            "description": "battles external docs",
            "url": "https://fastapi.tiangolo.com/",
        }
    }
]


@app.get("/")
def get_root():
    return {"Don't miss out your battle!"}



# class BattleBase(BaseModel):
#     id: int
#     name: str

# # Dependency
# def get_db():
#     db = SesssionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
        
# db_dependency = Annotated[Session,Depends(get_db)]

# @app.post("/battles/", status_code=status.HTTP_201_CREATED)
# async def create_battle(battle: BattleBase, db: db_dependency):
#     db_battle = models.Battle(**battle.model_dump())
#     db.add(db_battle)
#     db.commit()
    

# @app.get("/battles")
# def get_battles():
#     battles = "battle lists"
#     return battles

# @app.get("/battles/{id}")
# def get_battle(id: int, db: db_dependency):

#     # battle = db.query(models.Battle).filter(models.Post.id == id).first()
#     battle = f"battle id: {id}"
#     if not battle:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"Battle Id: {id} was not found")

#     return battle

