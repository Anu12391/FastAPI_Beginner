from fastapi import FastAPI

from blog import models
from blog.database import engine
from blog.schemas import Blog

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/blogschema')
def create_blog(request: Blog):
    return request
