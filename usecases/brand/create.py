'''This module handles the creation of a new brand.'''
from models.brand import Brand
from gateways.brand.repository import Repository as BrandRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    ''' Use case for creating a new brand. It checks if the brand name is unique and saves the brand to the database.'''
    def __init__(self):
        self.repo=BrandRepository()
        self.session_context = SessionContext()

    def handle(self, brand:Brand) -> Brand:
        '''Handles the creation of a new brand. It checks for unique brand name and saves the brand to the database.'''
        with self.session_context as session:
            saved_brand = self.repo.save(session , brand)
            return saved_brand