''' Repository for user management operations.'''
import uuid
from typing import List
from entities.model_entity import ModelEntity
from models.model import Model
from gateways.log import Log
from exceptions.exception import NotFoundError

logger = Log()
class Repository:
    '''Repository class for managing user data operations.'''
    def __init__(self ):
        '''Initialize the repository.'''
        logger.debug("Repository initialized")

    
    def save(self, session , model: Model) -> Model:
        '''Save a model entity to the database.'''
        logger.debug(f"Saving model: {model}")
        model_entity = ModelEntity()
        model_entity.from_domain(model=model)
        model_entity.id = str(uuid.uuid4())
        session.add(model_entity)
        logger.debug("Model saved successfully")
        return model_entity.to_domain()
    
    def get_all(self, session)->List[Model]:
        '''Retrieve all model entities from the database.'''
        models = session.query(ModelEntity).all()
        return [citie.to_domain() for citie in models]
    
    def get_by_id(self, session, id_: str) -> Model:
        '''Retrieve a model entity by its ID.'''
        logger.debug(f"Retrieving model by id: {id_}")
        model_entity = session.query(ModelEntity).filter(ModelEntity.id == id_).first()
        if not model_entity:
            logger.error(f"Model with id {id_} not found")
            raise ValueError(f"Model with id {id_} not found")
        return model_entity.to_domain()
    
    def delete(self, session, id_: str) -> bool:
        '''Delete a model entity by its ID.'''
        logger.debug(f"Deleting model by id: {id_}")
        model_entity = session.query(ModelEntity).filter(ModelEntity.id == id_).first()
        if not model_entity:
            logger.error(f"Model with id {id_} not found for deletion")
            raise NotFoundError(f"Model with id {id_} not found for deletion")
        session.delete(model_entity)
        logger.debug("Model deleted successfully")
        return True