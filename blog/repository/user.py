from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status   
from ..hashing import Hash


def create_user(request, db):
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password= hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'User with the id {id} is not available')
    return user