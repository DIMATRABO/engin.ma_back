''' This module defines an enumeration for user roles in the system. '''
from enum import Enum

class UserRole(str, Enum):
    ''' Enum representing different user roles in the system. '''
    ADMIN = "ADMIN"
    CLIENT = "CLIENT"
    OWNER = "OWNER"
    PILOT = "PILOT"
    def __str__(self):
        return self.value