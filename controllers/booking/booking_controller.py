''' booking_controller.py'''
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from gateways.log import Log
from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from dto.input.booking.create_booking_form import CreateBookingForm
from dto.input.booking.update_booking_form import UpdateBookingForm

from usecases.booking.create import Create
from usecases.booking.update import Update
from usecases.booking.get_all import GetAll
from usecases.booking.get_by_equipment_id import GetByEquipmentId
from usecases.booking.get_by_pilot_id import GetByPilotId


# Create a namespace
booking_ns = Namespace("bookings", description="Bookings management operations")
logger = Log()
create_booking_handler = Create()
update_booking_handler = Update()
get_all_bookings_handler = GetAll()
get_by_equipment_id_handler = GetByEquipmentId()
get_by_pilot_id_handler = GetByPilotId()


@booking_ns.route('')
class BookingEndpoint(Resource):
    '''Endpoint to create a new booking.'''
    
    @booking_ns.doc(security="Bearer Auth")
    @booking_ns.expect(CreateBookingForm.api_model(booking_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        '''Create a new booking (admin only)'''
        form = CreateBookingForm(request.get_json())
        return create_booking_handler.handle(form.to_domain()).to_dict()
    
    @booking_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self):
        '''Get all bookings'''
        bookings = get_all_bookings_handler.handle()
        return [booking.to_dict() for booking in bookings]
    
    '''Endpoint to update a booking.'''
    @booking_ns.doc(security="Bearer Auth")
    @booking_ns.expect(UpdateBookingForm.api_model(booking_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def put(self):
        '''Update a booking (admin only)'''
        form = UpdateBookingForm(request.get_json())
        return update_booking_handler.handle(form.to_domain()).to_dict()
    

@booking_ns.route('/equipment/<string:equipment_id>')
class BookingByEquipmentEndpoint(Resource):
    '''Endpoint to get bookings by equipment ID.'''
    @handle_exceptions
    @booking_ns.doc(security="Bearer Auth")
    @booking_ns.expect(booking_ns.parser().add_argument('equipment_id', type=str, required=True, help='Equipment ID'))
    @jwt_required()
    @check_permission("ADMIN")
    def get(self, equipment_id):
        '''Get bookings by equipment ID'''
        bookings = get_by_equipment_id_handler.handle(equipment_id)
        return [booking.to_dict() for booking in bookings]
    
@booking_ns.route('/pilot/<string:pilot_id>')
class BookingByPilotEndpoint(Resource):
    '''Endpoint to get bookings by pilot ID.'''
    @booking_ns.doc(security="Bearer Auth")
    @booking_ns.expect(booking_ns.parser().add_argument('pilot_id', type=str, required=True, help='Pilot ID'))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self, pilot_id):
        '''Get bookings by pilot ID'''
        bookings = get_by_pilot_id_handler.handle(pilot_id)
        return [booking.to_dict() for booking in bookings]