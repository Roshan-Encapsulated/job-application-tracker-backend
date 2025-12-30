#creating pydantic models to input / output
from pydantic import BaseModel,ConfigDict
from pydantic.networks import EmailStr

#model to validate input
class UserCreate(BaseModel):
    name: str
    email: EmailStr

#model to return response
class UserResponse(BaseModel):
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class ApplicationCreate(BaseModel):
    company: str
    role:str
    status:str
    user_id:int

class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str

    model_config = ConfigDict(from_attributes=True)



