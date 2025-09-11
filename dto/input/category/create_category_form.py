''' form to create a category '''
from flask_restx import Namespace, fields
from models.category import Category
from dto.input.validator import required, valid_string, valid_field_of_activity

class CreateCategoryForm:
    ''' Form to create a category '''
    def __init__(self , json_category=None):
        if not json_category is None:
            self.name_en = required("name_en" , json_category)
            self.name_en = valid_string(self.name_en)

            self.name_fr = required("name_fr" , json_category)
            self.name_fr = valid_string(self.name_fr)

            self.name_ar = required("name_ar" , json_category)
            self.name_ar = valid_string(self.name_ar)
            

            self.field_of_activity = required("field_of_activity" , json_category)
            self.field_of_activity = valid_field_of_activity(self.field_of_activity)
           

    def to_domain(self):
        """Converts the form data to a Category domain model."""
        return Category(
            id=None,
            name_en=self.name_en,
            name_fr=self.name_fr,
            name_ar=self.name_ar,
            field_of_activity=self.field_of_activity
            )
    
    @staticmethod
    def api_model(name_enspace: Namespace):
        """Returns the API model for the category creation form."""
        return name_enspace.model("CreateCategory", {
            "name_en": fields.String(required=True, description="Name of the category"),
            "name_fr": fields.String(required=True, description="Name of the category in French"),
            "name_ar": fields.String(required=True, description="Name of the category in Arabic"),
            "field_of_activity": fields.String(required=True, description="Field of activity of the category (e.g., IT, CONSTRUCTION, AGRICULTURE)")
            })