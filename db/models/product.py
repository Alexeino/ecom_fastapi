from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_model import Model

class Category(Model):
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    
    # Relationship
    products = relationship("Product",back_populates="category")

class Product(Model):
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    price = Column(Integer)
    description = Column(Text,nullable=True)
    created_at = Column(DateTime)
    
    categor_id = Column(Integer,ForeignKey("category.id"))