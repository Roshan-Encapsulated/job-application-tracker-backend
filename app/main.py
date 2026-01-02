from fastapi import FastAPI, Depends
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .schemas import UserSignup, ApplicationCreate, ApplicationResponse, UserResponse,ApplicationforCurrentUser
from . import database
from sqlalchemy.orm import Session
from typing import List
from . import crud
from . import database
from . import protectedroutes

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

'''ROOT MESSAGE'''
@app.get("/")
def root():
    return { "message": "Job - Tracker" }


'''USER CREATE AND RETURN USERS'''

#to create a new user
@app.post("/auth/user",response_model = UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user: UserSignup,db: Session = Depends(database.get_db)):
   return crud.create_user(user,db)

#to login into existing user
@app.post("/users/auth/login")
def login_user(data: OAuth2PasswordRequestForm = Depends(),db : Session = Depends(database.get_db)):
    return crud.user_login(data,db)

# to return all the existing users
@app.get("/users", response_model = List[UserResponse])
def get_all_users(db: Session = Depends(database.get_db)):
    return crud.get_all_users(db)

'''APPLICATION CREATE AND RETURN APPLICATIONS'''

#to create a new application
@app.post("/application",response_model = ApplicationResponse,status_code=status.HTTP_201_CREATED)
def create_application(application: ApplicationCreate, db : Session = Depends(database.get_db)):
   return crud.create_application(application,db)

#to print all the existing applications
@app.get("/applications", response_model =List[ApplicationResponse])
def get_all_applications( db : Session = Depends(database.get_db)):
    return crud.get_all_applications(db)



#endpoint of users/{id}/applications
@app.get("/users/{user_id}/applications",response_model = List[ApplicationResponse])
def get_applications_by_user_id(user_id: int, db : Session = Depends(database.get_db)):
    return crud.get_applications_by_user_id(user_id,db)



@app.get("/users/me",response_model=UserResponse)
def read_current_user(user_id : int = Depends(protectedroutes.get_current_user), db : Session = Depends(database.get_db)):
    return crud.read_current_user(user_id,db)


@app.get("/users/applications/me",response_model=List[ApplicationResponse])
def read_current_user_applications(user_id : int = Depends(protectedroutes.get_current_user), db : Session = Depends(database.get_db)):
    return crud.read_current_user_applications(user_id,db)

@app.post("/users/applications/create",response_model = ApplicationResponse)
def create_application_for_current_user(application : ApplicationforCurrentUser,user_id : int = Depends(protectedroutes.get_current_user),db : Session = Depends(database.get_db)):
    return crud.create_application_for_current_user(application,user_id, db)

