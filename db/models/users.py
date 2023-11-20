from db.base_model import Model
from sqlalchemy import Column, Integer, String, Boolean

class User(Model):
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    email = Column(String,nullable=False,unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean,default=True)

    