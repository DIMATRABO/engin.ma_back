''' Use Case: Get all equipments with pagination support'''
from dto.input.pagination.equipment_filter_form import EquipmentFilterForm
from dto.output.equipment.equipment_response_form import EquipmentResponseForm
from dto.output.equipment.equipments_paginated import EquipmentsPaginated
from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment.repository import Repository as EquipmentRepo

from usecases.city.get_by_id import GetById as GetCityById
from usecases.brand.get_by_id import GetById as GetBrandById
from usecases.user.details import Details as GetUserById
from usecases.model.get_by_id import GetById as GetModelById
from usecases.equipment_image.get_all_by_equipment_id import GetAllByEquipmentId



city_getter = GetCityById()
brand_getter = GetBrandById()
model_getter = GetModelById()
user_getter = GetUserById()
images_getter = GetAllByEquipmentId()




class GetAllEquipmentsPaginated:
    ''' Use case for retrieving all equipments with pagination support.'''
    def __init__(self):
        ''' Initializes the GetAllEquipmentsPaginated use case.'''
        self.equipment_repo=EquipmentRepo()
        self.session_context = SessionContext()

    def handle(self, input_form : EquipmentFilterForm) -> EquipmentsPaginated:
        ''' Handles the retrieval of all equipments with pagination.'''
        with self.session_context as session:
                equipments = self.equipment_repo.get_all_paginated(session,input_form)
                equipments_to_return = []
                for equipment in equipments.data:
                    
                    equipment.city = city_getter.handle(equipment.city.id) if equipment.city else None
                    equipment.brand = brand_getter.handle(equipment.brand.id) if equipment.brand else None
                    equipment.model = model_getter.handle(equipment.model.id) if equipment.model else None
                    equipment.owner = user_getter.handle(equipment.owner.id) if equipment.owner else None
                    equipment.pilot = user_getter.handle(equipment.pilot.id) if equipment.pilot else None
                    equipment.images = images_getter.handle(equipment.id) if equipment.images else []
                    equipments_to_return.append(EquipmentResponseForm(equipment))
                equipments.data = equipments_to_return
                return equipments
