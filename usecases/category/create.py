'''This module handles the creation of a new category.'''
from models.category import Category
from gateways.category.repository import Repository as CategoryRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    ''' Use case for creating a new category. It checks if the category name is unique and saves the category to the database.'''
    def __init__(self):
        self.repo = CategoryRepository()
        self.session_context = SessionContext()

    def handle(self, category:Category) -> Category:
        '''Handles the creation of a new category. It checks for unique category name and saves the category to the database.'''
        with self.session_context as session:
            saved_category = self.repo.save(session, category)
            return saved_category