from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from database import Base

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True)

    subjects = relationship("Subject", back_populates="teacher")
    assignments = relationship("Assignment", back_populates="teacher")

class Class(Base):
    __tablename__ = "classes"
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, unique=True)

    timetables = relationship("Timetable", back_populates="class_")
    assignments = relationship("Assignment", back_populates="class_")

class Subject(Base):
    __tablename__ = "subjects"
    id=Column(Integer, primary_key=True, index=True)
    name= Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    teacher = relationship("Teacher", back_populates="subjects")
    timetables = relationship("Timetable", back_populates="subject")
    assignments = relationship("Assignment", back_populates="subject")

class Timetable(Base):
    __tablename__ = "timetables"
    id= Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), index=True)
    day = Column(String)
    period = Column(Integer)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    
    class_ = relationship("Class", back_populates="timetables")
    subject = relationship("Subject", back_populates="timetables")

class Assignment(Base):
    __tablename__ = "assignments"

    id= Column(Integer, primary_key=True, index=True)
    teacher_id= Column(Integer, ForeignKey("teachers.id"))
    class_id= Column(Integer, ForeignKey("classes.id"))
    subject_id= Column(Integer, ForeignKey("subjects.id"))

    teacher = relationship("Teacher", back_populates="assignments")
    class_ = relationship("Class", back_populates="assignments")
    subject = relationship("Subject", back_populates="assignments")


class SchoolSettings(Base):
    __tablename__ = "school_settings"
    
    id = Column(Integer, primary_key=True, index=True)
    working_days = Column(Integer) 
    periods_per_day = Column(Integer)
    period_duration_minutes = Column(Integer)
    school_start_time = Column(Integer) 

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)


