''' Use Case: Get all equipments with pagination support'''
from dto.input.pagination.equipment_filter_form import EquipmentFilterForm
from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment.repository import Repository as EquipmentRepo


class GetAllEquipmentsPaginated:
    ''' Use case for retrieving all equipments with pagination support.'''
    def __init__(self):
        ''' Initializes the GetAllEquipmentsPaginated use case.'''
        self.equipment_repo=EquipmentRepo()
        self.session_context = SessionContext()

    def handle(self, input_form : EquipmentFilterForm):
        ''' Handles the retrieval of all equipments with pagination.'''
        with self.session_context as session:
                return self.equipment_repo.get_all_paginated(session,input_form)    