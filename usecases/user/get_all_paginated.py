''' Use Case: Get all users with pagination support'''
from dto.input.pagination.input_form import InputForm
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepo


class GetAllUsersPaginated:
    ''' Use case for retrieving all users with pagination support.'''
    def __init__(self):
        ''' Initializes the GetAllUsersPaginated use case.'''
        self.user_repo=UserRepo()
        self.session_context = SessionContext()

    def handle(self, input_form : InputForm):
        ''' Handles the retrieval of all users with pagination.'''
        with self.session_context as session:
                return self.user_repo.get_all_paginated(session,input_form)    