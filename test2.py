from models.equipment_image import EquipmentImage
from gateways.equipment_image.repository import Repository 
from gateways.dataBaseSession.session_context import SessionContext


image = EquipmentImage('123','eq-001','eq-001-name')
repo = Repository()
session_context = SessionContext()
with session_context as session:
    # Save the image using the repository
    print(repo.save(session, image))
