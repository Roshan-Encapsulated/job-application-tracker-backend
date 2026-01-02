from fastapi import FastAPI,Depends
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta


SECRET_KEY = "ab307311901d78bb90dda516a7a675e174196c888e2e564224184cb21b8de3c2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

pw_hash_password = CryptContext(schemes=["bcrypt"], deprecated="auto")

#to generate hashed password
def generate_hash_pass(password : str) -> str:
    return pw_hash_password.hash(password)

#to verify the password and hashed password to login the user
def verify_password(plain_password : str, hashed_password : str) -> bool:
    return pw_hash_password.verify(plain_password, hashed_password)

def create_jwt_token(data : dict):
    to_encode = data.copy()
    expiretime = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expiretime})
    return jwt.encode(to_encode,SECRET_KEY, ALGORITHM)

