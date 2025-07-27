''' UserController.py'''
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from gateways.log import Log
from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from dto.input.brand.create_brand_form import CreateBrandForm

from usecases.brand.create import Create
from usecases.brand.get_all import GetAll

# Create a namespace
brand_ns = Namespace("cities", description="Cities management operations")
logger = Log()
create_brand_handler = Create()
get_all_cities_handler = GetAll()

@brand_ns.route('/')
class CreateEndpoint(Resource):
    '''Endpoint to create a new brand.'''
    @brand_ns.doc(security="Bearer Auth")
    @brand_ns.expect(CreateBrandForm.api_model(brand_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        '''Create a new brand (admin only)'''
        form = CreateBrandForm(request.get_json())
        return create_brand_handler.handle(form.to_domain()).to_dict()
    
    @handle_exceptions
    def get(self):
        '''Get all cities'''
        cities = get_all_cities_handler.handle()
        return [brand.to_dict() for brand in cities]
    