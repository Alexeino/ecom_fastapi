from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative, Session
from fastapi.exceptions import HTTPException
from fastapi import status

@as_declarative()
class Model:
    id: Any
    __name__: str
    
    @declared_attr
    def __tablename__(cls)->str:
        return cls.__name__.lower()
    
class CRUDMixin:
    
    @classmethod
    def create(cls, db: Session, **kwargs):
        instance = cls(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance
    
    @classmethod
    def delete(cls, db: Session,id: int):
        instance = db.query(cls).filter(cls.id==id).first()
        if instance:
            db.delete(instance)
            db.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Subcategory not found")
    
    @classmethod
    def all(cls, db: Session,):
        
        qs = db.query(cls).all()
        return qs
    
    @classmethod
    def update(cls,id: int, db: Session, **kwargs):
        import pdb; pdb.set_trace()
        instance = db.query(cls).filter(cls.id==id).first()
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{cls.__name__} not found")
        for key, val in kwargs.items():
            setattr(instance,key,val)
        db.commit()
        db.refresh(instance)
        return instance