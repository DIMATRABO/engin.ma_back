''' form to create a model '''
from flask_restx import Namespace, fields
from models.model import Model
from dto.input.validator import required, valid_string

class CreateModelForm:
    ''' Form to create a model '''
    def __init__(self , json_model=None):
        if not json_model is None:
            self.name = required("name" , json_model)
            self.name = valid_string(self.name)
           


    def to_domain(self):
        """Converts the form data to a Model domain model."""
        return Model(
            id=None,
            name=self.name
            )
    
    @staticmethod
    def api_model(namespace: Namespace):
        """Returns the API model for the model creation form."""
        return namespace.model("CreateModel", {
            "name": fields.String(required=True, description="Name of the model")
            })