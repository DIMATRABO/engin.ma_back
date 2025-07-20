''' form to create a user '''
from models.user import User
from models.user_status import UserStatus
from models.user_role import UserRole
from dto.forms.validator import *


class CreateUserForm:

    def __init__(self , jsonUser):

        self.username = required("username" , jsonUser)
        self.username = valid_string(self.username)

        self.password = required("password",jsonUser)
        self.password =valid_password(self.password)

        self.full_name = required("fullname" , jsonUser)
        self.full_name = valid_string(self.full_name)


        self.email = required("email",jsonUser)
        self.email = valid_email_format(self.email)

        self.birthdate = optional("birthdate" , jsonUser)
        self.birthdate = valid_datetime(self.birthdate,  "%Y-%m-%d")

        self.address = optional("address", jsonUser)
        self.address = valid_string(self.address)

        self.phone_number = optional("phoneNumber", jsonUser)
        self.phone_number = valid_string(self.phone_number)


    def to_domain(self):
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
            role=[UserRole(UserRole.CLIENT.value)],
                            )