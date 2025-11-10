import models
from hashPassword import hash_password
from fastapi import HTTPException, status
def create_user(request, db):
    try:
        request.password = hash_password(request.password)
        obj = models.User(**request.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
    
def list_users(db):
    try:
        queryset = db.query(models.User).all()
        return queryset
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
    
def get_user(id, db):
    try:
        obj = db.query(models.User).filter(models.User.id == id).first()
        if not obj:
            raise HTTPException(status_code=404, detail="User not found")
        return obj
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))

def delete_user(id, db):
    try:
        obj = db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
        db.commit()
        return {"detail": "User deleted"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
    