from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth import authenticate_teacher, create_access_token
from models import Teacher
from routers.teachers import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Login endpoint to authenticate a teacher and return a JWT token.
    """
    teacher = authenticate_teacher(db, form_data.username, form_data.password)
    access_token = create_access_token(data={"sub": teacher.email})
    return {"access_token": access_token, "token_type": "bearer"}