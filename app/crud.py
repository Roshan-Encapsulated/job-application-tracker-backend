from fastapi import HTTPException,Depends
from . import models
from . import schemas
from sqlalchemy.orm import Session
from starlette import status
from . import security
from fastapi.security import OAuth2PasswordRequestForm
from ml.predictor import predict


def create_user(user: schemas.UserSignup,db: Session):
   # pydantic will return a dictionary so we need to convert it into an object in order to
   # fit that into our database via sqlalchemy
   ifuserexist = db.query(models.User).filter(models.User.email == user.email).first()

   if ifuserexist:
       raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

   hashed_pass = security.generate_hash_pass(user.password)
   newuser = models.User(name=user.name, email=user.email,password=hashed_pass)
   db.add(newuser)
   db.commit()
   db.refresh(newuser)
   return newuser


def user_login(data: OAuth2PasswordRequestForm, db: Session):
    existinguser = db.query(models.User).filter(models.User.email == data.username).first()

    if not existinguser:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")

    ifpasswordmatch = security.verify_password(data.password, existinguser.password)

    if not ifpasswordmatch:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    payload = {"id": existinguser.id}
    accesstoken = security.create_jwt_token(payload)

    return {
        "access_token": accesstoken,
        "token_type": "bearer",
    }

def get_all_users(db: Session):
    users = db.query(models.User).all()
    return users




def create_application(application: schemas.ApplicationCreate,db : Session):

    ifapplicationexist = db.query(models.Application).filter(
        models.Application.company == application.company,
        models.Application.role == application.role,
        models.Application.user_id == application.user_id
    ).first()

    if ifapplicationexist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Application already exists")

    newapplication = models.Application(company=application.company, role=application.role, experience = application.experience,platform=application.platform, user_id = application.user_id)

    db.add(newapplication)
    db.commit()
    db.refresh(newapplication)
    return newapplication

def get_all_applications( db : Session):
     applications = db.query(models.Application).all()
     return applications



def get_applications_by_user_id(user_id: int, db : Session):
     user = db.query(models.User).filter(user_id == models.User.id).first()
     if not user:
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="User does not exist")

     return user.applications


#there are the protected routes
def read_current_user(user_id : int, db : Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


def read_current_user_applications(user_id : int, db : Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user.applications


def create_application_for_current_user(application: schemas.ApplicationforCurrentUser,user_id : int , db : Session):
    id = user_id
    ifapplicationexists = db.query(models.Application).filter(models.Application.company == application.company,models.Application.role == application.role,models.Application.status == application.status,models.Application.user_id == user_id).first()
    if ifapplicationexists:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Application already exists")

    newapplication = models.Application(company=application.company, role=application.role, experience = application.experience, user_id = id)

    db.add(newapplication)
    db.commit()
    db.refresh(newapplication)
    return newapplication

def update_status(application_id : int, newstatus : schemas.StatusUpdate, user_id :int, db : Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    application = db.query(models.Application).filter(models.Application.id == application_id).first()
    application.status = newstatus.status
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


def predict_success(application : schemas.applicationtoPredict):
    probability = predict(application.dict())

    if probability >= 0.7:
        interpretation = "High Chance"
    elif probability >= 0.5:
        interpretation = "Moderate Chance"
    else:
        interpretation = "Low Chance"

    dict = {
        "success": probability,
         "interpretation": interpretation,
    }
    return dict



