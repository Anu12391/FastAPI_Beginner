from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import models
from blog.schemas import Blog


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(db: Session,id:int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this {id} is not found")
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return 'done'

def update_blog(db: Session,id:int,request: Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this {id} is not found")

    else:
        blog.update({'title': request.title, 'body': request.body})
        db.commit()
        return 'updated'


def getBlogById(db: Session,id:int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'error_response': f'Blog with this {id} not found'}
    return blog