''' Get all images associated with a specific equipment ID.'''
from models.equipment_image import EquipmentImage
from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment_image.repository import Repository as ImageRepository
class GetAllByEquipmentId:
    ''' Use case for retrieving all equipment images associated with a specific equipment ID.'''
    def __init__(self):
        self.repo = ImageRepository()
        self.session_context = SessionContext()

    def handle(self, equipment_id: str) -> list[EquipmentImage]:
        '''Handles the retrieval of all images associated with a specific equipment ID.'''
        with self.session_context as session:
            return self.repo.get_by_equipment_id(session, equipment_id)