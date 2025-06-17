from pydantic import BaseModel, EmailStr
from typing import Optional, List

class TeacherCreate(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    hashed_password: Optional[str]= None

class ClassCreate(BaseModel):
    name: str 

class SubjectCreate(BaseModel):
    name: str
    teacher_id: int

class AssignmentBase(BaseModel):
    teacher_id: int
    subject_id: int
    class_id: int

class AssignmentCreate(AssignmentBase):
    pass

class Assignment(AssignmentBase):
    id: int

    class Config:
        orm_mode = True

class SchoolSettingsBase(BaseModel):
    working_days: int
    periods_per_day: int
    period_duration_minutes: int
    school_start_time: int

class SchoolSettingsCreate(SchoolSettingsBase):
    pass

class SchoolSettings(SchoolSettingsBase):
    id: int

    class Config:
        orm_mode = True

class AssignmentCreate(BaseModel):
    teacher_id: int
    subject_id: int
    class_id: int

class AssignmentOut(AssignmentCreate):
    id: int

    class Config:
        from_attribute = True

class TeacherOut(BaseModel):
    id: int
    name: str
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True