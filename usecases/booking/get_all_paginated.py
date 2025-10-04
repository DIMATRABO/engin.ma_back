''' Use Case: Get all bookings with pagination support'''
from dto.input.pagination.booking_filter_form import BookingFilterForm
from dto.output.booking.booking_response_form import BookingResponseForm
from dto.output.booking.booking_paginated import BookingsPaginated
from gateways.dataBaseSession.session_context import SessionContext
from gateways.booking.repository import Repository as BookingRepo
from usecases.booking.load import Load as LoadBooking

class GetAllBookingsPaginated:
    ''' Use case for retrieving all bookings with pagination support.'''
    def __init__(self):
        ''' Initializes the GetAllBookingsPaginated use case.'''
        self.load_booking = LoadBooking()
        self.booking_repo=BookingRepo()
        self.session_context = SessionContext()

    def handle(self, input_form : BookingFilterForm) -> BookingsPaginated:
        ''' Handles the retrieval of all bookings with pagination.'''
        with self.session_context as session:
                bookings = self.booking_repo.get_all_paginated(session,input_form)
                bookings_to_return = []
                for booking in bookings.data:
                    booking = self.load_booking.handle(session,booking)
                    bookings_to_return.append(BookingResponseForm(booking))
                bookings.data = bookings_to_return
                return bookings
