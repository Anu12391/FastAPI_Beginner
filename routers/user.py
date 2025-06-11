from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from blog.database import get_db
from blog.schemas import User, ShowUser
from repository.user import create, getUser

router = APIRouter(prefix="/user", tags=["user"])


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = create(request, db)
    return new_user


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowUser)
def getuser(id: int, db: Session = Depends(get_db)):
    user = getUser(db, id)
    return user
