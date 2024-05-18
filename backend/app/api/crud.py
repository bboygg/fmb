# Functions for Create, Read, Update, Delete operations.

from sqlalchemy.orm import Session
from app.api import models, schemas
from datetime import datetime


def get_battle(db: Session, battle_id: int):
    return db.query(models.Battle).filter(models.Battle.id == battle_id).first()

def get_battles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Battle).offset(skip).limit(limit).all()

# TODO: check the schema for meta column
def create_battle(db: Session, battle: schemas.BattleCreate):
    db_battle = models.Battle(**battle.model_dump())
    db.add(db_battle)
    db.commit()
    db.refresh(db_battle)
    return db_battle

# TODO: check the schema for meta column
def update_battle(db: Session, battle_id: int, battle: schemas.BattleUpdate):
    db_battle = db.query(models.Battle).filter(models.Battle.id == battle_id).first()
    if db_battle is None: 
        return None

    for key, value in battle.model_dump(exclude_unset=True).items():
        setattr(db_battle, key, value)
    
    db.commit()
    db.refresh(db_battle)
    
    return db_battle

def delete_battle(db: Session, battle_id: int):
    db_battle = db.query(models.Battle).filter(models.Battle.id == battle_id).first()

    if db_battle:
        db.delete(db_battle)
        db.commit()
    
    return db_battle