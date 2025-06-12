from typing import List

from fastapi import APIRouter
from fastapi import Response
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from blog.database import get_db
from blog.schemas import Blog, ShowBlog, User
from repository.blog import get_all, create, delete, update_blog, getBlogById
from routers.oauth2 import get_current_user

router = APIRouter(prefix="/blog", tags=['blog'])


@router.get('/', response_model=List[ShowBlog] )
def get_all_blog(db: Session = Depends(get_db),current_user:User=Depends(get_current_user)):
    blogs = get_all(db)
    return blogs


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = create(request, db)
    return new_blog


@router.get('/{id}', status_code=200, response_model=ShowBlog)
def get_blog_by_id(id: int, response: Response, db: Session = Depends(get_db)):
    blog = getBlogById(db, id)
    return blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    deleteBlogResp = delete(db, id)
    return deleteBlogResp


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: Blog, db: Session = Depends(get_db)):
    blogUpdatedResp = update_blog(db, id, request)
    return blogUpdatedResp
