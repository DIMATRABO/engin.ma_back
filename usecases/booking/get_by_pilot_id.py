
'''This file is part of the Booking Management System project.'''
from typing import List
from dto.output.booking.booking_response_form import BookingResponseForm
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepository
from usecases.booking.load import Load


class GetByPilotId:
    ''' retrieve booking details by pilot id use case '''
    def __init__(self):
        ''' initialize the GetByPilotId use case with a booking repository '''
        self.repo= BookingRepository()
        self.load_usecase = Load()
        self.session_context = SessionContext()

    def handle(self, pilot_id:str)->List[BookingResponseForm]:
        ''' retrieve booking details by id '''
        with self.session_context as session:
            bookings = self.repo.get_by_pilot_id(session, pilot_id)
            results = []
            for booking in bookings:
                booking = self.load_usecase.handle(session, booking)
                results.append(BookingResponseForm(booking))
            return results