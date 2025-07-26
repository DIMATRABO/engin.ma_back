'''This file is part of the Open Food Network project.'''
from flask_restx import Namespace, fields
from models.user import User
from models.user_status import UserStatus
from dto.input.validator import *


class ChangeStatusForm:
    '''Form for changing user status.'''
    def __init__(self , jsonUser):
        self.id = required("id" , jsonUser)
        self.id = valid_string(self.id)

        self.user_status = optional("status", jsonUser)
        self.user_status = valid_string(self.user_status)
        self.user_status = valid_status(self.user_status)



    def to_domain(self):
        '''Converts the form to a User domain model.'''
        return User(
            id=self.id,
            user_status=UserStatus(self.user_status)
        )

    @staticmethod
    def api_model(namespace: Namespace):
        '''Returns the API model for changing user status.'''
        return namespace.model("ChangeStatusForm", {
            "id": fields.String(required=True, description="User ID"),
            "status": fields.String(required=False, description="New status of the user (e.g., ACTIVE, INACTIVE)")
    })