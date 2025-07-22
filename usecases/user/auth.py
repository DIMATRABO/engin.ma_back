''' Authentication use case module for handling user login and related operations. '''

import bcrypt
from models.user import User
from dto.input.user.login_form import LoginForm
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepo
from exceptions.exception import EmailNotVerifiedException
from exceptions.exception import UserBlockedException, UnauthorizedException


class Auth:
    def __init__(self):
        self.repo = UserRepo()
        self.session_context = SessionContext()

    def handle(self, auth_form:LoginForm)-> User:
        ''' Handles user authentication by verifying username/email and password.'''
        with self.session_context as session:
            user = self.repo.get_user_by_username_or_email(session , auth_form.username_or_email)
            if not user is None:
                if bcrypt.checkpw(auth_form.password.encode('utf-8'), user.password.encode('utf-8')):
                    if user.user_status.value == "ACTIVE":
                            return user
                    elif user.user_status.value == "PENDING":
                        raise EmailNotVerifiedException()
                    elif user.user_status.value == "BLOCKED":
                        raise UserBlockedException("User blocked")
                else:
                    status_message = "Bad Username or password "
                    raise UnauthorizedException(status_message)
            else:        
                status_message = "Bad Username or password "
                raise UnauthorizedException(status_message)