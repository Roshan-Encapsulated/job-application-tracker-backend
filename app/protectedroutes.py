
from fastapi.security import OAuth2PasswordBearer
from . import database
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from starlette import status
from fastapi import FastAPI,Depends,HTTPException
from . import models
from . import schemas
from typing import List

SECRET_KEY = "ab307311901d78bb90dda516a7a675e174196c888e2e564224184cb21b8de3c2"
ALGORITHM = "HS256"

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/auth/login")


def get_current_user(token : str = Depends(oauth2_scheme), db : Session = Depends(database.get_db)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = {"Header not Found"})
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = {"Invalid Credentials"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = {"Token may be expired or invalid"})
    return user_id




