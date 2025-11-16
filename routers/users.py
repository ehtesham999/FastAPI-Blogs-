from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from hashPassword import hash_password
import models
from repository import users
from schemas import BlogResponse, UserResponse, Blogs, User
from database import get_db
from typing import List
from oauth2 import get_current_user
router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", tags=["Users"], response_model=UserResponse)
def create_user(request: User, db: Session = Depends(get_db)):
    return users.create_user(request, db)
    

@router.get("/", tags=["Users"], response_model= List[UserResponse])
def list_users(db: Session = Depends(get_db)):
   return users.list_users(db)

@router.get("/{id}", tags=["Users"], response_model=UserResponse)
def get_user(id: int, db : Session = Depends(get_db)):
    return users.get_user(id, db)           
    
@router.delete("/{id}", tags=["Users"])
def delete_user(id: int, db: Session = Depends(get_db)):
    return users.delete_user(id, db)