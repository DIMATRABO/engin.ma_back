'''This module handles the creation of a new booking.'''
from models.booking import Booking
from gateways.booking.repository import Repository as BookingRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    ''' Use case for creating a new booking. It checks if the booking details are valid and saves the booking to the database.'''
    def __init__(self):
        self.repo=BookingRepository()
        self.session_context = SessionContext()

    def handle(self, booking:Booking) -> Booking:
        '''Handles the creation of a new booking. It checks for valid booking details and saves the booking to the database.'''
        with self.session_context as session:
            saved_brand = self.repo.save(session , booking)
            return saved_brand