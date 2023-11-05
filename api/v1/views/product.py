from sqlalchemy.orm import Session
from schemas.product import CategoryCreate
from db.models.product import Category

def create_new_category(category: CategoryCreate,db:Session):
    category = Category(
        name= category.name
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category