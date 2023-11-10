from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.product import CategoryCreate, ProductSchema
from db.session import get_db
from api.v1.views.product import create_new_category, create_new_product, get_all_categories, get_category_by_id

router = APIRouter()


@router.post("/")
def create_category(category:CategoryCreate, db: Session = Depends(get_db)):
    category = create_new_category(category,db=db)
    return category
    
@router.post("/product/add")
def create_product(product: ProductSchema, db: Session = Depends(get_db),category_id:int = 1):
    product = create_new_product(product=product,
                                 db = db,
                                 category_id=category_id)
    
    return product

@router.get("/categories")
def list_categories(db: Session = Depends(get_db)):
    categories = get_all_categories(db=db)
    return categories

@router.get('/{id}')
def get_category(id:int, db:Session = Depends(get_db)):
    category = get_category_by_id(id=id,db=db)
    return category