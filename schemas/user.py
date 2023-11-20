from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import String, Boolean

class UserSchema(BaseModel):
    email: EmailStr
    password: str = Field(...,min_length=4)