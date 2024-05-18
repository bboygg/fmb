from fastapi.routing import APIRouter, Depends, HTTPException, status
from app.api import crud, schemas
from sqlalchemy.orm import Session
from typing import List 
from app.database import get_db

router = APIRouter()

@router.get("/battles/", response_model=List[schemas.Battle])
def get_battles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    """
    Retrieve a list of battles from the database.

    Args:
        skip (int): Number of records to skip for pagination.
        limit (int): Maximum number of records to return.
        db (Session): Database session dependency.

    Returns:
        List[schemas.Battle]: List of battle records.
        Note: Use response model with 'List' allow api to return mulitple items
    """
    battles = crud.get_battles(db, skip=skip, limit=limit)
    return battles


@router.get("/battles/{battle_id}", response_mode=schemas.Battle)
def get_battle(batte_id: int, db: Session = Depends(get_db)):
    """
    Retrieve specific battle with given battle_id from the datase.

    Args:
        battle_id: Battle Id
        db (Session): Database session dependency.

    Returns:
        schemas.Battle: Battle Record
    """
    battle = crud.get_battle(db, battle_id=batte_id)
    return battle



