''' This module defines the Modelentity class in the database. '''
from sqlalchemy import Column, String
from models.model import Model
from models.category import Category
from models.brand import Brand
from entities.declarative_base_factory import Base


class ModelEntity(Base):
    ''' Modelentity class representing a model in the database. '''
    __tablename__ = "equipment_models"

    id = Column("id", String, primary_key=True)
    name = Column("name", String, nullable= False)
    brand_id = Column("brand_id", String, nullable=False)
    category_id = Column("category_id", String, nullable=False)

    def __repr__(self):
        return f"<ModelEntity(id={self.id}, name='{self.name}')>"
    
    def from_domain(self, model: Model):
        ''' Populate the ModelEntity instance from a domain model. '''
        self.id = model.id
        self.name = model.name
        self.brand_id = model.brand.id if model.brand else None
        self.category_id = model.category.id if model.category else None

    
    def to_domain(self):
        ''' Convert the ModelEntity instance to a domain model.'''
        return Model(
            id=self.id,
            name=self.name,
            brand=Brand(id=self.brand_id) if self.brand_id else None,
            category=Category(id=self.category_id) if self.category_id else None
        )

