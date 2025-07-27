''' Repository for user management operations.'''
import uuid
from entities.city_entity import CityEntity
from models.city import City
from gateways.log import Log

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