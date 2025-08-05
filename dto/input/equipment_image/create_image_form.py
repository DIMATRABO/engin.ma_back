''' CreateImageForm DTO '''
from flask_restx import Namespace, fields
from models.equipment_image import EquipmentImage
from dto.input.validator import required, valid_string

class CreateImageForm:
    ''' Form to create a equipment image '''
    def __init__(self, equipment_id=None, file_url=None):
        ''' Initializes the form with equipment ID and file URL. '''
        self.equipment_id = valid_string(equipment_id)
        self.image_url = file_url  # generated in backend, not sent by client

    def to_domain(self):
        ''' Converts the form to a domain object. '''
        return EquipmentImage(
            id=None,
            equipment_id=self.equipment_id,
            url=self.image_url
        )
    
    @staticmethod
    def api_model(namespace: Namespace):
        ''' Returns the API model for documentation (excluding image_url input). '''
        return namespace.model('CreateImageForm', {
            'equipment_id': fields.String(required=True, description='ID of the equipment'),
            # No image_url here because it's generated automatically
        })
