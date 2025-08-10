''' equipment image controller '''
from flask import request, send_from_directory
from flask_restx import Namespace, Resource, reqparse
from flask_jwt_extended import jwt_required
from werkzeug.datastructures import FileStorage
import os
from datetime import datetime

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

# Setup
UPLOAD_FOLDER = "uploads/equipment_images"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


create_image_handler = Create()
get_all_by_equipment_id_handler = GetAllByEquipmentId()
delete_image_handler = Delete()

# Parser for file uploads
upload_parser = reqparse.RequestParser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True, help='Image file')
upload_parser.add_argument('equipment_id', type=str, location='form', required=True)


def allowed_file(filename):
    '''Check if the uploaded file is allowed based on its extension'''
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@equipment_image_ns.route('')
class EquipmentImageListEndpoint(Resource):
    '''List and upload equipment images'''
    @equipment_image_ns.expect(upload_parser)
    @equipment_image_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def post(self):
        '''Upload and create a new equipment image (admin only)'''
        args = upload_parser.parse_args()
        file = args['file']
        equipment_id = args['equipment_id']

        if file and allowed_file(file.filename):
            extension = file.filename.rsplit('.', 1)[1].lower()
            timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
            filename = f"{timestamp}.{extension}"
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            # URL (adjust if hosted elsewhere or served statically)
            file_url = f"/{file_path}"

            # Now use DTO
            form = CreateImageForm(equipment_id=equipment_id,file_url=file_url)
            return create_image_handler.handle(form.to_domain()).to_dict()

        return {"error": "Invalid file type"}, 400


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


@equipment_image_ns.route('')
class EquipmentImageDeleteEndpoint(Resource):
    '''Delete an equipment image'''
    @equipment_image_ns.expect(DeleteImageForm.api_model(equipment_image_ns))
    @equipment_image_ns.doc(security="Bearer Auth")
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def delete(self):
        '''Delete an equipment image by ID (admin only)'''
        form = DeleteImageForm(request.get_json())
        if delete_image_handler.handle(form.to_domain()):
            return {"message": "Image deleted successfully"}
        else:
            return {"message": "Image not found"}
        

@equipment_image_ns.route("/<path:filename>")
class ExposeUploadedFiles(Resource):
    '''Endpoint to expose uploaded files for download'''
    @equipment_image_ns.doc(security="Bearer Auth", params={'filename': 'Path to the uploaded file'})
    @handle_exceptions
    @jwt_required()
    @check_permission("ADMIN")
    def get(self, filename):
        '''Get an uploaded file by filename'''
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
        UPLOAD_FOLDER_1 = os.path.join(BASE_DIR, "..", "..", "uploads","equipment_images")  # absolute path

        logger.log(f"Request to download file: {UPLOAD_FOLDER_1}/{filename}")
        return send_from_directory(UPLOAD_FOLDER_1, filename)
