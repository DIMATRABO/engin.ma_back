''' This module defines an enumeration for user statuses. '''
from enum import Enum

class UserStatus(str, Enum):
    ''' Enum representing different user statuses in the system. '''
    PENDING = "PENDING"
    ACTIVATED = "ACTIVE"
    BLOCKED = "BLOCKED"
    DELETED ="DELETED"
    def __str__(self):
        return self.value