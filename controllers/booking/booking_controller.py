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
from usecases.booking.get_by_client_id import GetByClientId


# Create a namespace
booking_ns = Namespace("bookings", description="Bookings management operations")
logger = Log()
create_booking_handler = Create()
update_booking_handler = Update()
get_all_bookings_handler = GetAll()
get_by_equipment_id_handler = GetByEquipmentId()
get_by_pilot_id_handler = GetByPilotId()
get_by_client_id_handler = GetByClientId()


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
    @booking_ns.doc(security="Bearer Auth",params={'equipment_id': 'The ID of the equipment'})
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self, equipment_id):
        '''Get bookings by equipment ID'''
        bookings = get_by_equipment_id_handler.handle(equipment_id)
        return [booking.to_dict() for booking in bookings]
    
@booking_ns.route('/pilot/<string:pilot_id>')
class BookingByPilotEndpoint(Resource):
    '''Endpoint to get bookings by pilot ID.'''
    @booking_ns.doc(security="Bearer Auth", params={'pilot_id': 'The ID of the pilot'})
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self, pilot_id):
        '''Get bookings by pilot ID'''
        bookings = get_by_pilot_id_handler.handle(pilot_id)
        results = []

        for i, booking in enumerate(bookings):
            try:
                results.append(booking.to_dict())
            except TypeError as e:
                logger.error(f"❌ Serialization error at booking index {i}: {booking}")
                # Check if dict has datetime
                try:
                    data = booking.to_dict()
                    for k, v in data.items():
                        if hasattr(v, "isoformat"):  # naive datetime check
                            logger.error(f"⚠️ Field '{k}' contains datetime: {v}")
                except Exception:
                    pass
                raise  # re-raise so Flask still fails

        logger.log(f"Retrieved {results}")
        return results

@booking_ns.route('/client/<string:client_id>')
class BookingByClientEndpoint(Resource):
    '''Endpoint to get bookings by client ID.'''
    @booking_ns.doc(security="Bearer Auth", params={'client_id': 'The ID of the client'})
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self, client_id):
        '''Get bookings by client ID'''
        bookings = get_by_client_id_handler.handle(client_id)
        return [booking.to_dict() for booking in bookings]