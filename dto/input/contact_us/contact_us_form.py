from flask_restx import Namespace, fields
from dto.input.validator import required, valid_string, valid_email_format, valid_phone_format

class ContactUsForm:
    """
    Represents the form data for a contact us submission.
    """
    def __init__(self, json_data=None):
        """ Initializes the ContactUsForm with data from a JSON object."""
        self.name = required("name", json_data)
        self.name = valid_string(self.name)

        self.phone = required("phone", json_data)
        self.phone = valid_phone_format(self.phone)

        self.email = required("email", json_data)
        self.email = valid_email_format(self.email)

        self.message = required("message", json_data)
        self.message = valid_string(self.message)

    def __repr__(self):
        return f"ContactUsForm(name={self.name}, email={self.email}, message={self.message})"
    
    def api_model(namespace: Namespace):
        """
        Returns the API model for the ContactUsForm.
        """
        return namespace.model("ContactUsForm", {
            "name": fields.String(required=True, description="Name of the person"),
            "phone": fields.String(required=True, description="Phone number of the person"),
            "email": fields.String(required=True, description="Email address of the person"),
            "message": fields.String(required=True, description="Message from the person")
        })