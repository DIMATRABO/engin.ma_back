'''This module handles the deletion of a new equipment.'''
from models.equipment import Equipment
from gateways.equipment.repository import Repository as EquipmentRepository
from gateways.equipment_image.repository import Repository as ImageRepository
from gateways.dataBaseSession.session_context import SessionContext

class Delete:
    '''Use case for deleting a new equipment . '''
    def __init__(self):
        self.repo=EquipmentRepository()
        self.image_repo = ImageRepository()
        self.session_context = SessionContext()

    def handle(self, equipment_id:str) -> Equipment:
        '''Handles the creation of a new equipment.'''
        with self.session_context as session:
            for image in self.image_repo.get_by_equipment_id(session, equipment_id):
                self.image_repo.delete(session, image.id)
            self.repo.delete(session , equipment_id)
            return True
