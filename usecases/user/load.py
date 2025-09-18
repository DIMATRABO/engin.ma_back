''' Use case for loading user details by id '''
from models.user import User

from usecases.user_role.get_roles_by_user_id import GetRolesByUserId
from gateways.dataBaseSession.session_context import SessionContext


class Load:
    ''' retrieve user details by id use case '''
    def __init__(self):
        ''' initialize the Load use case with user and user repositories '''
        self.roles_getter=GetRolesByUserId()
        self.session_context = SessionContext()

    def handle(self,session, user:User)->User:
        ''' retrieve user details by id '''
        if not session:
            with self.session_context as session:
                if user.id:
                    user.roles= self.roles_getter.handle(session,user.id)
            return user
        else:
            if user.id:
                user.roles= self.roles_getter.handle(session,user.id)
            return user