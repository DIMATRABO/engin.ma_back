''' UserController.py'''
from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import  jwt_required, create_access_token, create_refresh_token


from gateways.log import Log
from decorations.exception_handling import handle_exceptions

from dto.input.user.create_user_form import CreateUserForm
from dto.output.user.user_response_form import UserResponseForm
from dto.input.user.login_form import LoginForm

from usecases.user.auth import Auth
from usecases.user.create import Create
from usecases.user.delete import Delete
from usecases.utils.auth import create_additional_claims_from_user


# Create a namespace
user_ns = Namespace("user", description="User management operations")
logger = Log()
auth = Auth()
delete_handler = Delete()
creating_handler = Create()


@user_ns.route('/auth')
class AuthUser(Resource):
    """
    User authentication endpoint.
    This endpoint allows users to log in and obtain access and refresh tokens.
    """
    @handle_exceptions
    @user_ns.doc(security=None)
    @user_ns.expect(LoginForm.api_model(user_ns))
    def auth_user(self):
        ''' Authenticate a user and return access and refresh tokens.'''
        form = LoginForm(request.get_json())
        user = auth.handle(form)
        additional_claims =create_additional_claims_from_user(user)
        access_token = create_access_token(user.username, additional_claims=additional_claims)
        refresh_token = create_refresh_token(user.username, additional_claims=additional_claims)
        logger.log("Logged in as: " + user.username)
        return {"access_token": access_token, "refresh_token": refresh_token}



@user_ns.route('/signup')
class SignUp(Resource):
    ''' User signup endpoint.'''
    @user_ns.expect(CreateUserForm.api_model(user_ns))
    @handle_exceptions
    def post(self):
        """Create a new user"""
        user_json = request.get_json()
        form = CreateUserForm(user_json)
        user = form.to_domain()
        logger.log(f'Creating User {user.username}')
        response = creating_handler.handle(user)
        return UserResponseForm(response).to_dict(), 201


delete_model = user_ns.model("DeleteUser", {
    "id": fields.String(required=True)
})

@user_ns.route('/delete')
class DeleteUser(Resource):
    ''' User deletion endpoint.'''
    @user_ns.expect(delete_model)
    @user_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    def delete(self):
        """Delete an existing user (admin only)"""
        user_id = request.get_json().get("id")
        logger.log(f'Deleting User {user_id}')
        return delete_handler.handle(user_id), 200
