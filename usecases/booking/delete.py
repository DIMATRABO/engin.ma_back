''' Use case for deleting a booking account by ID.'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepository


class Delete:
    '''Use case for deleting a Booking account by ID. It interacts with the Booking repository to perform the deletion.'''
    def __init__(self):
        self.repo=BookingRepository()
        self.session_context = SessionContext()

    def handle(self, id:str):
        '''Handles the deletion of a Booking account by ID. It uses the repository to perform the deletion within a database session context.'''
        with self.session_context as session:
            return self.repo.delete(session , id)