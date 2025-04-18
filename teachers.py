from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from sqlalchemy import text
from database import SessionLocal, engine
from models import Teacher
from schemas import TeacherCreate
from auth import oauth2_scheme, decode_access_token

router = APIRouter(prefix="/teachers", tags=["Teachers"])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_teachers(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Get all teachers. Requires a valid JWT token.
    """
    # Decode and verify the token (optional)
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return db.query(Teacher).all()

@router.post("/")
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    new_teacher = Teacher(**teacher.dict())  # Ensure you're converting the schema to a model
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher
