''' Field of activity controller'''
from flask_restx import Namespace, Resource

from models.fields_of_activity import FieldsOfActivity
from gateways.log import Log
from decorations.exception_handling import handle_exceptions




foa_ns = Namespace("foa", description="Fields of Activity operations")
logger = Log()


@foa_ns.route('')
class FoaController(Resource):
    '''Endpoint to get all fields of activity'''    
    @handle_exceptions
    def get(self):
        '''Get all fields of activity'''
        return [field.value for field in FieldsOfActivity], 200
    