''' City model for representing a city with an ID and name.'''
from dataclasses import dataclass, asdict

@dataclass
class City:
    '''City model representing a city with an ID and name.'''
    id: str = None
    name: str = None

    @classmethod
    def from_dict(cls, self, d):
        return self(**d)

    def to_dict(self):
        '''Convert the city instance to a dictionary.'''
        return asdict(self)
