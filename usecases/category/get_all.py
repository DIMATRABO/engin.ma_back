from gateways.dataBaseSession.session_context import SessionContext
from gateways.category.repository import Repository as CategoryRepository

from dto.output.category.category_response_form import CategoryResponseForm

class GetAll:
    def __init__(self):
        self.repo= CategoryRepository()
        self.session_context = SessionContext()

    def handle(self,language)->list[CategoryResponseForm]:
        with self.session_context as session:
            categories =  self.repo.get_all(session)
            return [CategoryResponseForm(category, language) for category in categories]