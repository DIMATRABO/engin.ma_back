''' Repository for user management operations.'''
import uuid
from typing import List
from entities.city_entity import CityEntity
from models.city import City
from gateways.log import Log
from exceptions.exception import NotFoundException


logger = Log()
class Repository:
    '''Repository class for managing user data operations.'''
    def __init__(self ):
        '''Initialize the repository.'''
        logger.debug("Repository initialized")

    
    def save(self, session , city: City) -> City:
        '''Save a city entity to the database.'''
        logger.debug(f"Saving city: {city}")
        city_entity = CityEntity()
        city_entity.from_domain(model=city)
        city_entity.id = str(uuid.uuid4())
        session.add(city_entity)
        logger.debug("City saved successfully")
        return city_entity.to_domain()
    
    def get_all(self, session)->List[City]:
        '''Retrieve all city entities from the database.'''
        cities = session.query(CityEntity).all()
        return [citie.to_domain() for citie in cities]
    
    def get_by_id(self, session, id_: str) -> City:
        '''Retrieve a city entity by its ID from the database.'''
        logger.debug(f"Retrieving city with ID: {id_}")
        city_entity = session.query(CityEntity).filter_by(id=id_).first()
        if not city_entity:
            logger.error(f"City with ID {id_} not found")
            return None
        return city_entity.to_domain()
    
    def delete(self, session, id_: str) -> bool:
        '''Delete a city entity by its ID from the database.'''
        logger.debug(f"Deleting city with ID: {id_}")
        city_entity = session.query(CityEntity).filter_by(id=id_).first()
        if not city_entity:
            logger.error(f"City with ID {id_} not found")
            raise NotFoundException(f"City with ID {id_} not found")
        session.delete(city_entity)
        logger.debug("City deleted successfully")
        return True