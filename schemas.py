from pydantic import BaseModel, EmailStr
from typing import Optional

class TeacherCreate(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    hashed_password: Optional[str]= None

class ClassCreate(BaseModel):
    name: str 

class SubjectCreate(BaseModel):
    name: str
    teacher_id: int