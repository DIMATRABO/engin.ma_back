''' City model for representing a city with an ID and name.'''
from dataclasses import dataclass, asdict

@dataclass
class City:
    '''City model representing a city with an ID and name.'''
    id: str = None
    name_en: str = None
    name_ar: str = None
    name_fr: str = None

    @classmethod
    def from_dict(cls, self, d):
        '''Create a City instance from a dictionary.'''
        return self(**d)

    def to_dict(self):
        '''Convert the city instance to a dictionary.'''
        return asdict(self)
