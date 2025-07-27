''' Brand model for representing a brand with an ID and name.'''
from dataclasses import dataclass, asdict

@dataclass
class Brand:
    '''Brand model representing a brand with an ID and name.'''
    id: str = None
    name: str = None

    @classmethod
    def from_dict(cls, self, d):
        return self(**d)

    def to_dict(self):
        '''Convert the brand instance to a dictionary.'''
        return asdict(self)
