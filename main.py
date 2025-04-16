from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine
from base import Base  
from models import Teacher, Class, Subject, Timetable  
from database import create_tables
from routers import timetable
 
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app=FastAPI(lifespan=lifespan)
app.include_router(timetable.router)

@app.get("/")
def root():
    return {"message": "Welcome to school timetable API"}