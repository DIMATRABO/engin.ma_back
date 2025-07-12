from use_cases.admin.checkAdmin import CheckAdmin
from gateways.admin.repository import Repository as AdminRepo
from gateways.log import Log
from flask_jwt_extended import get_jwt
from functools import wraps
from exceptions.exception import UnauthorizedException


checkAdmin = CheckAdmin(AdminRepo())
logger = Log()

def check_admin_permission(permission):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            try:
                if not  get_jwt()["authority"] in permission:
                    raise UnauthorizedException()
            except:
                raise UnauthorizedException()
            
            return func(*args, **kwargs)

        return decorated_function

    return decorator
