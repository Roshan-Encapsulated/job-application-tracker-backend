from pydantic import EmailStr
from sqlalchemy import Column, Integer, Text, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from . import database
from datetime import datetime
from sqlalchemy import Enum as SqlEnum
from enum import Enum

class ApplicationStatus(str,Enum):
    APPLIED = "APPLIED"
    REJECTED = "REJECTED"
    OFFER = "OFFER"
    INTERVIEW = "INTERVIEW"



# User model (table)
class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    password = Column(Text, nullable=False)

    applications = relationship("Application", back_populates="user")


# Application model (table)
class Application(database.Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(Text, nullable=False)
    role = Column(Text, nullable=False)
    platform = Column(Text, nullable=False)
    experience = Column(Integer, nullable=False)
    applied_at = Column(DateTime, default=datetime.utcnow)
    status = Column(
        SqlEnum(ApplicationStatus),
        default=ApplicationStatus.APPLIED,
        nullable=False
    )
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="applications")
