from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from schemas.product import CategoryCreate, ProductSchema
from db.session import get_db
from api.v1.views.product import create_new_category, \
create_new_product, get_all_categories, get_category_by_id , \
get_all_products

product_router = APIRouter()
category_router = APIRouter()


@category_router.post("/add")
def create_category(category:CategoryCreate, db: Session = Depends(get_db)):
    category = create_new_category(category,db=db)
    return category

@category_router.get("/all")
def list_categories(db: Session = Depends(get_db)):
    categories = get_all_categories(db=db)
    return categories

@category_router.get('/{id}')
def get_category(id:int, db:Session = Depends(get_db)):
    category = get_category_by_id(id=id,db=db)
    return category


@product_router.post("/add")
def create_product(product: ProductSchema, db: Session = Depends(get_db),category_id:int = 1):
    product = create_new_product(product=product,
                                 db = db,
                                 category_id=category_id)
    
    return product

@product_router.get("/all",name="Get Products or By ID",description="Endpoint to Get All or Single Product by ID")
def list_products(db:Session = Depends(get_db),id: Optional[int]=None):
    products = get_all_products(db=db,id = id)
    return products