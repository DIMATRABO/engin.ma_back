''' This module defines the EquipmentEntity class representing an equipment listing in the database. '''
from sqlalchemy import Column, String, Integer, Text, Numeric, Boolean, Float, ForeignKey, TIMESTAMP, func
from models.equipment import Equipment  # Your domain model

from entities.declarative_base_factory import Base

class EquipmentEntity(Base):
    ''' EquipmentEntity class representing a construction machine. '''
    __tablename__ = "equipment"

    id = Column("id", String, primary_key=True)
    owner_id = Column("owner_id", String, ForeignKey("users.id", ondelete="SET NULL"))
    pilot_id = Column("pilot_id", String, ForeignKey("users.id", ondelete="SET NULL"))
    brand_id = Column("brand_id", String, ForeignKey("equipment_brands.id"))
    model_id = Column("model_id", String, ForeignKey("equipment_models.id"))
    model_year = Column("model_year", Integer)
    construction_year = Column("construction_year", Integer)
    date_of_customs_clearance = Column("date_of_customs_clearance", Integer)
    city_id = Column("city_id", String, ForeignKey("cities.id"))
    title = Column("title", String(255))
    description = Column("description", Text)
    price_per_day = Column("price_per_day", Numeric)
    is_available = Column("is_available", Boolean, default=True)
    rating_average = Column("rating_average", Float, default=0.0)
    fields_of_activity = Column("fields_of_activity", Text)
    created_at = Column("created_at", TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<EquipmentEntity(id={self.id}, title='{self.title}', owner_id='{self.owner_id}')>"

    def from_domain(self, model: Equipment):
        ''' Populate the EquipmentEntity instance from a domain model. '''
        self.id = model.id
        self.owner_id = model.owner_id
        self.pilot_id = model.pilot_id
        self.brand_id = model.brand_id
        self.model_id = model.model_id
        self.model_year = model.model_year
        self.construction_year = model.construction_year
        self.date_of_customs_clearance = model.date_of_customs_clearance
        self.city_id = model.city_id
        self.title = model.title
        self.description = model.description
        self.price_per_day = model.price_per_day
        self.is_available = model.is_available
        self.rating_average = model.rating_average
        self.fields_of_activity = model.fields_of_activity
        self.created_at = model.created_at

    def to_domain(self) -> Equipment:
        ''' Convert the EquipmentEntity instance to a domain model. '''
        return Equipment(
            id=self.id,
            owner_id=self.owner_id,
            pilot_id=self.pilot_id,
            brand_id=self.brand_id,
            model_id=self.model_id,
            model_year=self.model_year,
            construction_year=self.construction_year,
            date_of_customs_clearance=self.date_of_customs_clearance,
            city_id=self.city_id,
            title=self.title,
            description=self.description,
            price_per_day=self.price_per_day,
            is_available=self.is_available,
            rating_average=self.rating_average,
            fields_of_activity=self.fields_of_activity,
            created_at=self.created_at
        )
