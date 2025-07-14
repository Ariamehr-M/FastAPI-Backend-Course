from fastapi import APIRouter, Depends, status
from .. import schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog as blog_repo


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.get_all(db)

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.create(request, db)


@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete(id : int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.destroy(id, db)


@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id : int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.update(id, request, db)



@router.get('/{id}', status_code= 200, response_model=schemas.ShowBlog)
def show(id : int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.show(id, db)