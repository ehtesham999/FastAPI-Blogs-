# import router dependencies
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
from schemas import BlogResponse, UserResponse, Blogs, User
from database import get_db
from repository import blogs
from typing import List
from oauth2 import get_current_user
router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", response_model=BlogResponse)
def create_blog(request: Blogs, db: Session = Depends(get_db)):
    return blogs.create_blog(request, db)
    
@router.get("/",  response_model=List[BlogResponse])
def list(db: Session = Depends(get_db)):
    return blogs.list(db)

@router.get("/{id}", response_model=BlogResponse)
def get(id: int, db : Session = Depends(get_db)):
    return blogs.get_blog(id, db)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return blogs.delete_blog(id, db)
   

@router.put("/{id}", response_model=BlogResponse)
def update(id: int, request: Blogs, db: Session = Depends(get_db)):
    return blogs.update_blog(id, request, db)
    