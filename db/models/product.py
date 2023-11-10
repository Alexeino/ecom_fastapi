from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_model import Model

class Category(Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False,unique=True)
    
    # Relationship
    products = relationship("Product",back_populates="category")

class Product(Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    price = Column(Integer)
    description = Column(Text,nullable=True)
    created_at = Column(DateTime)
    
    category_id = Column(Integer,ForeignKey("category.id"))
    
    category = relationship("Category",back_populates="products")