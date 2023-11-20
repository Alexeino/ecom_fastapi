from fastapi import APIRouter, Depends
from schemas.user import UserSchema
from db.session import get_db
from sqlalchemy.orm import Session
from api.v1.views.user import create_user_view

user_router = APIRouter()

@user_router.post("/add")
def create_user(user:UserSchema,db:Session = Depends(get_db)):
    user = create_user_view(user=user,db=db)
    return user