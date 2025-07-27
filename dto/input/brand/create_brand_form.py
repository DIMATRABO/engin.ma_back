''' form to create a brand '''
from flask_restx import Namespace, fields
from models.brand import Brand
from dto.input.validator import required, valid_string

class CreateBrandForm:
    ''' Form to create a brand '''
    def __init__(self , json_brand=None):
        if not json_brand is None:
            self.name = required("name" , json_brand)
            self.name = valid_string(self.name)
           


    def to_domain(self):
        """Converts the form data to a Brand domain model."""
        return Brand(
            id=None,
            name=self.name
            )
    
    @staticmethod
    def api_model(namespace: Namespace):
        """Returns the API model for the brand creation form."""
        return namespace.model("CreateBrand", {
            "name": fields.String(required=True, description="Name of the brand")
            })