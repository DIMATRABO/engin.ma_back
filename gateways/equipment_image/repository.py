''' Repository for equipment images management operations.'''
import uuid
from typing import List
from entities.equipment_images_entity import EquipmentImageEntity
from models.equipment_image import EquipmentImage
from gateways.log import Log


logger = Log()
class Repository:
    '''Repository class for managing user data operations.'''
    def save(self, session , equipment_image: EquipmentImage) -> EquipmentImage:
        '''Save a image entity to the database.'''
        logger.debug(f"Saving equipment image: {equipment_image}")
        image_entity = EquipmentImageEntity()
        image_entity.from_domain(image=equipment_image)
        image_entity.id = str(uuid.uuid4())
        session.add(image_entity)
        logger.debug("Image saved successfully")
        return image_entity.to_domain()
    
    def get_all(self, session)->List[EquipmentImage]:
        '''Retrieve all image entities from the database.'''
        images = session.query(EquipmentImage).all()
        return [citie.to_domain() for citie in images]
    
    def get_by_equipment_id(self, session, equipment_id: str) -> List[EquipmentImage]:
        '''Retrieve all images associated with a specific equipment ID.'''
        logger.debug(f"Retrieving images for equipment ID: {equipment_id}")
        images = session.query(EquipmentImageEntity).filter_by(equipment_id=equipment_id).all()
        return [image.to_domain() for image in images]
    
    def delete(self, session, image_id: str) -> None:
        '''Delete an image entity by its ID.'''
        logger.debug(f"Deleting image with ID: {image_id}")
        image_entity = session.query(EquipmentImageEntity).filter_by(id=image_id).first()
        if image_entity:
            session.delete(image_entity)
            logger.debug("Image deleted successfully")
        else:
            logger.warning(f"No image found with ID: {image_id}")