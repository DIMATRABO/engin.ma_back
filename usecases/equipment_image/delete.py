''' Delete an equipment image. '''
from models.equipment_image import EquipmentImage
from gateways.equipment_image.repository import Repository as ImageRepository
from gateways.dataBaseSession.session_context import SessionContext

class Delete:
    ''' Use case for deleting an equipment image.'''
    def __init__(self):
        self.repo=ImageRepository()
        self.session_context = SessionContext()

    def handle(self, image: EquipmentImage) -> bool:
        '''Handles the deletion of an equipment image. It checks if the image belongs to the specified equipment and deletes it.'''
        with self.session_context as session:
            self.repo.delete(session, image_id=image.id)
            return True