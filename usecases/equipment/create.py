'''This module handles the creation of a new equipment.'''
from models.equipment import Equipment
from gateways.equipment.repository import Repository as EquipmentRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    '''Use case for creating a new equipment . '''
    def __init__(self):
        self.repo=EquipmentRepository()
        self.session_context = SessionContext()

    def handle(self, equipment:Equipment) -> Equipment:
        '''Handles the creation of a new equipment.'''
        with self.session_context as session:
            saved_equipment = self.repo.save(session , equipment)
            return saved_equipment
