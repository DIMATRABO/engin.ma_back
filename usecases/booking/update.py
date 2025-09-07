''' Use case for updating a booking.'''
from models.booking import Booking
from gateways.booking.repository import Repository as BookingRepository
from gateways.equipment.repository import Repository as EquipmentRepository
from gateways.dataBaseSession.session_context import SessionContext

class Update:
    ''' Use case for updating a booking. '''
    def __init__(self):
        self.repo=BookingRepository()
        self.equipment_repo = EquipmentRepository()
        self.session_context = SessionContext()

    def handle(self, booking:Booking) -> Booking:
        ''' Update a booking in the repository. '''
        with self.session_context as session:
            equipment = self.equipment_repo.get_equipment_by_id(session, booking.equipment.id)
            if equipment is None:
                raise ValueError(f"Equipment with ID {booking.equipment.id} does not exist.")
            booking.unit_price = equipment.price_per_day
            booking.total_price = booking.unit_price * booking.number_of_days
            updated_booking = self.repo.update(session, booking)
            return updated_booking
