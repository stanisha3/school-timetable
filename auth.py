from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Teacher
from database import SessionLocal
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "s@22448#!@&"  # Replace with a secure key (use environment variables in production)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Context for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Function to hash password
def get_password_hash(password):
    return pwd_context.hash(password)

# Function to get teacher by email
def get_teacher(db: Session, email: str):
    return db.query(Teacher).filter(Teacher.email == email).first()
    print("Retrieved Teacher:", teacher)  # Debugging: Check if the user is retrieved
    return teacher

# Function to authenticate teacher
def authenticate_teacher(db: Session, email: str, password: str):
    teacher = get_teacher(db, email)
    print("Teacher:", teacher)  # Debugging: Check if the user is retrieved
    if not teacher or not verify_password(password, teacher.hashed_password):
        print("Password verification failed")  # Debugging: Check password verification
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return teacher

# Function to create access token (implementation needed)
def create_access_token(data: dict):
    """
    Create a JWT access token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    """
    Decode and verify a JWT token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )