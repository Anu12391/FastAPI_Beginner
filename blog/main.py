from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from blog import models
from blog.database import engine, SessionLocal
from blog.schemas import Blog

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blogschema')
def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.get('/blogall')
def get_all_blog( db: Session = Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

