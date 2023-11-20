from fastapi import APIRouter
from api.v1.routes import product, user, login

api_router = APIRouter()
api_router.include_router(product.category_router,prefix="/category",tags=["category"])
api_router.include_router(product.product_router,prefix="/product",tags=["product"])
api_router.include_router(user.user_router,prefix="/user",tags=["user"])
api_router.include_router(login.login_router,prefix="/login",tags=["login"])