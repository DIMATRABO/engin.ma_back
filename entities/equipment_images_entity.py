''' This module defines the EquipmentImageEntity class representing equipment images in the database. '''

from sqlalchemy import Column, String, ForeignKey
from models.equipment_image import EquipmentImage
from entities.declarative_base_factory import Base



class EquipmentImageEntity(Base):
    ''' EquipmentImageEntity class representing an image associated with an equipment. '''
    __tablename__ = "equipment_images"

    id = Column("id", String, primary_key=True)
    equipment_id = Column("equipment_id", String, ForeignKey('equipment.id', ondelete='CASCADE'))
    url = Column("url", String(500), nullable=False)

    def __repr__(self):
        return f"<EquipmentImageEntity(id={self.id}, equipment_id={self.equipment_id}, url='{self.url}')>"

    def from_domain(self, image: EquipmentImage):
        ''' Populate the entity instance from the domain image. '''
        self.id = image.id
        self.equipment_id = image.equipment_id
        self.url = image.url

    def to_domain(self):
        ''' Convert the entity instance to the domain image. '''
        return EquipmentImage(
            id=self.id,
            equipment_id=self.equipment_id,
            url=self.url
        )
