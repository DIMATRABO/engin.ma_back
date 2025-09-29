
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from decorations.exception_handling import handle_exceptions

from dto.input.equipment.create_equipment import CreateEquipment
from dto.input.pagination.equipment_filter_form import EquipmentFilterForm
from dto.output.equipment.equipment_response_form import EquipmentResponseForm
from dto.input.equipment.update_equipment import UpdateEquipment

from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from usecases.equipment.create import Create as CreateEquipmentUseCase
from usecases.equipment.get_by_id import GetById as GetEquipmentByIdUseCase
from usecases.equipment.get_all_paginated import GetAllEquipmentsPaginated as GetAllEquipmentsUseCase
from usecases.equipment.delete import Delete
from usecases.equipment.update import Update as UpdateEquipmentUseCase



equipment_creator = CreateEquipmentUseCase()
equiment_getter_by_id = GetEquipmentByIdUseCase()
equipments_getter = GetAllEquipmentsUseCase()
equipment_deleter = Delete()
equipment_updater = UpdateEquipmentUseCase()

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
    
@equipments_ns.route("/<string:equipment_id>")
class GetEquipmentByIdController(Resource):
    ''' Endpoint to Get an equipment by ID. '''

    @equipments_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN,CLIENT,OWNER")
    def get_by_id(self, equipment_id):
        ''' get an equipment by ID. '''
        return equiment_getter_by_id.handle(equipment_id).to_dict()
    
@equipments_ns.route("/<string:equipment_id>")
class EquipmentDeleteController(Resource):
    ''' Endpoint to delete an equipment. '''

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


@equipments_ns.route('/update')
class EquipmentUpdateController(Resource):
    ''' Endpoint to update an equipment '''

    @equipments_ns.expect(UpdateEquipment.api_model(equipments_ns))
    @equipments_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def put(self):
        ''' Update equipment details '''
        form = UpdateEquipment(request.json)
        updated_equipment = equipment_updater.handle(form.to_domain())
        return EquipmentResponseForm(updated_equipment).to_dict()
    