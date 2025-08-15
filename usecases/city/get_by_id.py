
'''This file is part of the City Management System project.'''
from models.city import City
from gateways.dataBaseSession.session_context import SessionContext
from gateways.city.repository import Repository as CityRepository


class GetById:
    ''' retrieve city details by id '''
    def __init__(self):
        ''' initialize the GetById use case with a city repository '''
        self.repo= CityRepository()
        self.session_context = SessionContext()

    def handle(self, id_:str)->City:
        ''' retrieve city details by id '''
        with self.session_context as session:
            return  self.repo.get_by_id(session, id_)