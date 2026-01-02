#creating pydantic models to input / output
from pydantic import BaseModel,ConfigDict
from pydantic.networks import EmailStr

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
    status:str
    user_id:int

class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str

    model_config = ConfigDict(from_attributes=True)

class ApplicationforCurrentUser(BaseModel):
    company: str
    role: str
    status: str


