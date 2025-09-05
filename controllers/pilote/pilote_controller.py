''' PiloteController.py'''
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from usecases.pilote.get_all import GetAll

# Create a namespace
pilote_ns = Namespace("pilotes", description="pilotes management operations")
get_all_pilotes_handler = GetAll()

@pilote_ns.route('')
class PiloteController(Resource):
    '''Endpoint to create a new pilote.'''
    @pilote_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    @handle_exceptions
    def get(self):
        '''Get all pilotes'''
        pilotes = get_all_pilotes_handler.handle()
        return [pilote.to_dict() for pilote in pilotes]
    