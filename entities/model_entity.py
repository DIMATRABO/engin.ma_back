''' This module defines the Modelentity class in the database. '''
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.model import Model

Base = declarative_base()

class ModelEntity(Base):
    ''' Modelentity class representing a model in the database. '''
    __tablename__ = "equipment_models"

    id = Column("id", String, primary_key=True)
    name = Column("name", String, nullable= False)

    def __repr__(self):
        return f"<ModelEntity(id={self.id}, name='{self.name}')>"
    
    def from_domain(self, model: Model):
        ''' Populate the ModelEntity instance from a domain model. '''
        self.id = model.id
        self.name = model.name
    
    def to_domain(self):
        ''' Convert the ModelEntity instance to a domain model.'''
        return Model(id=self.id, name=self.name)
