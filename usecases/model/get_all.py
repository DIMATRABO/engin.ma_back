
from models.model import Model
from gateways.dataBaseSession.session_context import SessionContext
from gateways.model.repository import Repository as ModelRepository


class GetAll:
    def __init__(self):
        self.repo= ModelRepository()
        self.session_context = SessionContext()

    def handle(self)->list[Model]:
        with self.session_context as session:
            return  self.repo.get_all(session)
          
            


