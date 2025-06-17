from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from sqlalchemy import text
from database import SessionLocal, engine
from models import Teacher
from schemas import TeacherCreate, TeacherOut
from typing import List
from auth import oauth2_scheme, decode_access_token, get_password_hash

router = APIRouter(prefix="/teachers", tags=["Teachers"])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TeacherOut])
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()

@router.post("/", response_model=TeacherOut)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    if not teacher.hashed_password:
        raise HTTPException(status_code=400, detail="Password is required")
    hashed_pw = get_password_hash(teacher.hashed_password)
    new_teacher = Teacher(
        name=teacher.name,
        email=teacher.email,
        hashed_password=hashed_pw
    )
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher
