''' UpdateEquipment DTO '''
from flask_restx import Namespace, fields
from models.equipment import Equipment
from models.user import User
from models.brand import Brand
from models.model import Model
from models.city import City
from models.fields_of_activity import FieldsOfActivity
from dto.input.validator import required, valid_string, valid_int, valid_float

class UpdateEquipment:
    ''' Form to update equipment '''
    def __init__(self, json_data):
        self.id = required("id", json_data)
        self.id = valid_string(self.id)

        self.owner_id = required("owner_id", json_data)
        self.owner_id = valid_string(self.owner_id)

        self.pilot_id = required("pilot_id", json_data) 
        self.pilot_id = valid_string(self.pilot_id) 

        self.brand_id = required("brand_id", json_data)
        self.brand_id = valid_string(self.brand_id)

        self.model_id = required("model_id", json_data)
        self.model_id = valid_string(self.model_id)

        self.model_year = required("model_year", json_data)
        self.model_year = valid_int(self.model_year)

        self.construction_year = required("construction_year", json_data)
        self.construction_year = valid_int(self.construction_year)

        self.date_of_customs_clearance = required("date_of_customs_clearance", json_data)
        self.date_of_customs_clearance = valid_int(self.date_of_customs_clearance)

        self.city_id = required("city_id", json_data)
        self.city_id = valid_string(self.city_id)

        self.title = required("title", json_data)
        self.title = valid_string(self.title)

        self.description = required("description", json_data)
        self.description = valid_string(self.description)

        self.price_per_day = required("price_per_day", json_data)
        self.price_per_day = valid_float(self.price_per_day)

        self.is_available = required("is_available", json_data)
        self.is_available = valid_string(self.is_available).lower() == 'true'

        self.fields_of_activity= required("fields_of_activity", json_data)
        self.fields_of_activity = valid_string(self.fields_of_activity)


    def to_domain(self):
        """Converts the form data to an Equipment domain model."""
        return Equipment(
            id=self.id,
            owner=User(id=self.owner_id),
            pilot=User(id=self.pilot_id),
            brand=Brand(id=self.brand_id),
            model=Model(id=self.model_id),
            model_year=self.model_year,
            construction_year=self.construction_year,
            date_of_customs_clearance=self.date_of_customs_clearance,
            city=City(id=self.city_id),
            title=self.title,
            description=self.description,
            price_per_day=self.price_per_day,
            is_available=self.is_available,
            fields_of_activity=FieldsOfActivity.from_string(self.fields_of_activity),
        )


    
    @staticmethod
    def api_model(namespace: Namespace):
        """Returns the API model for the equipment creation form."""
        return namespace.model("CreateEquipment", {
            "id": fields.String(required=True, description="ID of the equipment"),
            "owner_id": fields.String(required=True, description="ID of the owner"),
            "pilot_id": fields.String(required=True, description="ID of the pilot"),
            "brand_id": fields.String(required=True, description="ID of the brand"),
            "model_id": fields.String(required=True, description="ID of the model"),
            "model_year": fields.Integer(required=True, description="Year of the model"),
            "construction_year": fields.Integer(required=True, description="Year of construction"),
            "date_of_customs_clearance": fields.Integer(required=True, description="Date of customs clearance"),
            "city_id": fields.String(required=True, description="ID of the city"),
            "title": fields.String(required=True, description="Title of the equipment"),
            "description": fields.String(required=True, description="Description of the equipment"),
            "price_per_day": fields.Float(required=True, description="Price per day for renting the equipment"),
            "is_available": fields.Boolean(required=True, description="Availability status of the equipment"),
            "fields_of_activity": fields.String(required=True, description="Fields of activity (comma-separated or as a list)"),
        })