''' form to create a category '''
from flask_restx import Namespace, fields
from models.category import Category
from dto.input.validator import required, valid_string, valid_field_of_activity

class CreateCategoryForm:
    ''' Form to create a category '''
    def __init__(self , json_category=None):
        if not json_category is None:
            self.name = required("name" , json_category)
            self.name = valid_string(self.name)

            self.field_of_activity = required("field_of_activity" , json_category)
            self.field_of_activity = valid_field_of_activity(self.field_of_activity)
           

    def to_domain(self):
        """Converts the form data to a Category domain model."""
        return Category(
            id=None,
            name=self.name,
            field_of_activity=self.field_of_activity
            )
    
    @staticmethod
    def api_model(namespace: Namespace):
        """Returns the API model for the category creation form."""
        return namespace.model("CreateCategory", {
            "name": fields.String(required=True, description="Name of the category"),
            "field_of_activity": fields.String(required=True, description="Field of activity of the category (e.g., IT, CONSTRUCTION, AGRICULTURE)")
            })