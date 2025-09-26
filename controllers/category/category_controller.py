''' Categorycontroller.py'''
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from gateways.log import Log
from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission

from dto.input.category.create_category_form import CreateCategoryForm

from usecases.category.create import Create
from usecases.category.get_all import GetAll
from usecases.category.delete import Delete

# Create a namespace
category_ns = Namespace("categories", description="Categories management operations")
logger = Log()
create_category_handler = Create()
get_all_categories_handler = GetAll()
delete_category_handler = Delete()

@category_ns.route('')
class CreateEndpoint(Resource):
    '''Endpoint to create a new category.'''
    @category_ns.doc(security="Bearer Auth")
    @category_ns.expect(CreateCategoryForm.api_model(category_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        '''Create a new category (admin only)'''
        form = CreateCategoryForm(request.get_json())
        return create_category_handler.handle(form.to_domain()).to_dict()
    
    @category_ns.doc(
    params={
            "Accept-Language": {
                "description": "Preferred language for the response (e.g. 'en', 'fr', 'ar')",
                "in": "header",
                "type": "string",
                "required": False
            }
        }
    )
    @handle_exceptions
    def get(self):
        '''Get all categories'''
        accept_language = request.headers.get("Accept-Language", "en") 
        categories = get_all_categories_handler.handle(accept_language)
        return [category.to_dict() for category in categories]
    
@category_ns.route('/<string:category_id>')
class CategoryDeleteEndpoint(Resource):
    '''Endpoint to delete a category by ID.'''
    @category_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def delete(self, category_id):
        '''Delete a category by ID (admin only)'''
        delete_category_handler.handle(category_id)
        return {"message": "Category deleted successfully"}