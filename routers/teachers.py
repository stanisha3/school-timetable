from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from sqlalchemy import text
from database import SessionLocal, engine
from models import Teacher
from schemas import TeacherCreate

router = APIRouter(prefix="/teachers", tags=["Teachers"])

def alter_teachers_table():
    print("Running alter table for teachers...")
    try:
        with engine.begin() as conn:
            conn.execute(text(""" ALTER TABLE teachers ADD COLUMN IF NOT EXISTS email VARCHAR UNIQUE; """))
            conn.execute(text(""" ALTER TABLE teachers ADD COLUMN IF NOT EXISTS hashed_password VARCHAR;"""))
        print("✅ Alteration complete.")
    except Exception as e:
        print("❌ Error during ALTER:", e)


alter_teachers_table()

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
    new_teacher = Teacher(**teacher.dict())  # Ensure you're converting the schema to a model
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher
