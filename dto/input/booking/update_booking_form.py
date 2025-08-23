''' Input DTO for updating a booking. '''
from flask_restx import fields, Namespace
from dto.input.validator import optional, valid_string, valid_datetime, required
from models.booking import Booking
from models.user import User
from models.equipment import Equipment

class UpdateBookingForm:
    ''' Input form for updating a booking. '''

    def __init__(self, json_input):
        self.id = required("id", json_input)
        self.id = valid_string(self.id)

        self.client_id = optional("client_id", json_input)
        self.client_id = valid_string(self.client_id) if self.client_id else None

        self.equipment_id = optional("equipment_id", json_input)
        self.equipment_id = valid_string(self.equipment_id) if self.equipment_id else None

        self.pilot_id = optional("pilot_id", json_input)
        self.pilot_id = valid_string(self.pilot_id) if self.pilot_id else None

        self.start_date = optional("start_date", json_input)
        self.start_date = valid_datetime(self.start_date, format="%Y-%m-%d") if self.start_date else None

        self.end_date = optional("end_date", json_input)
        self.end_date = valid_datetime(self.end_date,format="%Y-%m-%d"  ) if self.end_date else None

        self.status = optional("status", json_input)  # must be validated against BookingStatus Enum
        self.status = valid_string(self.status).upper() if self.status else None

    @staticmethod
    def api_model(namespace: Namespace):
        ''' Returns the API model for booking update. '''
        return namespace.model("UpdateBookingForm", {
            "id": fields.String(required=True, description="ID of the booking to update"),
            "client_id": fields.String(required=False, description="ID of the client"),
            "equipment_id": fields.String(required=False, description="ID of the equipment"),
            "pilot_id": fields.String(required=False, description="ID of the pilot (if any)"),
            "start_date": fields.String(required=False, description="Booking start date (YYYY-MM-DD)"),
            "end_date": fields.String(required=False, description="Booking end date (YYYY-MM-DD)"),
            "status": fields.String(required=False, description="Booking status (PENDING, CONFIRMED, CANCELED, COMPLETED)")
        })
    
    def to_domain(self):
        """Converts the form data to a Booking domain model."""
        return Booking(
            id=self.id,
            client=User(id=self.client_id) if self.client_id else None,
            equipment=Equipment(id=self.equipment_id) if self.equipment_id else None,
            pilot=User(id=self.pilot_id) if self.pilot_id else None,
            start_date=self.start_date,
            end_date=self.end_date,
            status=self.status
        )

