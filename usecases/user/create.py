'''This module handles the creation of a new user account.'''
import bcrypt
from models.user import User
from gateways.user.repository import Repository as UserRepository
from gateways.dataBaseSession.session_context import SessionContext
from exceptions.exception import UsernameAlreadyExists , EmailAlreadyExists


class Create:
    '''Use case for creating a new user account. It checks if the username and email are unique, hashes the password, and saves the user to the database.'''
    def __init__(self):
        self.repo=UserRepository()
        self.session_context = SessionContext()

    def handle(self, user:User) -> User:
        '''Handles the creation of a new user account. It checks for unique username and email, hashes the password, and saves the user to the database.'''
        with self.session_context as session:
            if not self.repo.get_user_by_username(session,user.username):
                if not self.repo.get_user_by_email(session,user.email):    
                    user.password = (bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())).decode("utf-8")
                    saved_user = self.repo.save(session , user)
                    return saved_user
                raise EmailAlreadyExists
            raise UsernameAlreadyExists
