''' This module defines an enumeration for various fields of activity.'''
from enum import Enum

class FieldsOfActivity(str, Enum):
    ''' Enum representing different fields of activity. '''
    CONSTRUCTION = "Construction"
    TRANSPORT = "Transport"
    LIFTING = "Lifting"
    ROADWORKS = "Roadworks"
    AGRICULTURE = "Agriculture"

    def __str__(self):
        return self.value
    @classmethod
    def from_string(cls, value: str):
        ''' Converts a string to a FieldsOfActivity enum member. '''
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid field of activity: {value}")
