from models.model import Model
from gateways.dataBaseSession.session_context import SessionContext
from gateways.model.repository import Repository as ModelRepository
from usecases.model.load import Load


class GetAll:
    def __init__(self):
        self.load = Load()
        self.repo= ModelRepository()
        self.session_context = SessionContext()

    def handle(self)->list[Model]:
        with self.session_context as session:
            models =  self.repo.get_all(session)
            for model in models:
                model = self.load.handle(session, model)
            return models

          
            


