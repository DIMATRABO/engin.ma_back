'''LoginForm class for user login validation.'''
from flask_restx import Namespace, fields
from dto.input.validator import required, valid_string, valid_password


class LoginForm:
    """LoginForm class for user login validation."""
    username_or_email: str
    password:str

    def __init__(self , json_credentials):

        self.username_or_email = required("username_or_email" , json_credentials)
        self.username_or_email = valid_string(self.username_or_email)
        
        self.password = required("password",json_credentials)
        self.password = valid_password(self.password)

    @staticmethod
    def api_model(namespace: Namespace):
        """Returns the API model."""
        return namespace.model("SignUp", {
        "username_or_email": fields.String(required=True, description="Username or email of the user"),
        "password": fields.String(required=True, description="Password of the user")
    })

