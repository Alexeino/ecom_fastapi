from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.product import CategoryCreate
from db.session import get_db
from api.v1.views.product import create_new_category

router = APIRouter()


@router.post("/")
def create_category(category:CategoryCreate, db: Session = Depends(get_db)):
    category = create_new_category(category,db=db)
    return category
    