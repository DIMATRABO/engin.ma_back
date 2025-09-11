from gateways.dataBaseSession.session_context import SessionContext
from gateways.city.repository import Repository as CityRepository

from dto.output.city.city_response_form import CityResponseForm


class GetAll:
    def __init__(self):
        self.repo= CityRepository()
        self.session_context = SessionContext()

    def handle(self, language)->list[CityResponseForm]:
        with self.session_context as session:
            cities = self.repo.get_all(session)
            return [CityResponseForm(city, language) for city in cities]
          
            


