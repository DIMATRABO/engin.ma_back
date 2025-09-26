''' Use case for deleting a brand account by ID.'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.brand.repository import Repository as BrandRepository


class Delete:
    '''Use case for deleting a Brand account by ID. It interacts with the Brand repository to perform the deletion.'''
    def __init__(self):
        self.repo=BrandRepository()
        self.session_context = SessionContext()

    def handle(self, id:str):
        '''Handles the deletion of a Brand account by ID. It uses the repository to perform the deletion within a database session context.'''
        with self.session_context as session:
            return self.repo.delete(session , id)