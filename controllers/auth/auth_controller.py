''' Controller for user authentication.'''
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from gateways.log import Log
from decorations.exception_handling import handle_exceptions

from dto.input.user.login_form import LoginForm
from usecases.user.auth import Auth
from usecases.utils.auth import create_additional_claims_from_user


# Create a namespace
auth_ns = Namespace("auth", description="User authentication operations")
logger = Log()
auth = Auth()


@auth_ns.route('')
class AuthUser(Resource):
    """
    User authentication endpoint.
    This endpoint allows users to log in and obtain access and refresh tokens.
    """
    @handle_exceptions
    @auth_ns.doc(security=None)
    @auth_ns.expect(LoginForm.api_model(auth_ns))
    def post(self):
        ''' Authenticate a user and return access and refresh tokens.'''
        form = LoginForm(request.get_json())
        user = auth.handle(form)
        additional_claims =create_additional_claims_from_user(user)
        access_token = create_access_token(user.username, additional_claims=additional_claims)
        refresh_token = create_refresh_token(user.username, additional_claims=additional_claims)
        logger.log("Logged in as: " + user.username)
        return {"access_token": access_token, "refresh_token": refresh_token}

