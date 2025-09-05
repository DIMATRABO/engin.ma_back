''' Ownercontroller.py'''
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from usecases.owner.get_all import GetAll

# Create a namespace
owner_ns = Namespace("owners", description="owners management operations")

get_all_owners_handler = GetAll()

@owner_ns.route('')
class OwnerController(Resource):
    '''Endpoint to create a new owner.'''
    @owner_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    @handle_exceptions
    def get(self):
        '''Get all owners'''
        owners = get_all_owners_handler.handle()
        return [owner.to_dict() for owner in owners]
    