''' Use case for updating a user's status in the system.'''
from models.user import User
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepo

class ChangeStatus:
    '''Use case for updating a user's status in the system.'''
    def __init__(self):
        self.repo=UserRepo()
        self.session_context = SessionContext()

    def handle(self, user:User)-> User:
        '''Handle the update of a user's status.'''
        with self.session_context as session:
            return self.repo.change_status(session , user)
    