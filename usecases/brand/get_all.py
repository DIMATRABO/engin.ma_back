'''This module defines a use case for retrieving all brands from the database.'''
from models.brand import Brand
from gateways.dataBaseSession.session_context import SessionContext
from gateways.brand.repository import Repository as BrandRepository


class GetAll:
    def __init__(self):
        self.repo= BrandRepository()
        self.session_context = SessionContext()

    def handle(self)->list[Brand]:
        with self.session_context as session:
            return  self.repo.get_all(session)
          
            


