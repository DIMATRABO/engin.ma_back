
''' Use case for loading model details by id '''
from models.model import Model

from usecases.brand.get_by_id import GetById as GetBrandById
from usecases.category.get_by_id import GetById as GetCategoryById

from gateways.dataBaseSession.session_context import SessionContext

class Load:
    ''' retrieve model details by id use case '''
    def __init__(self):
        ''' initialize the Load use case with user and model repositories '''

        self.brand_getter = GetBrandById()
        self.category_getter = GetCategoryById()
        self.session_context = SessionContext()

    def handle(self,session, model:Model)->Model:
        ''' retrieve model details by id '''
        if not session:
            with self.session_context as session:
                if model.brand and model.brand.id:
                    model.brand= self.brand_getter.handle(model.brand.id)
                if model.category and model.category.id:
                    model.category= self.category_getter.handle(model.category.id)
            return model
        else:
            if model.brand and model.brand.id:
                model.brand= self.brand_getter.handle(model.brand.id)
            if model.category and model.category.id:
                model.category= self.category_getter.handle(model.category.id)
        return model