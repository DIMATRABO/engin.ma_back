''' Use case for updating a booking.'''
from models.booking import Booking
from gateways.booking.repository import Repository as BookingRepository
from gateways.dataBaseSession.session_context import SessionContext

class Update:
    ''' Use case for updating a booking. '''
    def __init__(self):
        self.repo=BookingRepository()
        self.session_context = SessionContext()

    def handle(self, booking:Booking) -> Booking:
        ''' Update a booking in the repository. '''
        with self.session_context as session:
            updated_booking = self.repo.update(session, booking)
            return updated_booking
