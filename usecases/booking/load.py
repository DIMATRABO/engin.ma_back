
''' Use case for loading booking details by id '''
from models.booking import Booking
from usecases.equipment.load import Load as EquipmentLoad
from gateways.dataBaseSession.session_context import SessionContext
from gateways.user.repository import Repository as UserRepository
from gateways.log import Log


class Load:
    ''' retrieve booking details by id use case '''
    def __init__(self):
        ''' initialize the Load use case with user and equipment repositories '''
        self.user_repo= UserRepository()
        self.load_equipment_usecase = EquipmentLoad()
        self.session_context = SessionContext()
        self.logger = Log()

    def handle(self,session, booking:Booking)->Booking:
        ''' retrieve booking details by id '''
        if not session:
            self.logger.debug(f'Session not provided, creating a new session to load booking details for booking ID: {booking.id}')
            with self.session_context as session:
                if booking.client and booking.client.id:
                    booking.client= self.user_repo.get_user_by_id(session, booking.client.id)
                if booking.pilot and booking.pilot.id:
                    booking.pilot= self.user_repo.get_user_by_id(session, booking.pilot.id)
                if booking.equipment and booking.equipment.id:
                    booking.equipment= self.load_equipment_usecase.handle(session, booking.equipment)

        else:
            self.logger.debug(f'Using provided session to load booking details for booking ID: {booking.id}')
            if booking.client and booking.client.id:
                booking.client= self.user_repo.get_user_by_id(session, booking.client.id)
            if booking.pilot and booking.pilot.id:
                booking.pilot= self.user_repo.get_user_by_id(session, booking.pilot.id)
            if booking.equipment and booking.equipment.id:
                booking.equipment= self.load_equipment_usecase.handle(session, booking.equipment)
                self.logger.debug(f'Loaded equipment details for booking ID: {booking.id} is {booking.equipment}')
        
        self.logger.debug(f'Loaded booking details for booking ID: {booking}')
        return booking