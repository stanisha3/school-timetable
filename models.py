from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))

class SchoolSettings(Base):
    __tablename__ = "school_settings"
    id = Column(Integer, primary_key=True, index=True)
    working_days = Column(Integer)
    periods_per_day = Column(Integer)
    period_duration_minutes = Column(Integer)
    school_start_time = Column(Integer)
