from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from repositories.user_repo import userRepo

router = APIRouter()

@router.get("/signup")
def signup (user:user, db:Session=Depends(get_db)):
    user_repo=userRepo(db)
    user_repo.add_user(user)
    return {"message": "user sign up successfully"}

@router.post("/login")
def login():
    return {"message": "user login successfully"}