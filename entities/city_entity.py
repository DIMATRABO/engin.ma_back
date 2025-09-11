''' This module defines the Cityentity class in the database. '''
from sqlalchemy import Column, String
from models.city import City

from entities.declarative_base_factory import Base

class CityEntity(Base):
    ''' Cityentity class representing a city in the database. '''
    __tablename__ = "cities"

    id = Column("id", String, primary_key=True)
    name_en = Column("name_en", String, nullable= False)
    name_ar = Column("name_ar", String, nullable= False)
    name_fr = Column("name_fr", String, nullable= False)


    def __repr__(self):
        return f"<CityEntity(id={self.id}, name='{self.name}')>"
    
    def from_domain(self, model: City):
        ''' Populate the CityEntity instance from a domain model. '''
        self.id = model.id
        self.name_ar = model.name_ar
        self.name_en = model.name_en
        self.name_fr = model.name_fr
    
    def to_domain(self):
        ''' Convert the CityEntity instance to a domain model.'''
        return City(
            id=self.id,
            name_en=self.name_en,
            name_ar=self.name_ar,
            name_fr=self.name_fr
        )
