from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from blog import models
from blog.database import get_db

from blog.schemas import ShowBlog

router = APIRouter()


@router.get('/blogall', response_model=List[ShowBlog], tags=['blog'])
def get_all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
