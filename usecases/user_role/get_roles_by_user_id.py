from gateways.user_role.repository import Repository as UserRoleRepository
from gateways.dataBaseSession.session_context import SessionContext

class GetRolesByUserId:
    ''' Use case for getting roles by user id '''
    def __init__(self):
        self.session_context = SessionContext()
        self.user_role_repository = UserRoleRepository()

    def handle(self, session, user_id):
        ''' retrieve roles by user id '''
        with self.session_context as session:
            roles = self.user_role_repository.get_user_roles_by_user_id(session, user_id)
        return roles
