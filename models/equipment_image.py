''' EquipmentImage model for storing images related to equipment.'''
from dataclasses import dataclass, asdict

@dataclass
class EquipmentImage:
    ''' EquipmentImage class representing an image associated with an equipment. '''
    id: str
    equipment_id: str
    url: str

@classmethod
def from_dict(cls, self, d):
    '''Create an EquipmentImage instance from a dictionary.'''
    return self(**d)

def to_dict(self):
    '''Convert the equipment image instance to a dictionary.'''
    return asdict(self)

