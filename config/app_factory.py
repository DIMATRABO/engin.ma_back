from flask import Flask
from config.flask_config import configure_flask_app
from config.extensions import init_extensions
from config.api_config import setup_api
from config.error_handlers import register_error_handlers


def create_app():

    app = Flask(__name__)
    
    # Configure Flask application settings
    configure_flask_app(app)
    
    # Initialize all extensions (JWT, CORS, etc.)
    init_extensions(app)
    
    # Setup Flask-RESTX API and register namespaces
    setup_api(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    return app