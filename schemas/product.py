from pydantic import BaseModel, Field, root_validator
from typing import Text, Optional

class CategoryCreate(BaseModel):
    name: str = Field(min_length=3,alias="Category Name")
    
class ProductSchema(BaseModel):
    name: str = Field(min_length=3,alias="Product Name")
    price: int = Field(gt=0)
    description: Optional[str] = None
    
    class config():
        orm_mode = True