from dotenv import load_dotenv
import os

load_dotenv()
class Config_handler :
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config_handler, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
      
        # access the environment variables using `os.getenv()`
        self.app_name = os.getenv('APP_NAME')
        self.app_host = os.getenv('APP_HOST')
        self.app_port = os.getenv('APP_PORT')
        self.app_debug = os.getenv('APP_DEBUG')
        self.is_production = os.getenv('IS_PRODUCTION')
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.logging_level = os.getenv('LOGGING_LEVEL')
        self.logging_filename = os.getenv('LOGGING_FILENAME')
        self.jwt_secret = os.getenv('JWT_SECRET')
        self.jwt_expiration = int(os.getenv('JWT_EXPIRATION'))
        self.jwt_refresh_expiration = int(os.getenv('JWT_REFRESH_EXPIRATION'))
        self.enable_swagger_ui = os.getenv('ENABLE_SWAGGER_UI', 'False').lower() == 'true'