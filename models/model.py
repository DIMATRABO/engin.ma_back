''' Model model for representing a model with an ID and name.'''
from dataclasses import dataclass, asdict

@dataclass
class Model:
    '''Model model representing a model with an ID and name.'''
    id: str = None
    name: str = None

    @classmethod
    def from_dict(cls, self, d):
        return self(**d)

    def to_dict(self):
        '''Convert the model instance to a dictionary.'''
        return asdict(self)
