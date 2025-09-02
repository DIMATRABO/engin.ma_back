
''' Use case for loading booking details by id '''
from models.booking import Booking
from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment.repository import Repository as EquipmentRepository
from gateways.user.repository import Repository as UserRepository


class Load:
    ''' retrieve booking details by id use case '''
    def __init__(self):
        ''' initialize the Load use case with user and equipment repositories '''
        self.user_repo= UserRepository()
        self.equipment_repo= EquipmentRepository()
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
                    boking.equipment= self.equipment_repo.get_equipment_by_id(session, boking.equipment.id)
            return boking
        else:
            if boking.client and boking.client.id:
                boking.client= self.user_repo.get_user_by_id(session, boking.client.id)
            if boking.pilot and boking.pilot.id:
                boking.pilot= self.user_repo.get_user_by_id(session, boking.pilot.id)
            if boking.equipment and boking.equipment.id:
                boking.equipment= self.equipment_repo.get_equipment_by_id(session, boking.equipment.id)
            return boking