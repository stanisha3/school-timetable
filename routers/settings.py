from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
import models, schemas
from models import SchoolSettings

router = APIRouter(prefix="/settings", tags=["Settings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def save_settings(data: dict, db: Session = Depends(get_db)):
    settings= db.query(SchoolSettings). first()
    if settings:
        for key, value in data.items():
            setattr(settings, key, value)
    else:
        settings = SchoolSettings(**data)
        db.add(settings)
    db.commit()
    return {"message": "Settings saved successfully"}