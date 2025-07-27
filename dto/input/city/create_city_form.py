''' form to create a city '''
from flask_restx import Namespace, fields
from models.city import City
from dto.input.validator import required, valid_string

class CreateCityForm:
    ''' Form to create a city '''
    def __init__(self , json_city=None):
        if not json_city is None:
            self.name = required("name" , json_city)
            self.name = valid_string(self.name)
           


    def to_domain(self):
        """Converts the form data to a City domain model."""
        return City(
            id=None,
            name=self.name
            )
    
    @staticmethod
    def api_model(namespace: Namespace):
        """Returns the API model for the city creation form."""
        return namespace.model("CreateCity", {
            "name": fields.String(required=True, description="Name of the city")
            })