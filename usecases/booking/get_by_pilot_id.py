
'''This file is part of the Booking Management System project.'''
from typing import List
from models.booking import Booking
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepository


class GetByPilotId:
    ''' retrieve booking details by pilot id use case '''
    def __init__(self):
        ''' initialize the GetByPilotId use case with a booking repository '''
        self.repo= BookingRepository()
        self.session_context = SessionContext()

    def handle(self, pilot_id:str)->List[Booking]:
        ''' retrieve booking details by id '''
        with self.session_context as session:
            return  self.repo.get_by_pilot_id(session, pilot_id)