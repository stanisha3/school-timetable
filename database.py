from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from base import Base

DATABASE_URL= "postgresql://postgres:Stanisha@localhost:5432/timetable_db"

engine= create_engine(DATABASE_URL)
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)


