
'''This file is part of the Booking Management System project.'''
from typing import List
from models.booking import Booking
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepository


class GetByEquipmentId:
    ''' retrieve booking details by equipment id use case '''
    def __init__(self):
        ''' initialize the GetByEquipmentId use case with a booking repository '''
        self.repo= BookingRepository()
        self.session_context = SessionContext()

    def handle(self, equipment_id:str)->List[Booking]:
        ''' retrieve booking details by id '''
        with self.session_context as session:
            return  self.repo.get_by_equipment_id(session, equipment_id)