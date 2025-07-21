''' UserController.py'''
from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import  jwt_required


from gateways.log import Log
from decorations.exception_handling import handle_exceptions

from dto.input.user.create_user_form import CreateUserForm
from dto.output.user.user_response_form import UserResponseForm

from usecases.user.create import Create
from usecases.user.delete import Delete


# Create a namespace
user_ns = Namespace("user", description="User management operations")
logger = Log()
delete_handler = Delete()
creating_handler = Create()


@user_ns.route('/signup')
class SignUp(Resource):
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
    @user_ns.expect(delete_model)
    @user_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    def delete(self):
        """Delete an existing user (admin only)"""
        user_id = request.get_json().get("id")
        logger.log(f'Deleting User {user_id}')
        return delete_handler.handle(user_id), 200
