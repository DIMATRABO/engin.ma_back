''' Repository for user management operations.'''
import uuid
from typing import List
from entities.brand_entity import BrandEntity
from models.brand import Brand
from gateways.log import Log


logger = Log()
class Repository:
    '''Repository class for managing user data operations.'''
    def __init__(self ):
        '''Initialize the repository.'''
        logger.debug("Repository initialized")

    
    def save(self, session , brand: Brand) -> Brand:
        '''Save a brand entity to the database.'''
        logger.debug(f"Saving brand: {brand}")
        brand_entity = BrandEntity()
        brand_entity.from_domain(model=brand)
        brand_entity.id = str(uuid.uuid4())
        session.add(brand_entity)
        logger.debug("Brand saved successfully")
        return brand_entity.to_domain()
    
    def get_all(self, session)->List[Brand]:
        '''Retrieve all brand entities from the database.'''
        brands = session.query(BrandEntity).all()
        return [citie.to_domain() for citie in brands]
    
    def get_by_id(self, session, id_: str) -> Brand:
        '''Retrieve a brand entity by its ID from the database.'''
        logger.debug(f"Retrieving brand with ID: {id_}")
        brand_entity = session.query(BrandEntity).filter(BrandEntity.id == id_).first()
        if not brand_entity:
            logger.error(f"Brand with ID {id_} not found")
            raise ValueError(f"Brand with ID {id_} not found")
        return brand_entity.to_domain()