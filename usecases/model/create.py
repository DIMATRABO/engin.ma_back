'''This module handles the creation of a new model.'''
from models.model import Model
from gateways.model.repository import Repository as ModelRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    ''' Use case for creating a new model. It checks if the model name is unique and saves the model to the database.'''
    def __init__(self):
        self.repo=ModelRepository()
        self.session_context = SessionContext()

    def handle(self, model:Model) -> Model:
        '''Handles the creation of a new model. It checks for unique model name and saves the model to the database.'''
        with self.session_context as session:
            saved_model = self.repo.save(session , model)
            return saved_model