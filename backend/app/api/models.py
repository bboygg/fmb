# SQLAlchemy models (database schemas).
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Battle(Base):
    __tablename__ = 'battles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False)
    description = Column(String(255))
    url = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    address = Column(String(255))
    reg_start = Column(DateTime)
    reg_end = Column(DateTime)
    #organizer_id = Column(String, ForeignKey('users.user_id'), nullable=True)
    # organizer_id = Column(String, nullable=True)
    genre = Column(String(100))
    format = Column(String(100))
    image_url = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    updated_by = Column(String(50), nullable=True)

    #organizer = relationship("User", back_populates="organized_battles")

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    role = Column(String(50))
    email = Column(String(100), unique=True, nullable=True)
    tel = Column(String(20), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    updated_by = Column(String(50), nullable=True)

    #organized_battles = relationship("Battle", back_populates="organizer")
