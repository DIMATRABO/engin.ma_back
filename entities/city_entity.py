''' This module defines the Cityentity class in the database. '''
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.city import City

Base = declarative_base()

class CityEntity(Base):
    ''' Cityentity class representing a city in the database. '''
    __tablename__ = "cities"

    id = Column("id", String, primary_key=True)
    name = Column("name", String, nullable= False)

    def __repr__(self):
        return f"<CityEntity(id={self.id}, name='{self.name}')>"
    
    def from_domain(self, model: City):
        ''' Populate the CityEntity instance from a domain model. '''
        self.id = model.id
        self.name = model.name
    
    def to_domain(self):
        ''' Convert the CityEntity instance to a domain model.'''
        return City(id=self.id, name=self.name)
