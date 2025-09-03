
''' Use case for loading booking details by id '''
from models.booking import Booking
from usecases.equipment.load import Load as EquipmentLoad
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepository


class Load:
    ''' retrieve booking details by id use case '''
    def __init__(self):
        ''' initialize the Load use case with user and equipment repositories '''
        self.user_repo= UserRepository()
        self.load_equipment_usecase = EquipmentLoad()
        self.session_context = SessionContext()

    def handle(self,session, boking:Booking)->Booking:
        ''' retrieve booking details by id '''
        if not session:
            with self.session_context as session:
                if boking.client and boking.client.id:
                    boking.client= self.user_repo.get_user_by_id(session, boking.client.id)
                if boking.pilot and boking.pilot.id:
                    boking.pilot= self.user_repo.get_user_by_id(session, boking.pilot.id)
                if boking.equipment and boking.equipment.id:
                    boking.equipment= self.load_equipment_usecase.handle(session, boking.equipment)
            return boking
        else:
            if boking.client and boking.client.id:
                boking.client= self.user_repo.get_user_by_id(session, boking.client.id)
            if boking.pilot and boking.pilot.id:
                boking.pilot= self.user_repo.get_user_by_id(session, boking.pilot.id)
            if boking.equipment and boking.equipment.id:
                boking.equipment= self.load_equipment_usecase.handle(session, boking.equipment)
            return boking