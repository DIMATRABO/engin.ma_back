'''EquipmentResponseForm Data Transfer Object'''
from dataclasses import dataclass, asdict
from datetime import datetime
from models.equipment import Equipment
from models.brand import Brand
from models.model import Model
from models.city import City
from models.fields_of_activity import FieldsOfActivity
from models.equipment_image import EquipmentImage
from typing import Optional, List
from dto.output.user.user_response_form import UserResponseForm

@dataclass
class EquipmentResponseForm:
    id: Optional[str] = None
    owner: Optional[UserResponseForm] = None
    pilot: Optional[UserResponseForm] = None
    brand: Optional[Brand] = None
    model: Optional[Model] = None
    model_year: Optional[int] = None
    construction_year: Optional[int] = None
    date_of_customs_clearance: Optional[int] = None
    city: Optional[City] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price_per_day: Optional[float] = None
    is_available: bool = True
    rating_average: float = 0.0
    fields_of_activity: Optional[FieldsOfActivity] = None
    images: List[EquipmentImage] = None

    def __init__(self, equipment: Equipment):
        self.id = equipment.id
        self.owner = equipment.owner
        self.pilot = equipment.pilot
        self.brand = equipment.brand
        self.model = equipment.model
        self.model_year = equipment.model_year
        self.construction_year = equipment.construction_year
        self.date_of_customs_clearance = equipment.date_of_customs_clearance
        self.city = equipment.city
        self.title = equipment.title
        self.description = equipment.description
        self.price_per_day = float(equipment.price_per_day)
        self.is_available = equipment.is_available
        self.rating_average = float(equipment.rating_average)
        self.fields_of_activity = equipment.fields_of_activity
        self.images = equipment.images if equipment.images else []

    @classmethod
    def from_dict(self, d):
        return self(**d)
    
    def to_dict(self):
        '''Convert the EquipmentResponseForm object to a dictionary.'''
        self.owner = self.owner.to_dict() if self.owner else None
        self.pilot = self.pilot.to_dict() if self.pilot else None
        return asdict(self)
