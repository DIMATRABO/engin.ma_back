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
from models.category import Category



@dataclass
class Equipment:
    """ Equipment class representing a construction machine. """
    id: str
    owner: Optional[User] = None
    pilot: Optional[User] = None
    brand: Brand = None
    model: Model = None 
    model_year: Optional[int] = None 
    construction_year: Optional[int] = None
    date_of_customs_clearance: Optional[int] = None
    city: City = None
    title: str = None
    description: str = None
    price_per_day: float = 0.0
    is_available: bool = True
    rating_average: float = 0.0
    fields_of_activity: Optional[FieldsOfActivity] = None
    category: Optional[Category] = None
    images: List[EquipmentImage] = None
    created_at: Optional[datetime] = None