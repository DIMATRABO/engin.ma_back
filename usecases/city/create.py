'''This module handles the creation of a new city.'''
from models.city import City
from gateways.city.repository import Repository as CityRepository
from gateways.dataBaseSession.session_context import SessionContext

class Create:
    ''' Use case for creating a new city. It checks if the city name is unique and saves the city to the database.'''
    def __init__(self):
        self.repo=CityRepository()
        self.session_context = SessionContext()

    def handle(self, city:City) -> City:
        '''Handles the creation of a new city. It checks for unique city name and saves the city to the database.'''
        with self.session_context as session:
            saved_city = self.repo.save(session , city)
            return saved_city