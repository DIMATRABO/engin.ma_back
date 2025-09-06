
from models.category import Category
from gateways.dataBaseSession.session_context import SessionContext
from gateways.category.repository import Repository as CategoryRepository


class GetAll:
    def __init__(self):
        self.repo= CategoryRepository()
        self.session_context = SessionContext()

    def handle(self)->list[Category]:
        with self.session_context as session:
            return  self.repo.get_all(session)