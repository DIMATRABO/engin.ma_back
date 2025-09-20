from gateways.dataBaseSession.session_context import SessionContext
from gateways.review.repository import Repository as ReviewRepository
from models.review import Review

class GetAll:
    def __init__(self):
        self.repo= ReviewRepository()
        self.session_context = SessionContext()

    def handle(self, pilot_id: str)->list[Review]:
        with self.session_context as session:
            return self.repo.get_by_pilot_id(session, pilot_id)