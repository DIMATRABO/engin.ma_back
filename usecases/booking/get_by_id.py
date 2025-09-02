
'''This file is part of the Booking Management System project.'''
from dto.output.booking.booking_response_form import BookingResponseForm
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepository
from usecases.booking.load import Load


class GetById:
    ''' retrieve booking details by id '''
    def __init__(self):
        ''' initialize the GetById use case with a booking repository '''
        self.repo= BookingRepository()
        self.load_usecase = Load()
        self.session_context = SessionContext()

    def handle(self, id_:str)->BookingResponseForm:
        ''' retrieve booking details by id '''
        with self.session_context as session:
            booking = self.repo.get_by_id(session, id_)
            booking = self.load_usecase.handle(session, booking)
            booking = BookingResponseForm(booking)
            return booking