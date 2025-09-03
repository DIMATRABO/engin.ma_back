'''This module defines a use case for retrieving all bookings from the database.'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepository
from usecases.booking.load import Load
from dto.output.booking.booking_response_form import BookingResponseForm

class GetAll:
    ''' retrieve all bookings use case '''
    def __init__(self):
        self.repo= BookingRepository()
        self.session_context = SessionContext()
        self.load_usecase = Load()

    def handle(self)->list[BookingResponseForm]:
        ''' retrieve all bookings '''
        with self.session_context as session:
            bookings = self.repo.get_all(session)
            results = []
            for booking in bookings:
                booking = self.load_usecase.handle(session, booking)
                results.append(BookingResponseForm(booking))
            return results

