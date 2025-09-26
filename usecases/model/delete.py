''' Use case for deleting a model account by ID.'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.model.repository import Repository as ModelRepository


class Delete:
    '''Use case for deleting a Model account by ID. It interacts with the Model repository to perform the deletion.'''
    def __init__(self):
        self.repo=ModelRepository()
        self.session_context = SessionContext()

    def handle(self, id:str):
        '''Handles the deletion of a Model account by ID. It uses the repository to perform the deletion within a database session context.'''
        with self.session_context as session:
            return self.repo.delete(session , id)