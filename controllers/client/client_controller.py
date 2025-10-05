''' Clientcontroller.py'''
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from usecases.client.get_all import GetAll

# Create a namespace
client_ns = Namespace("clients", description="clients management operations")

get_all_clients_handler = GetAll()

@client_ns.route('')
class ClientController(Resource):
    '''Endpoint to create a new client.'''
    @client_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    @handle_exceptions
    def get(self):
        '''Get all clients'''
        clients = get_all_clients_handler.handle()
        return [client.to_dict() for client in clients]
    