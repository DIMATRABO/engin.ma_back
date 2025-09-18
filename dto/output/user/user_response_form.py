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
    roles:  list = None
    status:  str = None
    address: str = None
    birthday: datetime = None
   

    def __init__(self, user: User):
        self.id = user.id
        self.name = user.full_name
        self.email = user.email
        self.username = user.username
        self.roles = [role.value for  role in user.roles]
        self.status = user.user_status.value.upper()
        self.address = user.address
        self.birthday = user.birthdate

    @classmethod
    def from_dict(self, d):
        return self(**d)
     
 
    def to_dict(self):
        self.birthday = self.birthday.isoformat() if self.birthday else None
        self.roles = [roleEntity.role for roleEntity in self.roles] if self.roles else []
        return asdict(self)
