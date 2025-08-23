from sqlalchemy import Column, String, Date, TIMESTAMP, ForeignKey, func
from entities.declarative_base_factory import Base
from models.booking import Booking
from models.user import User
from models.equipment import Equipment
from models.booking_status import BookingStatus

class BookingEntity(Base):
    ''' BookingEntity class representing a booking in the database. '''
    __tablename__ = "bookings"

    id = Column("id", String, primary_key=True)
    client_id = Column("client_id", String, ForeignKey("users.id"))
    equipment_id = Column("equipment_id", String, ForeignKey("equipment.id"))
    pilot_id = Column("pilot_id", String, ForeignKey("users.id"))
    start_date = Column("start_date", Date)
    end_date = Column("end_date", Date)
    status = Column("status", String(50))
    created_at = Column("created_at", TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return (f"<BookingEntity(id={self.id}, client_id='{self.client_id}', "
                f"equipment_id='{self.equipment_id}', pilot_id='{self.pilot_id}', "
                f"status='{self.status}')>")

    def from_domain(self, model: Booking):
        ''' Populate the BookingEntity instance from a domain model. '''
        self.id = model.id
        self.client_id = model.client.id if model.client else None
        self.equipment_id = model.equipment.id if model.equipment else None
        self.pilot_id = model.pilot.id if model.pilot else None
        self.start_date = model.start_date
        self.end_date = model.end_date
        self.status = model.status.value if model.status else None
        self.created_at = model.created_at

    def to_domain(self) -> Booking:
        ''' Convert the BookingEntity instance to a domain model. '''
        return Booking(
            id=self.id,
            client=User(id=self.client_id) if self.client_id else None,
            equipment=Equipment(id=self.equipment_id) if self.equipment_id else None,
            pilot=User(id=self.pilot_id) if self.pilot_id else None,
            start_date=self.start_date,
            end_date=self.end_date,
            status=BookingStatus(self.status) if self.status else None,
            created_at=self.created_at
        )
