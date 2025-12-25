import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Optional

load_dotenv()

class User(BaseModel):
    id: int
    username: str
    email: str

class Item(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

app = FastAPI()

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    session = SessionLocal()
    try:
        request.state.db = session
        response = await call_next(request)
    finally:
        session.close()
    return response

@app.get("/users/", response_model=List[User])
async def read_users():
    db = SessionLocal()
    users = db.query(User).all()
    return users

@app.get("/items/", response_model=List[Item])
async def read_items():
    db = SessionLocal()
    items = db.query(Item).all()
    return items