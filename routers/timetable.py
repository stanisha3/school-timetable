from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from database import SessionLocal
from models import Timetable

router = APIRouter(prefix="/timetable", tags=["Timetable"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_timetable(db: Session = Depends(get_db)):
    return db.query(Timetable).all()

@router.post("/")
def create_entry(entry: dict, db: Session = Depends(get_db)):
                 new_entry= Timetable(**entry)                 
                 db.add(new_entry)
                 db.commit()
                 db.refresh(new_entry)
                 return new_entry

                 



