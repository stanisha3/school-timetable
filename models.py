from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from base import Base

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    subjects = relationship("Subject", back_populates="teacher")

class Class(Base):
    __tablename__ = "classes"
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, unique=True)

    timetables = relationship("Timetable", back_populates="class_")

class Subject(Base):
    __tablename__ = "subjects"
    id=Column(Integer, primary_key=True, index=True)
    name= Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    teacher = relationship("Teacher", back_populates="subjects")
    timetables = relationship("Timetable", back_populates="subject")

class Timetable(Base):
    __tablename__ = "timetables"
    id= Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), index=True)
    day = Column(String)
    period = Column(Integer)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    
    class_ = relationship("Class", back_populates="timetables")
    subject = relationship("Subject", back_populates="timetables")
