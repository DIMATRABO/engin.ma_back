'''This module handles the creation of a new review.'''
from models.review import Review
from gateways.review.repository import Repository as ReviewRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    ''' Use case for creating a new review.'''
    def __init__(self):
        self.repo=ReviewRepository()
        self.session_context = SessionContext()

    def handle(self, review:Review) -> Review:
        '''Handles the creation of a new review.'''
        with self.session_context as session:
            saved_review = self.repo.save(session , review)
            return saved_review