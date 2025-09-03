
''' Use case for loading equipment details by id '''
from models.equipment import Equipment
from gateways.dataBaseSession.session_context import SessionContext
from gateways.equipment.repository import Repository as EquipmentRepository
from gateways.user.repository import Repository as UserRepository
from gateways.brand.repository import Repository as BrandRepository
from gateways.model.repository import Repository as ModelRepository
from gateways.city.repository import Repository as CityRepository


class Load:
    ''' retrieve equipment details by id use case '''
    def __init__(self):
        ''' initialize the Load use case with user and equipment repositories '''
        self.user_repo= UserRepository()
        self.equipment_repo= EquipmentRepository()
        self.brand_repo= BrandRepository()
        self.model_repo= ModelRepository()
        self.city_repo= CityRepository()

        self.session_context = SessionContext()

    def handle(self,session, equipment:Equipment)->Equipment:
        ''' retrieve equipment details by id '''
        if not session:
            with self.session_context as session:
                if equipment.owner and equipment.owner.id:
                    equipment.owner= self.user_repo.get_user_by_id(session, equipment.owner.id)
                if equipment.pilot and equipment.pilot.id:
                    equipment.pilot= self.user_repo.get_user_by_id(session, equipment.pilot.id)
                if equipment.brand and equipment.brand.id:
                    equipment.brand= self.brand_repo.get_by_id(session, equipment.brand.id)
                if equipment.model and equipment.model.id:
                    equipment.model= self.model_repo.get_by_id(session, equipment.model.id)
                if equipment.city and equipment.city.id:
                    equipment.city= self.city_repo.get_by_id(session, equipment.city.id)
            return equipment
        else:
            if equipment.owner and equipment.owner.id:
                equipment.owner= self.user_repo.get_user_by_id(session, equipment.owner.id)
            if equipment.pilot and equipment.pilot.id:
                equipment.pilot= self.user_repo.get_user_by_id(session, equipment.pilot.id)
            if equipment.brand and equipment.brand.id:
                equipment.brand= self.brand_repo.get_by_id(session, equipment.brand.id)
            if equipment.model and equipment.model.id:
                equipment.model= self.model_repo.get_by_id(session, equipment.model.id)
            if equipment.city and equipment.city.id:
                equipment.city= self.city_repo.get_by_id(session, equipment.city.id)
            return equipment