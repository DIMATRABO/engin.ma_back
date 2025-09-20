''' Reviewcontroller.py'''
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from gateways.log import Log
from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from dto.input.review.create_review_form import CreateReviewForm

from usecases.review.create import Create
from usecases.review.get_all import GetAll
from usecases.review.get_all_by_client_id import GetAll as GetAllByClientId
from usecases.review.get_all_by_equipment_id import GetAll as GetAllByEquipmentId
from usecases.review.get_all_by_pilot_id import GetAll as GetAllByPilotId

# Create a namespace
review_ns = Namespace("reviews", description="Reviews management operations")
logger = Log()
create_review_handler = Create()
get_all_reviews_handler = GetAll()
get_reviews_by_client_id_handler = GetAllByClientId()
get_reviews_by_equipment_id_handler = GetAllByEquipmentId()
get_reviews_by_pilot_id_handler = GetAllByPilotId()

@review_ns.route('')
class CreateEndpoint(Resource):
    '''Endpoint to create a new review.'''
    @review_ns.doc(security="Bearer Auth")
    @review_ns.expect(CreateReviewForm.api_model(review_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        '''Create a new review (admin only)'''
        form = CreateReviewForm(request.get_json())
        return create_review_handler.handle(form.to_domain()).to_dict()
    
@review_ns.route('/all')
class GetAllEndpoint(Resource):
    '''Endpoint to get all reviews.'''
    @review_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self):
        '''Get all reviews (admin only)'''
        reviews = get_all_reviews_handler.handle()
        return [review.to_dict() for review in reviews]
    
@review_ns.route('/client/<string:client_id>')
class GetByClientIdEndpoint(Resource):
    '''Endpoint to get reviews by client ID.'''
    @review_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self, client_id: str):
        '''Get reviews by client ID (admin only)'''
        reviews = get_reviews_by_client_id_handler.handle(client_id)
        return [review.to_dict() for review in reviews]
    
@review_ns.route('/equipment/<string:equipment_id>')
class GetByEquipmentIdEndpoint(Resource):
    '''Endpoint to get reviews by equipment ID.'''
    @review_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN,PILOT,CLIENT")
    def get(self, equipment_id: str):
        '''Get reviews by equipment ID (admin, pilot, client)'''
        reviews = get_reviews_by_equipment_id_handler.handle(equipment_id)
        return [review.to_dict() for review in reviews]

@review_ns.route('/pilot/<string:pilot_id>')
class GetByPilotIdEndpoint(Resource):
    '''Endpoint to get reviews by pilot ID.'''
    @review_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN,PILOT,CLIENT")
    def get(self, pilot_id: str):
        '''Get reviews by pilot ID (admin, pilot, client)'''
        reviews = get_reviews_by_pilot_id_handler.handle(pilot_id)
        return [review.to_dict() for review in reviews]