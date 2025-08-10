
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from decorations.exception_handling import handle_exceptions

from dto.input.equipment.create_equipment import CreateEquipment

from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

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
        return {"message":"not implemented yet"}