''' UserController.py'''
from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import  jwt_required, create_access_token, create_refresh_token


from gateways.log import Log
from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission
from models.user_role import UserRole

from dto.input.user.create_user_form import CreateUserForm
from dto.output.user.user_response_form import UserResponseForm
from dto.input.user.login_form import LoginForm
from dto.input.pagination.input_form import InputForm
from dto.input.user.change_status_form import ChangeStatusForm

from usecases.user.auth import Auth
from usecases.user.create import Create
from usecases.user.get_all_paginated import GetAllUsersPaginated
from usecases.user.delete import Delete
from usecases.user.change_status import ChangeStatus
from usecases.utils.auth import create_additional_claims_from_user

# Create a namespace
user_ns = Namespace("user", description="User management operations")
logger = Log()
auth = Auth()
delete_handler = Delete()
creating_handler = Create()
get_all_users_handler = GetAllUsersPaginated()
change_status_handler = ChangeStatus()


@user_ns.route('/auth')
class AuthUser(Resource):
    """
    User authentication endpoint.
    This endpoint allows users to log in and obtain access and refresh tokens.
    """
    @handle_exceptions
    @user_ns.doc(security=None)
    @user_ns.expect(LoginForm.api_model(user_ns))
    def post(self):
        ''' Authenticate a user and return access and refresh tokens.'''
        form = LoginForm(request.get_json())
        user = auth.handle(form)
        additional_claims =create_additional_claims_from_user(user)
        access_token = create_access_token(user.username, additional_claims=additional_claims)
        refresh_token = create_refresh_token(user.username, additional_claims=additional_claims)
        logger.log("Logged in as: " + user.username)
        return {"access_token": access_token, "refresh_token": refresh_token}



@user_ns.route('/register')
class SignUp(Resource):
    ''' User signup endpoint.'''
    @user_ns.expect(CreateUserForm.api_model(user_ns))
    @handle_exceptions
    def post(self):
        """Create a new user"""
        user_json = request.get_json()
        form = CreateUserForm(user_json)
        user = form.to_domain([UserRole(UserRole.CLIENT.value)])
        logger.log(f'Creating User {user.username}')
        response = creating_handler.handle(user)
        return UserResponseForm(response).to_dict()


delete_model = user_ns.model("DeleteUser", {
    "id": fields.String(required=True)
})


@user_ns.route('/change_status')
class ChangeStatusEndPoint(Resource):
    ''' User status change endpoint.'''
    @user_ns.expect(ChangeStatusForm.api_model(user_ns))
    @user_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def put(self):
        """Change the status of an existing user (admin only)"""
        form = ChangeStatusForm(request.get_json())
        logger.log(f'Changing status for User {form.id} to {form.user_status}')
        return change_status_handler.handle(form.to_domain()).to_dict()
    

@user_ns.route('/delete')
class DeleteUser(Resource):
    ''' User deletion endpoint.'''
    @user_ns.expect(delete_model)
    @user_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def delete(self):
        """Delete an existing user (admin only)"""
        user_id = request.get_json().get("id")
        logger.log(f'Deleting User {user_id}')
        return delete_handler.handle(user_id)

@user_ns.route('/')
class UserList(Resource):
    ''' Endpoint to get a list of users.'''
    @user_ns.doc(security="Bearer Auth")
    @user_ns.expect(InputForm.api_model(user_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        """Get a list of users (admin only)"""
        form = InputForm(request.get_json())
        data = get_all_users_handler.handle(form)
        return data.to_dict()