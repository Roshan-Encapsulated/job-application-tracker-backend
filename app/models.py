from pydantic import EmailStr
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from . import database


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
    status = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="applications")
