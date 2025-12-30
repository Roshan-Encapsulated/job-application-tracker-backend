from fastapi import FastAPI, Depends
from starlette import status

from schemas import UserCreate, ApplicationCreate, ApplicationResponse, UserResponse
from database import get_db
from sqlalchemy.orm import Session
from typing import List
import crud

from database import engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

'''ROOT MESSAGE'''
@app.get("/")
def root():
    return { "message": "Job - Tracker" }


'''USER CREATE AND RETURN USERS'''

#to create a new user
@app.post("/user",response_model = UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate,db: Session = Depends(get_db)):
   return crud.create_user(user,db)

# to return all the existing users
@app.get("/users", response_model = List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

'''APPLICATION CREATE AND RETURN APPLICATIONS'''

#to create a new application
@app.post("/application",response_model = ApplicationResponse,status_code=status.HTTP_201_CREATED)
def create_application(application: ApplicationCreate, db : Session = Depends(get_db)):
   return crud.create_application(application,db)

#to print all the existing applications
@app.get("/applications", response_model =List[ApplicationResponse])
def get_all_applications( db : Session = Depends(get_db)):
    return crud.get_all_applications(db)



#endpoint of users/{id}/applications
@app.get("/users/{user_id}/applications",response_model = List[ApplicationResponse])
def get_applications_by_user_id(user_id: int, db : Session = Depends(get_db)):
    return crud.get_applications_by_user_id(user_id,db)