'''Pilote Simple Data Transfer Object'''
from dataclasses import dataclass, asdict
from models.user import User

@dataclass
class UserSimple:
    id: str = None
    full_name: str = None
    username:  str = None


    def __init__(self, user: User):
        self.id = user.id
        self.full_name = user.full_name
        self.username = user.username


    @classmethod
    def from_dict(self, d):
        return self(**d)
     
 
    def to_dict(self):
        return asdict(self)
