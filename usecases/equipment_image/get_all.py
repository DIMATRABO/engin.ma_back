''' Get all images '''
from models.equipment_image import EquipmentImage
from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment_image.repository import Repository as ImageRepository


class GetAll:
    ''' Use case for retrieving all equipment images. It fetches all images from the database.'''
    def __init__(self):
        self.repo= ImageRepository()
        self.session_context = SessionContext()

    def handle(self)->list[EquipmentImage]:
        '''Handles the retrieval of all equipment images. It fetches all images from the database.'''
        with self.session_context as session:
            return  self.repo.get_all(session)
          
            


