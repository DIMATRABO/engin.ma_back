''' This module defines the EquipmentEntity class representing an equipment listing in the database. '''
from sqlalchemy import Column, String, Integer, Text, Numeric, Boolean, Float, ForeignKey, TIMESTAMP, func
from models.equipment import Equipment
from models.user import User
from models.brand import Brand
from models.model import Model
from models.city import City
from models.fields_of_activity import FieldsOfActivity
from models.category import Category


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
    category_id = Column("category_id", String, ForeignKey("categories.id"))
    created_at = Column("created_at", TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<EquipmentEntity(id={self.id}, title='{self.title}', owner_id='{self.owner_id}')>"

    def from_domain(self, model: Equipment):
        ''' Populate the EquipmentEntity instance from a domain model. '''
        self.id = model.id
        self.owner_id = model.owner.id if model.owner else None
        self.pilot_id = model.pilot.id if model.pilot else None
        self.brand_id = model.brand.id if model.brand else None
        self.model_id = model.model.id if model.model else None
        self.model_year = model.model_year
        self.construction_year = model.construction_year
        self.date_of_customs_clearance = model.date_of_customs_clearance
        self.city_id = model.city.id if model.city else None
        self.title = model.title
        self.description = model.description
        self.price_per_day = model.price_per_day
        self.is_available = model.is_available
        self.rating_average = model.rating_average
        self.fields_of_activity = model.fields_of_activity
        self.category_id = model.category.id if model.category else None
        self.created_at = model.created_at

    def to_domain(self) -> Equipment:
        ''' Convert the EquipmentEntity instance to a domain model. '''
        return Equipment(
            id=self.id,
            owner=User(id = self.owner_id) if self.owner_id else None,
            pilot=User(id = self.pilot_id) if self.pilot_id else None,
            brand= Brand(id=self.brand_id) if self.brand_id else None,
            model= Model(id=self.model_id) if self.model_id else None,
            model_year=self.model_year,
            construction_year=self.construction_year,
            date_of_customs_clearance=self.date_of_customs_clearance,
            city= City(id=self.city_id) if self.city_id else None,
            title=self.title,
            description=self.description,
            price_per_day=self.price_per_day,
            is_available=self.is_available,
            rating_average=self.rating_average,
            fields_of_activity= FieldsOfActivity(name=self.fields_of_activity) if self.fields_of_activity else None,
            category=Category(name=self.category_id) if self.category_id else None,
            images=[],
            created_at=self.created_at
        )
    
    def update_non_null_fields_from_model(self, model: Equipment):
        """Update only non-null fields from a domain model by leveraging from_domain()."""
        temp = EquipmentEntity()
        temp.from_domain(model)  # populate all fields from model

        for column in self.__table__.columns.keys():
            value = getattr(temp, column)
            if value is not None:
                setattr(self, column, value)
