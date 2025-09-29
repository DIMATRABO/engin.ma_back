''' Use Case: Get an equipment by id'''

from dto.output.equipment.equipment_response_form import EquipmentResponseForm
from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment.repository import Repository as EquipmentRepo
from usecases.equipment.load import Load as LoadEquipment

class GetById:
    ''' Use case for retrieving one equipment by id.'''
    def __init__(self):
        ''' Initializes the getById usecase.'''
        self.load_equipment = LoadEquipment()
        self.equipment_repo=EquipmentRepo()
        self.session_context = SessionContext()

    def handle(self, id_ : str) -> EquipmentResponseForm:
        ''' Handles the retrieval of one equipment by id.'''
        with self.session_context as session:
                equipment = self.equipment_repo.get_equipment_by_id(session,id_)
                equipment = self.load_equipment.handle(session,equipment)
                return EquipmentResponseForm(equipment)