''' usecases/user/details.py'''
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepo
from dto.output.user.user_response_form import UserResponseForm

class Details:
    ''' retrieve user details by id '''
    def __init__(self):
        ''' initialize the Details use case with a user repository '''
        self.repo= UserRepo()
        self.session_context = SessionContext()

    def handle(self, id_:str)-> UserResponseForm:
        ''' retrieve user details by id '''
        with self.session_context as session:
            return UserResponseForm(self.repo.get_user_by_id(session , id_))