
'''This file is part of the Category Management System project.'''
from models.category import Category
from gateways.dataBaseSession.session_context import SessionContext
from gateways.category.repository import Repository as CategoryRepository


class GetById:
    ''' retrieve category details by id '''
    def __init__(self):
        ''' initialize the GetById use case with a category repository '''
        self.repo= CategoryRepository()
        self.session_context = SessionContext()

    def handle(self, id_:str)->Category:
        ''' retrieve category details by id '''
        with self.session_context as session:
            return  self.repo.get_by_id(session, id_)