
from flask_restx import fields
from controllers.user.user_namespace import user_ns

signup_model = user_ns.model("SignUp", {
    "username": fields.String(required=True),
    "password": fields.String(required=True),
    "fullname": fields.String(required=True),
    "email": fields.String(required=True),
    "birthdate": fields.String(required=False,description="Birth date in format YYYY-MM-DD"),
    "address": fields.String(required=False),
    "phoneNumber": fields.String(required=False),
})
user_response_model = user_ns.model("UserResponse", {
    "id": fields.String(),
    "username": fields.String(),
    "email": fields.String(),
    "full_name": fields.String()
})