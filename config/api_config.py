''' configration for Flask-RESTX API '''
from flask_restx import Api
from config.config_handler import ConfigHandler
from controllers.health_check_controller import healthcheck_ns
from controllers.user.user_controller import user_ns


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
        security="Bearer Auth",
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
    api.add_namespace(user_ns, path="/users")
    #api.add_namespace(auth_ns, path="/auth")