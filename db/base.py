# List all model as imports here to enable alembic to detect them
from db.base_model import Model
# from db.models.example import Example
from db.models.product import Product, Category, SubCategory
from db.models.users import User