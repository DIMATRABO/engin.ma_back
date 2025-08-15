
'''This file is part of the Brand Management System project.'''
from models.brand import Brand
from gateways.dataBaseSession.session_context import SessionContext
from gateways.brand.repository import Repository as BrandRepository


class GetById:
    ''' retrieve brand details by id '''
    def __init__(self):
        ''' initialize the GetById use case with a brand repository '''
        self.repo= BrandRepository()
        self.session_context = SessionContext()

    def handle(self, id_:str)->Brand:
        ''' retrieve brand details by id '''
        with self.session_context as session:
            return  self.repo.get_by_id(session, id_)