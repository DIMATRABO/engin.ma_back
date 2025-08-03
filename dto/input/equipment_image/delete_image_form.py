''' DTO for deleting an equipment image. '''
from flask_restx import Namespace, fields
from dto.input.validator import required, valid_string
from models.equipment_image import EquipmentImage

class DeleteImageForm:
    """
    Form for deleting an equipment image.
    """
    def __init__(self, json_image: str):
        self.id = required("id", json_image)
        self.id = valid_string(self.id)

    def to_domain(self):
        ''' Converts the form to a domain model. '''
        return EquipmentImage(id=self.id, equipment_id=None, url=None)

    @staticmethod
    def api_model(namespace: Namespace):
        ''' Returns the API model for the form. '''
        return namespace.model('deleteImageForm', {
            'id': fields.String(required=True, description='ID of the image to delete')
        })