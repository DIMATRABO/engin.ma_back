from forms.user.userDetailsForm import UserDetailsForm
from gateways.dataBaseSession.sessionContext import SessionContext
from gateways.user.abstraction.repositoryAbstraction import RepositoryAbstraction as UserRepo



class Details:
    def __init__(self ,  repo:UserRepo):
        self.repo=repo
        self.sessionContext = SessionContext()

    def handle(self, id:str)-> UserDetailsForm:
        with self.sessionContext as session:
            return self.repo.getUserById(session , id)