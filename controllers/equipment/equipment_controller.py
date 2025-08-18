
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from decorations.exception_handling import handle_exceptions

from dto.input.equipment.create_equipment import CreateEquipment
from dto.input.pagination.equipment_filter_form import EquipmentFilterForm
from dto.output.equipment.equipment_response_form import EquipmentResponseForm

from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from usecases.equipment.create import Create as CreateEquipmentUseCase
from usecases.equipment.get_all_paginated import GetAllEquipmentsPaginated as GetAllEquipmentsUseCase
from usecases.equipment.delete import Delete


equipment_creator = CreateEquipmentUseCase()
equipments_getter = GetAllEquipmentsUseCase()
equipment_deleter = Delete()

equipments_ns = Namespace("equipments", description="equipments operations")


@equipments_ns.route('')
class EquipmentController(Resource):
    ''' Equipments endpoint.'''
    
    @equipments_ns.expect(CreateEquipment.api_model(equipments_ns))
    @equipments_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        ''' Handle equipment creation.'''
        return EquipmentResponseForm(equipment_creator.handle(CreateEquipment(request.json).to_domain())).to_dict()
    

    ''' endpoint to delete an equipment '''
    @equipments_ns.route('/<string:equipment_id>')
    @equipments_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def delete(self, equipment_id):
        ''' Delete an equipment by ID. '''
        equipment_deleter.handle(equipment_id)
        return {"message": "Equipment deleted successfully"}

@equipments_ns.route('/filter')
class EquipmentFilterController(Resource):
    ''' Endpoint to filter and paginate equipments. '''

    @equipments_ns.expect(EquipmentFilterForm.api_model(equipments_ns))
    @equipments_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")  # or "CLIENT", "OWNER", depending on your rules
    def post(self):
        ''' Retrieve equipments based on filters and pagination. '''
        form = EquipmentFilterForm(request.json)
        equipments = equipments_getter.handle(form)
        return equipments.to_dict()
