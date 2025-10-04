''' Repository for booking management operations. '''
import uuid
from sqlalchemy import desc
from typing import List, Optional
from entities.booking_entity import BookingEntity
from models.booking import Booking
from gateways.log import Log
from exceptions.exception import NotFoundException
from exceptions.exception import InvalidRequestException
from dto.input.pagination.booking_filter_form import BookingFilterForm
from dto.output.booking.booking_paginated import BookingsPaginated
from dto.output.booking.booking_response_form import BookingResponseForm

logger = Log()

class Repository:
    '''Repository class for managing booking data operations.'''

    def __init__(self):
        '''Initialize the repository.'''
        logger.debug("BookingRepository initialized")

    def save(self, session, booking: Booking) -> Booking:
        '''Save a booking entity to the database.'''
        logger.debug(f"Saving booking: {booking}")
        booking_entity = BookingEntity()
        booking_entity.from_domain(model=booking)
        booking_entity.id = str(uuid.uuid4())
        session.add(booking_entity)
        logger.debug("Booking saved successfully")
        return booking_entity.to_domain()

    def update(self, session, booking: Booking) -> Optional[Booking]:
        '''Update an existing booking entity in the database.'''
        logger.debug(f"Updating booking with ID: {booking.id}")
        booking_entity = session.query(BookingEntity).filter_by(id=booking.id).first()
        if not booking_entity:
            logger.error(f"Booking with ID {booking.id} not found")
            return None
        booking_entity.from_domain(model=booking)  # overwrite with new values
        logger.debug("Booking updated successfully")
        return booking_entity.to_domain()

    def get_by_id(self, session, booking_id: str) -> Optional[Booking]:
        '''Retrieve a booking entity by its ID from the database.'''
        logger.debug(f"Retrieving booking with ID: {booking_id}")
        booking_entity = session.query(BookingEntity).filter_by(id=booking_id).first()
        if not booking_entity:
            logger.error(f"Booking with ID {booking_id} not found")
            return None
        return booking_entity.to_domain()

    def get_all(self, session) -> List[Booking]:
        '''Retrieve all booking entities from the database.'''
        logger.debug("Retrieving all bookings")
        bookings = session.query(BookingEntity).all()
        return [booking.to_domain() for booking in bookings]
    
    def get_by_client_id(self, session, client_id: str) -> List[Booking]:
        '''Retrieve all bookings for a specific client ID.'''
        logger.debug(f"Retrieving bookings for client ID: {client_id}")
        bookings = session.query(BookingEntity).filter_by(client_id=client_id).all()
        return [booking.to_domain() for booking in bookings]
    
    def get_by_booking_id(self, session, booking_id: str) -> List[Booking]:
        '''Retrieve all bookings for a specific booking ID.'''
        logger.debug(f"Retrieving bookings for booking ID: {booking_id}")
        bookings = session.query(BookingEntity).filter_by(booking_id=booking_id).all()
        return [booking.to_domain() for booking in bookings]
    
    def get_by_pilot_id(self, session, pilot_id: str) -> List[Booking]:
        '''Retrieve all bookings for a specific pilot ID.'''
        logger.debug(f"Retrieving bookings for pilot ID: {pilot_id}")
        bookings = session.query(BookingEntity).filter_by(pilot_id=pilot_id).all()
        return [booking.to_domain() for booking in bookings]
    
    def delete(self, session, booking_id: str) -> bool:
        '''Delete a booking entity by its ID from the database.'''
        logger.debug(f"Deleting booking with ID: {booking_id}")
        booking_entity = session.query(BookingEntity).filter_by(id=booking_id).first()
        if not booking_entity:
            logger.error(f"Booking with ID {booking_id} not found")
            raise NotFoundException(f"Booking with ID {booking_id} not found")
        session.delete(booking_entity)
        logger.debug("Booking deleted successfully")
        return True
    
    def get_all_paginated(self, session, input_form: BookingFilterForm) -> BookingsPaginated:
        '''Retrieve all bookings with pagination, filtering, and sorting.'''

        allowed_filter_keys = {
            'client_id': str,
            'equipment_id': str,
            'pilot_id': str,
            'start_date_range': list,
            'end_date_range': list,
            'number_of_days_range': list,
            'unit_price_range': list,
            'total_price_range': list,
            'status': str
        }

        allowed_sort_keys = [
            'start_date',
            'end_date',
            'number_of_days',
            'unit_price',
            'total_price',
            'created_at'
        ]

        query = session.query(BookingEntity)

        # Apply filters from filterData
        if input_form.client_id:
            query = query.filter(BookingEntity.client_id == input_form.client_id)
        if input_form.equipment_id:
            query = query.filter(BookingEntity.equipment_id == input_form.equipment_id)
        if input_form.pilot_id:
            query = query.filter(BookingEntity.pilot_id == input_form.pilot_id)
        if input_form.status:
            query = query.filter(BookingEntity.status == input_form.status)
        if input_form.start_date_range: 
            query = query.filter(
                BookingEntity.start_date >= input_form.start_date_range[0],
                BookingEntity.start_date <= input_form.start_date_range[1]
            )
        if input_form.end_date_range:
            query = query.filter(
                BookingEntity.end_date >= input_form.end_date_range[0],
                BookingEntity.end_date <= input_form.end_date_range[1]
            )
        if input_form.number_of_days_range:
            query = query.filter(
                BookingEntity.number_of_days >= input_form.number_of_days_range[0],
                BookingEntity.number_of_days <= input_form.number_of_days_range[1]
            )
        if input_form.unit_price_range:
            query = query.filter(
                BookingEntity.unit_price >= input_form.unit_price_range[0],
                BookingEntity.unit_price <= input_form.unit_price_range[1]
            )
        if input_form.total_price_range:
            query = query.filter(
                BookingEntity.total_price >= input_form.total_price_range[0],
                BookingEntity.total_price <= input_form.total_price_range[1]
            )
        if input_form.status:
            query = query.filter(BookingEntity.status == input_form.status)
  



        # Sorting
        if input_form.key and input_form.order:
            sort_key = input_form.key.lower()
            if sort_key in allowed_sort_keys:
                sort_column = getattr(BookingEntity, sort_key)
                query = query.order_by(desc(sort_column) if input_form.order.lower() == 'desc' else sort_column)
            else:
                raise InvalidRequestException(f"Invalid sort key: {sort_key}")
        else:
            query = query.order_by(desc(BookingEntity.created_at))

        # Pagination
        total_records = query.count()
        starting_index = (input_form.pageIndex - 1) * input_form.pageSize
        bookings = query.offset(starting_index).limit(input_form.pageSize).all()

        return BookingsPaginated(
            total=total_records,
            data=[BookingResponseForm(booking=booking.to_domain()) for booking in bookings]
        )
    

    

