# Manages the database connection and setup using SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABSE_URL = os.getenv("DATABSE_URL")

engine = create_engine(DATABSE_URL)
SesssionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SesssionLocal()
    try:
        yield db
    finally:
        db.close()