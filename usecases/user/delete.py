''' Use case for deleting a user account by ID.'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepository


class Delete:
    '''Use case for deleting a user account by ID. It interacts with the user repository to perform the deletion.'''
    def __init__(self):
        self.repo=UserRepository()
        self.session_context = SessionContext()

    def handle(self, id:str):
        '''Handles the deletion of a user account by ID. It uses the repository to perform the deletion within a database session context.'''
        with self.session_context as session:
            return self.repo.delete(session , id)