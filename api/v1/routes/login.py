from settings.security import create_access_token
from fastapi import Depends, APIRouter,status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.session import get_db
from api.v1.views.user import Hasher, get_user_by_email


login_router = APIRouter()

def authenticate_user(email: str,password: str, db: Session):
    user = get_user_by_email(email=email,db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    
    return user


@login_router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username,form_data.password, db=db)
    if not user:
        raise HTTPException("Details not correct",status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token(data={
        "sub":user.email
    })
    return {
        "access_token":access_token,
        "token_type": "bearer"
    }