''' Use Case: Get all equipments with pagination support'''
from dto.input.pagination.equipment_filter_form import EquipmentFilterForm
from dto.output.equipment.equipment_response_form import EquipmentResponseForm
from dto.output.equipment.equipments_paginated import EquipmentsPaginated
from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment.repository import Repository as EquipmentRepo

from usecases.equipment.load import Load as LoadEquipment



class GetAllEquipmentsPaginated:
    ''' Use case for retrieving all equipments with pagination support.'''
    def __init__(self):
        ''' Initializes the GetAllEquipmentsPaginated use case.'''
        self.load_equipment = LoadEquipment()
        self.equipment_repo=EquipmentRepo()
        self.session_context = SessionContext()

    def handle(self, input_form : EquipmentFilterForm) -> EquipmentsPaginated:
        ''' Handles the retrieval of all equipments with pagination.'''
        with self.session_context as session:
                equipments = self.equipment_repo.get_all_paginated(session,input_form)
                equipments_to_return = []
                for equipment in equipments.data:
                    equipment = self.load_equipment.handle(session,equipment)
                    equipments_to_return.append(EquipmentResponseForm(equipment))
                equipments.data = equipments_to_return
                return equipments
