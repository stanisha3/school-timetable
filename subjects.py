from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Subject
from schemas import SubjectCreate

router = APIRouter(prefix="/subjects", tags=["Subjects"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_subjects(db: Session = Depends(get_db)):
    return db.query(Subject).all()

@router.post("/")
def create_subject(subject_data: SubjectCreate, db: Session = Depends(get_db)):
    new_subject = Subject(**subject_data.dict())
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject
