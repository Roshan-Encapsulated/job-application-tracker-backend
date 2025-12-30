from fastapi import HTTPException,Depends
from models import User,Application
from schemas import UserCreate,ApplicationCreate
from sqlalchemy.orm import Session
from starlette import status



def create_user(user: UserCreate,db: Session):
   # pydantic will return a dictionary so we need to convert it into an object in order to
   # fit that into our database via sqlalchemy
   ifuserexist = db.query(User).filter(User.email == user.email).first()

   if ifuserexist:
       raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

   newuser = User(name=user.name, email=user.email)
   db.add(newuser)
   db.commit()
   db.refresh(newuser)
   return newuser

def get_all_users(db: Session):
    users = db.query(User).all()
    return users




def create_application(application: ApplicationCreate,db : Session):

    ifapplicationexist = db.query(Application).filter(
        Application.company == application.company,
        Application.role == application.role,
        Application.user_id == application.user_id
    ).first()

    if ifapplicationexist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Application already exists")

    newapplication = Application(company=application.company, role=application.role, status = application.status, user_id = application.user_id)

    db.add(newapplication)
    db.commit()
    db.refresh(newapplication)
    return newapplication

def get_all_applications( db : Session):
     applications = db.query(Application).all()
     return applications



def get_applications_by_user_id(user_id: int, db : Session):
     user = db.query(User).filter(user_id == User.id).first()
     if not user:
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="User does not exist")

     return user.applications