from fastapi import FastAPI

from blog.schemas import Blog

app = FastAPI()

@app.post('/blogschema')
def create_blog(request: Blog):
    return request
