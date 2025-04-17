from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Class
from schemas import ClassCreate

router = APIRouter(prefix="/classes", tags=["Classes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_classes(db: Session = Depends(get_db)):
    return db.query(Class).all()

@router.post("/")
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    new_class = Class(**class_data.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class
