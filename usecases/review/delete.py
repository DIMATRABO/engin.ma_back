''' Use case for deleting a review account by ID.'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.review.repository import Repository as ReviewRepository


class Delete:
    '''Use case for deleting a review account by ID. It interacts with the review repository to perform the deletion.'''
    def __init__(self):
        self.repo=ReviewRepository()
        self.session_context = SessionContext()

    def handle(self, id:str):
        '''Handles the deletion of a review account by ID. It uses the repository to perform the deletion within a database session context.'''
        with self.session_context as session:
            return self.repo.delete(session , id)