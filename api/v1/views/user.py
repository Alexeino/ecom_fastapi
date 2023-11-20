from passlib.context import CryptContext
from schemas.user import UserSchema
from sqlalchemy.orm import Session
from db.models.users import User

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


class Hasher:
    
    @staticmethod
    def verify_password(plain_pwd,hashed_pwd):
        return pwd_context.verify(plain_pwd,hashed_pwd)

    
    @staticmethod
    def get_pwd_hash(pwd):
        return pwd_context.hash(pwd)
    
def create_user_view(user: UserSchema, db: Session):
    pwd_hash = Hasher.get_pwd_hash(user.password)
    user = User(
        email = user.email,
        password = pwd_hash
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user