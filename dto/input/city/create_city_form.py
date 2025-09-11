''' form to create a city '''
from flask_restx import Namespace, fields
from models.city import City
from dto.input.validator import required, valid_string

class CreateCityForm:
    ''' Form to create a city '''
    def __init__(self , json_city=None):
        if not json_city is None:
            self.name_en = required("name_en" , json_city)
            self.name_en = valid_string(self.name_en)

            self.name_fr = required("name_fr" , json_city)
            self.name_fr = valid_string(self.name_fr)

            self.name_ar = required("name_ar" , json_city)
            self.name_ar = valid_string(self.name_ar)


    def to_domain(self):
        """Converts the form data to a City domain model."""
        return City(
            id=None,
            name_en=self.name_en,
            name_fr=self.name_fr,
            name_ar=self.name_ar
            )
    
    @staticmethod
    def api_model(name_enspace: Namespace):
        """Returns the API model for the city creation form."""
        return name_enspace.model("CreateCity", {
            "name_en": fields.String(required=True, description="Name of the city in English"),
            "name_fr": fields.String(required=True, description="Name of the city in French"),
            "name_ar": fields.String(required=True, description="Name of the city in Arabic"),
            })