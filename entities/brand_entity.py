''' This module defines the Brandentity class in the database. '''
from sqlalchemy import Column, String
from models.brand import Brand
from entities.declarative_base_factory import Base


class BrandEntity(Base):
    ''' Brandentity class representing a brand in the database. '''
    __tablename__ = "equipment_brands"

    id = Column("id", String, primary_key=True)
    name = Column("name", String, nullable= False)

    def __repr__(self):
        return f"<BrandEntity(id={self.id}, name='{self.name}')>"
    
    def from_domain(self, model: Brand):
        ''' Populate the BrandEntity instance from a domain model. '''
        self.id = model.id
        self.name = model.name
    
    def to_domain(self):
        ''' Convert the BrandEntity instance to a domain model.'''
        return Brand(id=self.id, name=self.name)
