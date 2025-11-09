from fastapi import FastAPI, Depends
from database import SessionLocal, engine
import models  
from schemas import Blogs

from sqlalchemy.orm import session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.post("/blogs/")
def create_blog(request: Blogs, db: session = Depends(get_db)):
    obj = models.Blog(title = request.title, body = request.body)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
    
@app.get("/blogs/")
def list(db: session = Depends(get_db)):
    queryset = db.query(models.Blog).all()
    return queryset

@app.get("/blogs/{id}")
def get(id: int, db : session = Depends(get_db)):
    obj = db.query(models.Blog).filter(models.Blog.id == id).first()
    return obj

@app.delete("/blogs/{id}")
def delete(id: int, db: session = Depends(get_db)):
    obj = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"detail": "Blog deleted"}

@app.put("/blogs/{id}")
def update(id: int, request: Blogs, db: session = Depends(get_db)):
    obj = db.query(models.Blog).filter(models.Blog.id == id)
    if not obj.first():
        return {"error": "Blog not found"}
    obj.update(request.model_dump())
    db.commit()
    db.refresh(obj.first())
    return obj.first()