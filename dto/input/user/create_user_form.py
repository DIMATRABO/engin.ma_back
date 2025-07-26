''' form to create a user '''
from flask_restx import Namespace, fields
from models.user import User
from models.user_status import UserStatus
from models.user_role import UserRole
from dto.input.validator import required, optional, valid_string
from dto.input.validator import valid_password, valid_email_format, valid_datetime



class CreateUserForm:

    def __init__(self , json_user=None):
        if not json_user is None:

            self.username = required("username" , json_user)
            self.username = valid_string(self.username)

            self.password = required("password",json_user)
            self.password =valid_password(self.password)

            self.full_name = required("fullname" , json_user)
            self.full_name = valid_string(self.full_name)


            self.email = required("email",json_user)
            self.email = valid_email_format(self.email)

            self.birthdate = optional("birthdate" , json_user)
            self.birthdate = valid_datetime(self.birthdate,  "%Y-%m-%d")

            self.address = optional("address", json_user)
            self.address = valid_string(self.address)

            self.phone_number = optional("phoneNumber", json_user)
            self.phone_number = valid_string(self.phone_number)


    def to_domain(self, user_role: UserRole = UserRole.CLIENT):
        return User(
            id=None,
            username=self.username,
            password=self.password,
            full_name=self.full_name,
            email=self.email,
            birthdate=self.birthdate ,
            address=self.address,
            phone_number=self.phone_number,
            user_status=UserStatus(UserStatus.PENDING.value),
            role=[user_role.value]
            )
    @staticmethod
    def api_model(namespace: Namespace):
        """Returns the API model for the user creation form."""
        return namespace.model("SignUp", {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "fullname": fields.String(required=True),
        "email": fields.String(required=True),
        "birthdate": fields.String(required=False,description="Birth date in format YYYY-MM-DD"),
        "address": fields.String(required=False),
        "phoneNumber": fields.String(required=False),
    })