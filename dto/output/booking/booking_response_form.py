'''BookingResponseForm Data Transfer Object'''
from dataclasses import dataclass
from datetime import datetime
from models.booking import Booking
from dto.output.user.user_response_form import UserResponseForm
from dto.output.equipment.equipment_response_form import EquipmentResponseForm

@dataclass
class BookingResponseForm:
    ''' Data Transfer Object for booking responses.'''
    id: str = None
    client: UserResponseForm = None
    equipment: EquipmentResponseForm = None
    pilot: UserResponseForm = None
    start_date: datetime = None
    end_date: datetime = None
    number_of_days: int = None
    unit_price: float = None
    total_price: float = None
    status: str = None
    created_at: datetime = None



    def __init__(self, booking: Booking):
        self.id = booking.id
        self.client = UserResponseForm(booking.client) if booking.client else None
        self.equipment = EquipmentResponseForm(booking.equipment) if booking.equipment else None
        self.pilot = UserResponseForm(booking.pilot) if booking.pilot else None
        self.start_date = booking.start_date
        self.end_date = booking.end_date
        self.number_of_days = booking.number_of_days
        self.unit_price = float(booking.unit_price) if booking.unit_price else None
        self.total_price = float(booking.total_price) if booking.total_price else None
        self.status = booking.status.value if booking.status else None
        self.created_at = booking.created_at
        
    @classmethod
    def from_dict(self, d):
        ''' Create a BookingResponseForm instance from a dictionary. '''
        return self(**d)
     
 
    def to_dict(self):
        ''' Convert the BookingResponseForm instance to a dictionary. '''
        return {
            "id": str(self.id),
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "client": self.client.to_dict() if self.client else None,
            "equipment": self.equipment.to_dict() if self.equipment else None,
            "pilot": self.pilot.to_dict() if self.pilot else None,
            "number_of_days": self.number_of_days if self.number_of_days else None,
            "unit_price": self.unit_price if self.unit_price else None,
            "total_price": self.total_price if self.total_price else None,
            "status": self.status if self.status else None,
        }
