from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment.repository import Repository as EquipmentRepository

class Update:
    ''' UseCase to update an equipment '''
    def __init__(self):
        self.repo = EquipmentRepository()

    def handle(self, equipment):
        ''' Handles the update of an equipment. '''
        with SessionContext() as session:
            updated = self.repo.update(session, equipment)
            return updated
