''' Repository for user management operations.'''
import uuid
from typing import List
from entities.model_entity import ModelEntity
from models.model import Model
from gateways.log import Log


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