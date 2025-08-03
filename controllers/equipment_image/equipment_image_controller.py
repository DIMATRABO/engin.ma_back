''' equipment image controller '''
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import  jwt_required

from gateways.log import Log
from decorations.exception_handling import handle_exceptions
from decorations.check_permission import check_permission


from dto.input.equipment_image.create_image_form import CreateImageForm
from dto.input.equipment_image.delete_image_form import DeleteImageForm



from usecases.equipment_image.get_all_by_equipment_id import GetAllByEquipmentId
from usecases.equipment_image.get_all import GetAll
from usecases.equipment_image.create import Create
from usecases.equipment_image.delete import Delete


# Create a namespace
equipment_image_ns = Namespace("equipment_images",
                               description="Equipment images management operations")
logger = Log()
create_image_handler = Create()
get_all_images_handler = GetAll()
get_all_by_equipment_id_handler = GetAllByEquipmentId()
delete_image_handler = Delete()
@equipment_image_ns.route('')
class EquipmentImageListEndpoint(Resource):
    '''Create or get all equipment images'''

    @equipment_image_ns.doc(security="Bearer Auth")
    @equipment_image_ns.expect(CreateImageForm.api_model(equipment_image_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        '''Create a new equipment image (admin only)'''
        form = CreateImageForm(request.get_json())
        return create_image_handler.handle(form.to_domain())

    @equipment_image_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self):
        '''Get all equipment images'''
        images = get_all_images_handler.handle()
        return [image.to_dict() for image in images]


@equipment_image_ns.route('/by-equipment/<string:equipment_id>')
class EquipmentImageByEquipmentEndpoint(Resource):
    '''Get images by equipment ID'''

    @equipment_image_ns.doc(security="Bearer Auth", params={'equipment_id': 'ID of the equipment'})
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self, equipment_id):
        '''Get all images associated with a specific equipment ID'''
        images = get_all_by_equipment_id_handler.handle(equipment_id)
        return [image.to_dict() for image in images]


@equipment_image_ns.route('/<string:image_id>')
class EquipmentImageDeleteEndpoint(Resource):
    '''Delete an equipment image'''

    @equipment_image_ns.doc(security="Bearer Auth", params={'image_id': 'ID of the image to delete'})
    @equipment_image_ns.expect(DeleteImageForm.api_model(equipment_image_ns))
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def delete(self, image_id):
        '''Delete an equipment image by ID (admin only)'''
        form = DeleteImageForm(request.get_json())
        form.image_id = image_id
        if delete_image_handler.handle(form.to_domain()):
            return {"message": "Image deleted successfully"}
        else:
            return {"message": "Image not found"}
