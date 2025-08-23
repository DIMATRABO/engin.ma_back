'''This module defines a use case for retrieving all bookings from the database.'''
from models.booking import Booking
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepository


class GetAll:
    def __init__(self):
        self.repo= BookingRepository()
        self.session_context = SessionContext()

    def handle(self)->list[Booking]:
        with self.session_context as session:
            return  self.repo.get_all(session)
          
            


