''' Repository for booking management operations. '''
import uuid
from typing import List, Optional
from entities.booking_entity import BookingEntity
from models.booking import Booking
from gateways.log import Log

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
    
    def get_by_equipment_id(self, session, equipment_id: str) -> List[Booking]:
        '''Retrieve all bookings for a specific equipment ID.'''
        logger.debug(f"Retrieving bookings for equipment ID: {equipment_id}")
        bookings = session.query(BookingEntity).filter_by(equipment_id=equipment_id).all()
        return [booking.to_domain() for booking in bookings]
    
    def get_by_pilot_id(self, session, pilot_id: str) -> List[Booking]:
        '''Retrieve all bookings for a specific pilot ID.'''
        logger.debug(f"Retrieving bookings for pilot ID: {pilot_id}")
        bookings = session.query(BookingEntity).filter_by(pilot_id=pilot_id).all()
        return [booking.to_domain() for booking in bookings]
    

    

