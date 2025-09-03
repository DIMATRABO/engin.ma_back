
''' Use case for loading booking details by id '''
from models.booking import Booking
from usecases.equipment.load import Load as EquipmentLoad
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepository
from gateways.equipment.repository import Repository as EquipmentRepository



class Load:
    ''' retrieve booking details by id use case '''
    def __init__(self):
        ''' initialize the Load use case with user and equipment repositories '''
        self.user_repo= UserRepository()
        self.equipment_repo= EquipmentRepository()
        self.load_equipment_usecase = EquipmentLoad()
        self.session_context = SessionContext()


    def handle(self,session, booking:Booking)->Booking:
        ''' retrieve booking details by id '''
        if not session:
            with self.session_context as session:
                if booking.client and booking.client.id:
                    booking.client= self.user_repo.get_user_by_id(session, booking.client.id)
                if booking.pilot and booking.pilot.id:
                    booking.pilot= self.user_repo.get_user_by_id(session, booking.pilot.id)
                if booking.equipment and booking.equipment.id:
                    booking.equipment=self.equipment_repo.get_equipment_by_id(session, booking.equipment.id)
                    booking.equipment= self.load_equipment_usecase.handle(session, booking.equipment)

        else:
            if booking.client and booking.client.id:
                booking.client= self.user_repo.get_user_by_id(session, booking.client.id)
            if booking.pilot and booking.pilot.id:
                booking.pilot= self.user_repo.get_user_by_id(session, booking.pilot.id)
            if booking.equipment and booking.equipment.id:
                booking.equipment=self.equipment_repo.get_equipment_by_id(session, booking.equipment.id)
                booking.equipment= self.load_equipment_usecase.handle(session, booking.equipment)
                
        return booking