'''This module handles the creation of a new booking.'''
from models.booking import Booking
from gateways.booking.repository import Repository as BookingRepository
from gateways.equipment.repository import Repository as EquipmentRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    ''' Use case for creating a new booking. It checks if the booking details are valid and saves the booking to the database.'''
    def __init__(self):
        self.repo=BookingRepository()
        self.equipment_repo = EquipmentRepository()
        self.session_context = SessionContext()

    def handle(self, booking:Booking) -> Booking:
        '''Handles the creation of a new booking. It checks for valid booking details and saves the booking to the database.'''
        with self.session_context as session:
            equipment = self.equipment_repo.get_equipment_by_id(session, booking.equipment.id)
            if equipment is None:
                raise ValueError(f"Equipment with ID {booking.equipment.id} does not exist.")
            booking.unit_price = equipment.price_per_day
            booking.total_price = booking.unit_price * booking.number_of_days
            saved_brand = self.repo.save(session , booking)
            return saved_brand