import models


def create_blog(request, db):
    try:
        obj = models.Blog(**request.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except Exception as e:
        return {"error": str(e)}
def list(db):
    try:
        queryset = db.query(models.Blog).all()
        return queryset
    except Exception as e:
        return {"error": str(e)}

def get_blog(id, db):
    try:
        obj = db.query(models.Blog).filter(models.Blog.id == id).first()
        return obj
    except Exception as e:
        return {"error": str(e)}

def delete_blog(id, db):
    try:
        obj = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
        db.commit()
        return {"detail": "Blog deleted"}
    except Exception as e:
        return {"error": str(e)}

def update_blog(id, request, db):
    try:
        obj = db.query(models.Blog).filter(models.Blog.id == id)
        if not obj.first():
            return {"error": "Blog not found"}
        obj.update(request.model_dump())
        db.commit()
        db.refresh(obj.first())
        return obj.first()
    except Exception as e:
        return {"error": str(e)}