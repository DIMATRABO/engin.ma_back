''' Decorator to check if the user has the required permission. '''
from functools import wraps
from flask_jwt_extended import get_jwt
from gateways.log import Log
from exceptions.exception import UnauthorizedException

logger = Log()

def check_permission(permission):
    ''' Decorator to check if the user has the required permission.'''
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            try:
                authorities = get_jwt()["authority"].split(",")
                permissions = permission.split(",")

                logger.log("authorities: " + str(authorities) + ", permissions: " + str(permissions) +"condition: " + str(set(authorities) & set(permissions)))
                if not set(authorities) & set(permissions):
                    raise UnauthorizedException()
            except:
                raise UnauthorizedException()
            return func(*args, **kwargs)
        return decorated_function
    return decorator
