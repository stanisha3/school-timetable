from pydantic import BaseModel

class TeacherCreate(BaseModel):
    name: str

class ClassCreate(BaseModel):
    name: str 

class SubjectCreate(BaseModel):
    name: str
    teacher_id: int