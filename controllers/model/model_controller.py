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
from usecases.model.delete import Delete

# Create a namespace
model_ns = Namespace("models", description="Models management operations")
logger = Log()
create_model_handler = Create()
get_all_models_handler = GetAll()
delete_model_handler = Delete()

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

@model_ns.route('/<string:model_id>')
class ModelDeleteEndpoint(Resource):
    '''Endpoint to delete a model by ID.'''
    @model_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def delete(self, model_id):
        '''Delete a model by ID (admin only)'''
        delete_model_handler.handle(model_id)
        return {"message": "Model deleted successfully"}