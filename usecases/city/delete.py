''' Use case for deleting a city account by ID.'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.city.repository import Repository as CityRepository


class Delete:
    '''Use case for deleting a citie account by ID. It interacts with the citie repository to perform the deletion.'''
    def __init__(self):
        self.repo=CityRepository()
        self.session_context = SessionContext()

    def handle(self, id:str):
        '''Handles the deletion of a citie account by ID. It uses the repository to perform the deletion within a database session context.'''
        with self.session_context as session:
            return self.repo.delete(session , id)