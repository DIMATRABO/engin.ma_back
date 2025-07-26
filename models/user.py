'''User model for the application.'''
import json
from datetime import datetime
from typing import List
from dataclasses import dataclass, asdict, field
from models.user_role import UserRole
from models.user_status import UserStatus

@dataclass
class User:
    '''User model representing a user in the system.'''
    id: str = None
    username: str = None
    password: str = None
    full_name: str = None
    email: str = None
    birthdate: datetime = None
    address: str = None
    phone_number: str = None
    user_status: UserStatus = None
    roles: List[UserRole] = field(default_factory=list)
    email_verified_at: str =None
    reset_password_otp: str = None
    otp_expiration_date: datetime = None
    created_at: datetime = None

    @classmethod
    def from_dict(cls, self, d):
        '''Create a User instance from a dictionary.'''
        return self(**d)

    def to_dict(self):
        '''Convert the User instance to a dictionary.'''
        self.birthdate = self.birthdate.isoformat() if self.birthdate else None
        d_string = json.dumps(asdict(self))
        d_ = json.loads(d_string)
        d_["user_status"] = None if self.user_status is None else self.user_status.name
        d_["roles"] = None if self.roles is None else self.roles
        d_["password"] = None
        self.otp_expiration_date = self.otp_expiration_date.isoformat() if self.otp_expiration_date else None
        return d_
