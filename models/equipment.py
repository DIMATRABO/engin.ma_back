''' Equipment model for construction machines.'''
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class Equipment:
    """ Equipment class representing a construction machine. """
    id: str
    owner_id: Optional[str]
    pilot_id: Optional[str]
    brand_id: str
    model_id: str
    model_year: Optional[int]
    construction_year: Optional[int]
    date_of_customs_clearance: Optional[int]
    city_id: str
    title: str
    description: str
    price_per_day: float
    is_available: bool = True
    rating_average: float = 0.0
    fields_of_activity: Optional[str] = None  # Can be comma-separated or converted to Enum/List
    images: List[str] = None
    created_at: Optional[datetime] = None