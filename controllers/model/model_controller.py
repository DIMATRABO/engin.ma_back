''' UserController.py'''
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from gateways.log import Log
from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from dto.input.model.create_model_form import CreateModelForm

from usecases.model.create import Create
from usecases.model.get_all import GetAll

# Create a namespace
model_ns = Namespace("models", description="Cities management operations")
logger = Log()
create_model_handler = Create()
get_all_models_handler = GetAll()

@model_ns.route('')
class CreateEndpoint(Resource):
    '''Endpoint to create a new model.'''
    @model_ns.doc(security="Bearer Auth")
    @model_ns.expect(CreateModelForm.api_model(model_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        '''Create a new model (admin only)'''
        form = CreateModelForm(request.get_json())
        return create_model_handler.handle(form.to_domain()).to_dict()
    
    @handle_exceptions
    def get(self):
        '''Get all models'''
        models = get_all_models_handler.handle()
        return [model.to_dict() for model in models]
    