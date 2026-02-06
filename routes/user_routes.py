from fastapi import APIRouter

router = APIRouter()

@router.get("/signup")
def signup ():
    return {"message": "user sign up successfully"}

@router.post("/login")
def login():
    return {"message": "user login successfully"}