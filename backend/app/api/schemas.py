# Pydantic models for request and response validation.
'''
<<Tips>>
:SQLAlchemy models(models.py) vs Pydantic models(schemas.py)
To avoid confusion between the SQLAlchemy models and the Pydantic models, 
we will have the file models.py with the SQLAlchemy models, 
and the file schemas.py with the Pydantic models.
'''
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class BattleBase(BaseModel):
    name: str
    description: Optional[str] = None
    url: str
    date: datetime
    city: str
    country: str
    address: Optional[str] = None
    reg_start: Optional[datetime] = None
    reg_end: Optional[datetime] = None
    genre: Optional[str] = None
    format: Optional[str] = None
    image_url: Optional[str] = None  

class BattleCreate(BattleBase):
    pass

class BattleUpdate(BattleBase):
    pass

class Battle(BattleBase):
    id: int
    created_at: datetime
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None

    class Config:
        orm_mode = True


# class BattleUpdate(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     link: Optional[str] = None
#     date: Optional[datetime] = None
#     city: Optional[str] = None
#     country: Optional[str] = None
#     address: Optional[str] = None
#     reg_start: Optional[datetime] = None
#     reg_end: Optional[datetime] = None
#     genre: Optional[str] = None
#     format: Optional[str] = None
#     image_url: Optional[str] = None
#     updated_at: Optional[datetime] = None  
#     updated_by: Optional[str] = None
