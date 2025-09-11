''' Category model for representing a category with an ID and name.'''
from dataclasses import dataclass, asdict
from models.fields_of_activity import FieldsOfActivity

@dataclass
class Category:
    '''Category model representing a category with an ID and name.'''
    id: str = None
    field_of_activity:FieldsOfActivity = None
    name_en: str = None
    name_ar: str = None
    name_fr: str = None

    @classmethod
    def from_dict(cls, self, d):
        '''Create a Category instance from a dictionary.'''
        return self(**d)

    def to_dict(self):
        '''Convert the category instance to a dictionary.'''
        return asdict(self)
