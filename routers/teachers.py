from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from database import SessionLocal
from models import Teacher
from schemas import TeacherCreate

router = APIRouter(prefix="/teachers", tags=["Teachers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()

@router.post("/")
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    new_teacher = Teacher(**teacher)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher