from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Teacher
from database import SessionLocal

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

# Function to authenticate teacher
def authenticate_teacher(db: Session, email: str, password: str):
    teacher = get_teacher(db, email)
    if not teacher or not verify_password(password, teacher.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return teacher

# Function to create access token (implementation needed)
def create_access_token(data: dict):
    pass
