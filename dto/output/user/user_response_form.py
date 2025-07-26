'''UserResponseForm Data Transfer Object'''
from dataclasses import dataclass, asdict
from datetime import datetime
from models.user import User

@dataclass
class UserResponseForm:
    id: str = None
    name: str = None
    email: str = None
    username:  str = None
    status:  str = None
    location: str = None
    birthday: datetime = None
   

    def __init__(self, user: User):
        self.id = user.id
        self.name = user.full_name
        self.email = user.email
        self.username = user.username
        self.status = user.user_status.value.upper()
        self.location = user.address
        self.birthday = user.birthdate

    @classmethod
    def from_dict(self, d):
        return self(**d)
     
 
    def to_dict(self):
        self.birthday = self.birthday.isoformat() if self.birthday else None
        return asdict(self)
