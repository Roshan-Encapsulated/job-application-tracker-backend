#creating pydantic models to input / output
from pydantic import BaseModel,ConfigDict
from pydantic.networks import EmailStr
from typing import Optional
from datetime import datetime

from pydantic import Field
from sqlalchemy import Enum as sqlaEnum
#function to provide the options
from enum import Enum

from sqlalchemy.sql.annotation import Annotated


#model to validate input

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str

#model to user Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#model to return response
class UserResponse(BaseModel):
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class ApplicationCreate(BaseModel):
    company: str
    role:str
    experience:float
    platform:str
    user_id:int

class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    experience: Optional[float] = None
    platform: Optional[str] = None
    applied_day : Optional[datetime] = None
    status: str

    model_config = ConfigDict(from_attributes=True)

class ApplicationforCurrentUser(BaseModel):
    company: str
    role: str
    experience: float
    platform: str

class StatusUpdate(BaseModel):
    status: str

class applicationtoPredict(BaseModel):
    company: str = Field(default="unknown")
    role: str = Field(default="unknown")
    platform: str = Field(default="unknown")
    experience: float = Field(default=0.0)
    applied_day:int = Field(description="Enter 0 for modnay , 1 for tuesday ,... ,6 for sunday",default=0)

class predictResponse(BaseModel):
    success: float
    interpretation: str

