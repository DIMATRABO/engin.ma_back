''' This module defines the Reviewentity class in the database. '''
from sqlalchemy import Column, String, Integer, Text, DateTime
from models.review import Review

from entities.declarative_base_factory import Base

class ReviewEntity(Base):
    ''' Reviewentity class representing a review in the database. '''
    __tablename__ = "cities"

    id = Column("id", String, primary_key=True)
    client_id = Column("client_id", String)
    equipment_id = Column("equipment_id", String)
    pilot_id = Column("pilot_id", String)
    rating = Column("rating", Integer)
    comment = Column("comment", Text)
    created_at = Column("created_at", DateTime)

    def __repr__(self):
        return f"<ReviewEntity(id={self.id}, client_id={self.client_id}, equipment_id={self.equipment_id}, pilot_id={self.pilot_id}, rating={self.rating}, comment={self.comment}, created_at={self.created_at})>"
    
    def from_domain(self, model: Review):
        ''' Populate the ReviewEntity instance from a domain model. '''
        self.id = model.id
        self.client_id = model.client_id
        self.equipment_id = model.equipment_id
        self.pilot_id = model.pilot_id
        self.rating = model.rating
        self.comment = model.comment
        self.created_at = model.created_at

    
    def to_domain(self):
        ''' Convert the ReviewEntity instance to a domain model.'''
        return Review(
            id=self.id,
            client_id=self.client_id,
            equipment_id=self.equipment_id,
            pilot_id=self.pilot_id,
            rating=self.rating,
            comment=self.comment,
            created_at=self.created_at
        )