
from models.city import City
from gateways.dataBaseSession.session_context import SessionContext
from gateways.city.repository import Repository as CityRepository


class GetAll:
    def __init__(self):
        self.repo= CityRepository()
        self.session_context = SessionContext()

    def handle(self)->list[City]:
        with self.session_context as session:
            return  self.repo.get_all(session)
          
            


