''' form to create a model '''
from flask_restx import Namespace, fields
from models.model import Model
from models.brand import Brand
from models.category import Category
from dto.input.validator import required, valid_string

class CreateModelForm:
    ''' Form to create a model '''
    def __init__(self , json_model=None):
        if not json_model is None:
            self.name = required("name" , json_model)
            self.name = valid_string(self.name)

            self.brand_id = required("brand_id" , json_model)
            self.brand_id = valid_string(self.brand_id)

            self.category_id = required("category_id" , json_model)
            self.category_id = valid_string(self.category_id)
           


    def to_domain(self):
        """Converts the form data to a Model domain model."""
        return Model(
            id=None,
            name=self.name,
            brand=Brand(id=self.brand_id),
            category=Category(id=self.category_id)
            )
    
    @staticmethod
    def api_model(namespace: Namespace):
        """Returns the API model for the model creation form."""
        return namespace.model("CreateModel", {
            "name": fields.String(required=True, description="Name of the model"),
            "brand_id": fields.String(required=True, description="ID of the brand"),
            "category_id": fields.String(required=True, description="ID of the category")
            })