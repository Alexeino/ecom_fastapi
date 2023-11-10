from fastapi import APIRouter
from api.v1.routes import product

api_router = APIRouter()
api_router.include_router(product.category_router,prefix="/category",tags=["category"])
api_router.include_router(product.product_router,prefix="/product",tags=["product"])