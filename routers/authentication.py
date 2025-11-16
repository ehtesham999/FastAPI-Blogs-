
import models
from database import get_db
from hashPassword import check_password
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from oauth2 import create_access_token
router = APIRouter(
    prefix="/authentication",
    tags=["Auhtentication"]
)
@router.post("/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # OAuth2PasswordRequestForm uses "username" field; we treat it as the user's email
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not check_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    # Create JWT token using user's email as subject
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}