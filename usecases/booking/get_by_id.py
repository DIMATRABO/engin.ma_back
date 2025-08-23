
'''This file is part of the Booking Management System project.'''
from models.booking import Booking
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepository


class GetById:
    ''' retrieve booking details by id '''
    def __init__(self):
        ''' initialize the GetById use case with a booking repository '''
        self.repo= BookingRepository()
        self.session_context = SessionContext()

    def handle(self, id_:str)->Booking:
        ''' retrieve booking details by id '''
        with self.session_context as session:
            return  self.repo.get_by_id(session, id_)