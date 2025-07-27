''' UserController.py'''
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from gateways.log import Log
from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from dto.input.city.create_city_form import CreateCityForm

from usecases.city.create import Create
from usecases.city.get_all import GetAll

# Create a namespace
city_ns = Namespace("cities", description="Cities management operations")
logger = Log()
create_city_handler = Create()
get_all_cities_handler = GetAll()

@city_ns.route('')
class CreateEndpoint(Resource):
    '''Endpoint to create a new city.'''
    @city_ns.doc(security="Bearer Auth")
    @city_ns.expect(CreateCityForm.api_model(city_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        '''Create a new city (admin only)'''
        form = CreateCityForm(request.get_json())
        return create_city_handler.handle(form.to_domain()).to_dict()
    
    @handle_exceptions
    def get(self):
        '''Get all cities'''
        cities = get_all_cities_handler.handle()
        return [city.to_dict() for city in cities]
    