
''' Use case for loading equipment details by id '''
from models.equipment import Equipment

from usecases.city.get_by_id import GetById as GetCityById
from usecases.brand.get_by_id import GetById as GetBrandById
from usecases.user.details import Details as GetUserById
from usecases.model.get_by_id import GetById as GetModelById
from usecases.category.get_by_id import GetById as GetCategoryById
from usecases.equipment_image.get_all_by_equipment_id import GetAllByEquipmentId

from gateways.dataBaseSession.session_context import SessionContext

class Load:
    ''' retrieve equipment details by id use case '''
    def __init__(self):
        ''' initialize the Load use case with user and equipment repositories '''
        self.city_getter = GetCityById()
        self.brand_getter = GetBrandById()
        self.model_getter = GetModelById()
        self.user_getter = GetUserById()
        self.category_getter = GetCategoryById()
        self.images_getter = GetAllByEquipmentId()
        self.session_context = SessionContext()

    def handle(self,session, equipment:Equipment)->Equipment:
        ''' retrieve equipment details by id '''
        if not session:
            with self.session_context as session:
                if equipment.owner and equipment.owner.id:
                    equipment.owner= self.user_getter.handle(equipment.owner.id)
                if equipment.pilot and equipment.pilot.id:
                    equipment.pilot= self.user_getter.handle(equipment.pilot.id)
                if equipment.brand and equipment.brand.id:
                    equipment.brand= self.brand_getter.handle(equipment.brand.id)
                if equipment.model and equipment.model.id:
                    equipment.model= self.model_getter.handle(equipment.model.id)
                if equipment.city and equipment.city.id:
                    equipment.city= self.city_getter.handle(equipment.city.id)
                if equipment.category and equipment.category.id:
                    equipment.category= self.category_getter.handle(equipment.category.id)
                equipment.images= self.images_getter.handle(equipment.id)
            return equipment
        else:
            if equipment.owner and equipment.owner.id:
                equipment.owner= self.user_getter.handle(equipment.owner.id)
            if equipment.pilot and equipment.pilot.id:
                equipment.pilot= self.user_getter.handle(equipment.pilot.id)
            if equipment.brand and equipment.brand.id:
                equipment.brand= self.brand_getter.handle(equipment.brand.id)
            if equipment.model and equipment.model.id:
                equipment.model= self.model_getter.handle(equipment.model.id)
            if equipment.city and equipment.city.id:
                equipment.city= self.city_getter.handle(equipment.city.id)
            if equipment.category and equipment.category.id:
                equipment.category= self.category_getter.handle(equipment.category.id)
            equipment.images= self.images_getter.handle(equipment.id)
        return equipment