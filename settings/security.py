from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from settings.config import settings

def create_access_token(data: dict, expires_delta: Optional[timedelta]=timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    
    return encoded_jwt