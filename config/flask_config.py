from datetime import timedelta
from config.config_handler import Config_handler


def configure_flask_app(app):
    """Configure Flask application settings."""
    config = Config_handler()
    
    app.config.update({
        'TIMEOUT': 300,  # 5 minutes timeout
        'JWT_SECRET_KEY': config.jwt_secret,
        'JWT_ACCESS_TOKEN_EXPIRES': timedelta(minutes=config.jwt_expiration),
        'JWT_REFRESH_TOKEN_EXPIRES': timedelta(minutes=config.jwt_refresh_expiration),
        'JSON_SORT_KEYS': False,  # Maintain JSON key order
        # Add other Flask-specific configurations here
        'JSONIFY_PRETTYPRINT_REGULAR': True,
    })