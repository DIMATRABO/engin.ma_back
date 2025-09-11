'''CategoryResponseForm Data Transfer Object'''
from dataclasses import dataclass
from models.category import Category
from models.fields_of_activity import FieldsOfActivity


@dataclass
class CategoryResponseForm:
    ''' Data Transfer Object for Category responses.'''
    id: str = None
    field_of_activity:FieldsOfActivity = None
    name: str = None



    def __init__(self, category: Category, language: str = 'en'):
        self.id = category.id
        self.field_of_activity = category.field_of_activity
        if language == 'en':
            self.name = category.name_en
        elif language == 'fr':
            self.name = category.name_fr
        elif language == 'ar':
            self.name = category.name_ar
        else:
            self.name = category.name_en

        
    @classmethod
    def from_dict(self, d):
        ''' Create a CategoryReaponseForm instance from a dictionary. '''
        return self(**d)
     
 
    def to_dict(self):
        ''' Convert the CategoryResponseForm instance to a dictionary. '''
        return {
            "id": str(self.id),
            "field_of_activity": self.field_of_activity.value if self.field_of_activity else None,
            "name": self.name if self.name else None,
        }
