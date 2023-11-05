from pydantic import BaseModel, Field

class CategoryCreate(BaseModel):
    name: str = Field(min_length=3,alias="Category Name")