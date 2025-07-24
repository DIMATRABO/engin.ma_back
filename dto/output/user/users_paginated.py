'''Data Transfer Object for paginated user responses.'''
from dataclasses import dataclass, field, asdict
from typing import List
from dto.output.user.user_response_form import UserResponseForm



@dataclass
class UsersPaginated:
    ''' Data Transfer Object for paginated user responses.'''
    total: int
    data: List[UserResponseForm] = field(default_factory=list)
    

    def to_dict(self):
        '''Convert the UsersPaginated object to a dictionary.'''
        self.data = [user.to_dict() for user in self.data]
        return asdict(self)