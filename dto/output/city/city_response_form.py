'''CityResponseForm Data Transfer Object'''
from dataclasses import dataclass
from models.city import City


@dataclass
class CityResponseForm:
    ''' Data Transfer Object for City responses.'''
    id: str = None
    name: str = None


    def __init__(self, city: City, language: str = 'en'):
        self.id = city.id
        if language == 'en':
            self.name = city.name_en
        elif language == 'fr':
            self.name = city.name_fr
        elif language == 'ar':
            self.name = city.name_ar
        else:
            self.name = city.name_en

        
    @classmethod
    def from_dict(self, d):
        ''' Create a CityResponseForm instance from a dictionary. '''
        return self(**d)
     
 
    def to_dict(self):
        ''' Convert the CityResponseForm instance to a dictionary. '''
        return {
            "id": str(self.id),
            "name": self.name if self.name else None,
        }
