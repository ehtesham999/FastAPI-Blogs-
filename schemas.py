from pydantic import BaseModel
from typing import List

class Blogs(BaseModel):
    title: str
    body: str
    user_id: int
            
class User(BaseModel):
    user_name: str
    email: str
    password: str

class BlogResponse(BaseModel):
    id: int
    title: str
    body: str
    class Config:
        from_attributes = True
class UserResponse(BaseModel):
    user_name: str
    email: str
    Blogs : List[BlogResponse]= []
    class Config:
        from_attributes = True
    