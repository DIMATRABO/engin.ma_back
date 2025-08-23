''' This module defines an enumeration for booking statuses. '''
from enum import Enum

class BookingStatus(str, Enum):
    ''' Enum representing different booking statuses. '''
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

    @classmethod
    def from_string(cls, value: str):
        ''' Converts a string to a BookingStatus enum member. '''
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid booking status: {value}")
        
    def __str__(self):
        return self.value