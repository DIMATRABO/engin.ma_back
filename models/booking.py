from dataclasses import dataclass, asdict
from datetime import date, datetime
from typing import Optional
from models.user import User
from models.equipment import Equipment
from models.booking_status import BookingStatus

@dataclass
class Booking:
    ''' Domain model representing a booking. '''
    id: Optional[str]
    client: Optional[User]
    equipment: Optional[Equipment]
    pilot: Optional[User]
    start_date: date
    end_date: date
    status: BookingStatus
    created_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, self, d):
        '''Create a Booking instance from a dictionary.'''
        return self(**d)

    def to_dict(self):
        '''Convert the brand instance to a dictionary.'''
        self.start_date = self.start_date.isoformat() if self.start_date else None
        self.end_date = self.end_date.isoformat() if self.end_date else None
        return asdict(self)
