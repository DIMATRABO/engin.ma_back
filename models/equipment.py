''' Equipment model for construction machines.'''
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from models.user import User
from models.brand import Brand
from models.model import Model
from models.city import City
from models.fields_of_activity import FieldsOfActivity
from models.equipment_image import EquipmentImage



@dataclass
class Equipment:
    """ Equipment class representing a construction machine. """
    id: str
    owner: Optional[User]
    pilot: Optional[User]
    brand: Brand
    model: Model
    model_year: Optional[int]
    construction_year: Optional[int]
    date_of_customs_clearance: Optional[int]
    city: City
    title: str
    description: str
    price_per_day: float
    is_available: bool = True
    rating_average: float = 0.0
    fields_of_activity: Optional[FieldsOfActivity] = None
    images: List[EquipmentImage] = None
    created_at: Optional[datetime] = None