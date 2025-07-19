from flask_jwt_extended import JWTManager
from flask_cors import CORS


def init_extensions(app):
    """Initialize Flask extensions."""
    # Initialize JWT
    jwt = JWTManager(app)
    
    # Initialize CORS
    CORS(app)
    
    # Setup JWT callbacks
    setup_jwt_callbacks(jwt)
    
    return jwt


def setup_jwt_callbacks(jwt):
    """Setup JWT-specific callbacks and handlers."""
    from flask import jsonify
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({'error': 'Token has expired'}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({'error': 'Invalid token'}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({'error': 'Authorization token is required'}), 401