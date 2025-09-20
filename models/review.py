''' Review model for representing a review with an ID and name.'''
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Review:
    '''Review model representing a review with an ID and name.'''
    id: str = None
    client_id: str = None
    equipment_id: str = None
    pilot_id: str = None
    rating: int = None
    comment: str = None
    created_at: datetime = None

    @classmethod
    def from_dict(cls, self, d):
        '''Create a Review instance from a dictionary.'''
        return self(**d)

    def to_dict(self):
        '''Convert the review instance to a dictionary.'''
        self.created_at = self.created_at.isoformat() if self.created_at else None
        return asdict(self)
