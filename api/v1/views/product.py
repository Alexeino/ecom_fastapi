from sqlalchemy.orm import Session
from schemas.product import CategoryCreate, ProductSchema
from db.models.product import Category, Product
from datetime import datetime
from fastapi.exceptions import HTTPException
from fastapi import status

def create_new_category(category: CategoryCreate,db:Session):
    category = Category(
        name= category.name
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def create_new_product(product:ProductSchema, db: Session,category_id:int):
    product = Product(
        name = product.name,
        price = product.price,
        description = product.description,
        created_at = datetime.now(),
        category_id = category_id
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_categories(db:Session):
    cats = db.query(Category).all()
    return cats

def get_category_by_id(id:int,db:Session):
    category = db.query(Category).filter(Category.id == id).first()
    if not category:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return category