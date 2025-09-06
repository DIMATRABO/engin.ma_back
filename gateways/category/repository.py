''' Repository for Category management operations.'''
import uuid
from typing import List
from entities.category_entity import CategoryEntity
from models.category import Category
from gateways.log import Log


logger = Log()
class Repository:
    '''Repository class for managing user data operations.'''
    def __init__(self ):
        '''Initialize the repository.'''
        logger.debug("Repository initialized")

    
    def save(self, session , category: Category) -> Category:
        '''Save a category entity to the database.'''
        logger.debug(f"Saving category: {category}")
        category_entity = CategoryEntity()
        category_entity.from_domain(model=category)
        category_entity.id = str(uuid.uuid4())
        session.add(category_entity)
        logger.debug("Category saved successfully")
        return category_entity.to_domain()
    
    def get_all(self, session)->List[Category]:
        '''Retrieve all category entities from the database.'''
        categories = session.query(CategoryEntity).all()
        return [categorie.to_domain() for categorie in categories]
    
    def get_by_id(self, session, id_: str) -> Category:
        '''Retrieve a category entity by its ID from the database.'''
        logger.debug(f"Retrieving category with ID: {id_}")
        category_entity = session.query(CategoryEntity).filter_by(id=id_).first()
        if not category_entity:
            logger.error(f"Category with ID {id_} not found")
            return None
        return category_entity.to_domain()