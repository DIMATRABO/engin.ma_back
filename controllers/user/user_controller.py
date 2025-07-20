''' UserController.py'''
from flask import request 
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource

from gateways.log import Log
from decorations.exception_handling import handle_exceptions

from dto.forms.user.create.create_user_api_model import signup_model
from dto.forms.user.delete.delete_user_api_model import delete_model
from dto.forms.user.create.create_user_form import CreateUserForm
from dto.output.user.user_response_form import UserResponseForm

from flask_restx import Namespace
from usecases.user.create import Create
from usecases.user.delete import Delete


logger = Log()
delete_handler = Delete()
creating_handler = Create()

user_ns = Namespace("user", description="User management operations")


@user_ns.route('/signup')
class SignUp(Resource):
    @user_ns.expect(signup_model)
    @handle_exceptions
    def post(self):
        """Create a new user"""
        user_json = request.get_json()
        form = CreateUserForm(user_json)
        user = form.to_domain()
        logger.log(f'Creating User {user.username}')
        response = creating_handler.handle(user)
        return UserResponseForm(response).to_dict(), 201


@user_ns.route('/delete')
class DeleteUser(Resource):
    @user_ns.expect(delete_model)
    @jwt_required()
    @handle_exceptions
    def delete(self):
        """Delete an existing user (admin only)"""
        user_id = request.get_json().get("id")
        logger.log(f'Deleting User {user_id}')
        return delete_handler.handle(user_id), 200