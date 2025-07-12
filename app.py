from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from gateways.config_handler import Config_handler

from controllers.healthCheckController import healthcheck_bp


from flask_cors import CORS

config = Config_handler()


app = Flask(__name__)
app.config['TIMEOUT'] = 300  # 5 minutes timeout
app.config["JWT_SECRET_KEY"] = config.jwt_secret
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=config.jwt_expiration)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(minutes=config.jwt_refresh_expiration)
jwt = JWTManager(app)

@app.errorhandler(404)
def not_found(error):
    return jsonify(error='Not found'), 404

app.register_error_handler(404, not_found)
app.register_blueprint(healthcheck_bp,url_prefix = "/health")

CORS(app)

if __name__ == "__main__":
    app.run(host=config.app_host, port=config.app_port , debug=config.app_debug)
    