''' Get all users with role PILOT'''
from models.user_role import UserRole
from dto.output.user.user_simple import UserSimple
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepository


class GetAll:
    ''' Get all users with role PILOT'''
    def __init__(self):
        self.repo= UserRepository()
        self.session_context = SessionContext()

    def handle(self)->list[UserSimple]:
        ''' Get all users with role PILOT'''
        with self.session_context as session:
            role = UserRole.PILOT
            return  self.repo.get_all_simple_by_role(session, role)
          
            


