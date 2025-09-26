''' Use case for deleting a category account by ID.'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.category.repository import Repository as CategoryRepository


class Delete:
    '''Use case for deleting a Category account by ID. It interacts with the Category repository to perform the deletion.'''
    def __init__(self):
        self.repo=CategoryRepository()
        self.session_context = SessionContext()

    def handle(self, id:str):
        '''Handles the deletion of a Category account by ID. It uses the repository to perform the deletion within a database session context.'''
        with self.session_context as session:
            return self.repo.delete(session , id)