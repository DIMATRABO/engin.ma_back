''' configration for Flask-RESTX API '''
from flask_restx import Api
from config.config_handler import ConfigHandler
from controllers.health_check_controller import healthcheck_ns
from controllers.auth.auth_controller import auth_ns
from controllers.contact_us.contact_us import contact_ns
from controllers.user.user_controller import user_ns
from controllers.city.city_controller import city_ns
from controllers.brand.brand_controller import brand_ns
from controllers.model.model_controller import model_ns
from controllers.category.category_controller import category_ns
from controllers.equipment_image.equipment_image_controller import equipment_image_ns
from controllers.equipment.equipment_controller import equipments_ns
from controllers.booking.booking_controller import booking_ns
from controllers.fields_of_activity.fields_of_activity_controler import foa_ns
from controllers.owner.owner_controller import owner_ns
from controllers.pilote.pilote_controller import pilote_ns
from controllers.review.review_controller import review_ns




def setup_api(app):
    """Setup Flask-RESTX API and register all namespaces."""
    config = ConfigHandler()


    authorizations = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
        }
    }

    # Create API instance
    api = Api(
        app,
        version="1.0",
        title="EnginChantier.ma API",
        description="Swagger documentation for EnginChantier.ma API",
        authorizations=authorizations,
        doc="/docs" if config.enable_swagger_ui else False,
        validate=True,  # Enable request validation
        ordered=True    # Maintain endpoint order in docs
    )
    
    # Register all namespaces
    register_namespaces(api)
    
    return api


def register_namespaces(api):
    """Register all API namespaces."""

    api.add_namespace(healthcheck_ns, path="/health")
    api.add_namespace(contact_ns, path="/contact")
    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(user_ns, path="/users")
    api.add_namespace(owner_ns, path="/owners")
    api.add_namespace(pilote_ns, path="/pilotes")
    api.add_namespace(city_ns, path="/cities")
    api.add_namespace(brand_ns, path="/brands")
    api.add_namespace(model_ns, path="/models")
    api.add_namespace(category_ns, path="/categories")
    api.add_namespace(equipment_image_ns, path="/equipment-images")
    api.add_namespace(equipments_ns, path="/equipments")
    api.add_namespace(booking_ns, path="/bookings")
    api.add_namespace(foa_ns, path="/foa")
    api.add_namespace(review_ns, path="/reviews")