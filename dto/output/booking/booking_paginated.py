'''Data Transfer Object for paginated booking responses.'''
from dataclasses import dataclass, field, asdict
from typing import List
from dto.output.booking.booking_response_form import BookingResponseForm



@dataclass
class BookingsPaginated:
    ''' Data Transfer Object for paginated booking responses.'''
    total: int
    data: List[BookingResponseForm] = field(default_factory=list)
    

    def to_dict(self):
        '''Convert the BookingsPaginated object to a dictionary.'''
        self.data = [booking.to_dict() for booking in self.data]
        return asdict(self)