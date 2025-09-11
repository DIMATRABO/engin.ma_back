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
    name_en = Column("name_en", String, nullable= False)
    name_ar = Column("name_ar", String, nullable= False)
    name_fr = Column("name_fr", String, nullable= False)

    def __repr__(self):
        return f"<CategoryEntity(id={self.id}, name='{self.name}')>"
    
    def from_domain(self, model: Category):
        ''' Populate the CategoryEntity instance from a domain model. '''
        self.id = model.id
        self.field_of_activity = model.field_of_activity.value if model.field_of_activity else None
        self.name_ar = model.name_ar
        self.name_en = model.name_en
        self.name_fr = model.name_fr
    
    def to_domain(self):
        ''' Convert the CategoryEntity instance to a domain model.'''
        return Category(
        id=self.id,
        field_of_activity=FieldsOfActivity(self.field_of_activity),
        name_ar=self.name_ar,
        name_en=self.name_en,
        name_fr=self.name_fr
        )