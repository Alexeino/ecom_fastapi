from fastapi import APIRouter, Depends, exceptions
from sqlalchemy.orm import Session
from typing import Optional

from schemas.product import CategoryCreate, ProductSchema, SubCategorySchema
from db.models.product import SubCategory
from db.session import get_db
from api.v1.views.product import create_new_category, \
create_new_product, get_all_categories, get_category_by_id , \
get_all_products, update_category_by_id

product_router = APIRouter()
category_router = APIRouter()


@category_router.post("/add")
def create_category(category:CategoryCreate, db: Session = Depends(get_db)):
    category = create_new_category(category,db=db)
    return category

@category_router.get("/all_subcat")
def list_subcategories(db:Session = Depends(get_db)):
    subcats = SubCategory.all(db=db)
    return subcats

@category_router.get("/all")
def list_categories(db: Session = Depends(get_db)):
    categories = get_all_categories(db=db)
    return categories

@category_router.get('/{id}')
def get_category(id:int, db:Session = Depends(get_db)):
    category = get_category_by_id(id=id,db=db)
    return category

@category_router.put("/{id}")
def update_category(id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    category = update_category_by_id(id=id,category=category,db=db)
    return category

@category_router.post("/add_subcategory")
def create_subcategory(sub_cat: SubCategorySchema, db:Session = Depends(get_db)):
    obj = SubCategory.create(db=db,**sub_cat.model_dump())
    return obj

@category_router.post("/delete_subcategory/{id}")
def delete_subcategory(id: int,db: Session = Depends(get_db)):
    SubCategory.delete(db=db,id=id)
        
@category_router.put("/update_subcat/{id}")
def update_subcategory(id: int , subcat: SubCategorySchema, db: Session = Depends(get_db)):
    instance = SubCategory.update(db=db,id=id,**subcat.model_dump(exclude_unset=True))
    return instance


# Product Routes

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