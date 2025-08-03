'''This module handles the creation of a new model.'''
from models.equipment_image import EquipmentImage
from gateways.equipment_image.repository import Repository as ImageRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    ''' Use case for creating a new equipment image. It checks if the image name is unique and saves the image to the database.'''
    def __init__(self):
        self.repo=ImageRepository()
        self.session_context = SessionContext()

    def handle(self, model:EquipmentImage) -> EquipmentImage:
        '''Handles the creation of a new equipment image. It checks for unique image name and saves the image to the database.'''
        with self.session_context as session:
            saved_model = self.repo.save(session , model)
            return saved_model