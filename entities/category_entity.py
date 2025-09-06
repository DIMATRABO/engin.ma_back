''' This module defines the Categoryentity class in the database. '''
from sqlalchemy import Column, String
from models.category import Category
from models.fields_of_activity import FieldsOfActivity

from entities.declarative_base_factory import Base

class CategoryEntity(Base):
    ''' Categoryentity class representing a category in the database. '''
    __tablename__ = "categories"

    id = Column("id", String, primary_key=True)
    field_of_activity = Column("field_of_activity", String, nullable=False)
    name = Column("name", String, nullable= False)

    def __repr__(self):
        return f"<CategoryEntity(id={self.id}, name='{self.name}')>"
    
    def from_domain(self, model: Category):
        ''' Populate the CategoryEntity instance from a domain model. '''
        self.id = model.id
        self.field_of_activity = model.field_of_activity.value if model.field_of_activity else None
        self.name = model.name
    
    def to_domain(self):
        ''' Convert the CategoryEntity instance to a domain model.'''
        return Category(
        id=self.id,
        field_of_activity=FieldsOfActivity(self.field_of_activity),
        name=self.name
        )