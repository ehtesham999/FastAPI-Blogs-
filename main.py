from fastapi import FastAPI
from database import  engine
import models  
from routers import blogs, users


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# register router

app.include_router(blogs.router)
app.include_router(users.router)





