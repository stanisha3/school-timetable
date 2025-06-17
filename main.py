from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, create_tables
from base import Base  
from models import Teacher, Class, Subject, Timetable  
from routers import teachers, timetable, subjects, assignments, users 
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    create_tables()
    print("Setup complete.")
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teachers.router)
app.include_router(subjects.router)
app.include_router(timetable.router)
app.include_router(assignments.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to school timetable API"}
