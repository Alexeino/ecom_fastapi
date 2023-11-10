from sqlalchemy.orm import Session
from schemas.product import CategoryCreate, ProductSchema
from db.models.product import Category, Product
from datetime import datetime

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