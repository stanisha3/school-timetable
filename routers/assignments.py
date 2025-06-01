from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/assignments", tags=["Assignments"])

@router.post("/", response_model=schemas.AssignmentOut)
def create_assignment(data: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    assignment = models.Assignment(**data.dict())
    db.add(assignment)
    db.commit()
    db.refresh(assignment)
    return assignment

@router.get("/", response_model=list[schemas.AssignmentOut])
def get_all_assignments(db: Session = Depends(get_db)):
    return db.query(models.Assignment).all()