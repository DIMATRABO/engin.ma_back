
'''This file is part of the Model Management System project.'''
from models.model import Model
from gateways.dataBaseSession.session_context import SessionContext
from gateways.model.repository import Repository as ModelRepository


class GetById:
    ''' retrieve model details by id '''
    def __init__(self):
        ''' initialize the GetById use case with a model repository '''
        self.repo= ModelRepository()
        self.session_context = SessionContext()

    def handle(self, id_:str)->Model:
        ''' retrieve model details by id '''
        with self.session_context as session:
            return  self.repo.get_by_id(session, id_)