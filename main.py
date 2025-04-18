from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, create_tables
from base import Base  
from models import Teacher, Class, Subject, Timetable  
from routers import teachers, timetable, subjects

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    create_tables()
    print("Setup complete.")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(teachers.router)
app.include_router(subjects.router)
app.include_router(timetable.router)

@app.get("/")
def root():
    return {"message": "Welcome to school timetable API"}
