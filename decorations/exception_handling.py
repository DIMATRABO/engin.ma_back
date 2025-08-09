from functools import wraps
from flask import Response
from exceptions.exception import *
from flask_jwt_extended.exceptions import NoAuthorizationError
from gateways.log import Log
from config.config_handler import ConfigHandler
import traceback

config = ConfigHandler()
logging = Log(config.app_debug)

def handle_exceptions(endpoint_function):
    @wraps(endpoint_function)
    def wrapper(*args, **kwargs):
        try:
            result = endpoint_function(*args, **kwargs)
            if isinstance(result, Response):
                return result
            return result, 200

        except UsernameAlreadyExists as e:
            logging.debug(str(e))
            return {"error": str(e)}, 400

        except EmailAlreadyExists as e:
            logging.debug(str(e))
            return {"error": str(e)}, 400

        except InvalidRequestException as e:
            logging.debug(str(e))
            return {"error": str(e)}, 400

        except UnauthorizedException as e:
            logging.debug(str(e))
            return {"error": str(e)}, 401

        except NoAuthorizationError as e:  # <-- Add this block
            logging.debug(str(e))
            return {"error": "Missing or invalid Authorization token"}, 401

        except EmailNotVerifiedException as e:
            logging.debug(str(e))
            return {"error": str(e)}, 428

        except UserBlockedException as e:
            logging.debug(str(e))
            return {"error": str(e)}, 403

        except NotFoundException as e:
            logging.debug(str(e))
            return {"error": str(e)}, 404

        except ValidationException as e:
            logging.debug(str(e))
            return {"error": str(e)}, 400

        except BadGatewayException as e:
            logging.debug(str(e))
            return {"error": str(e)}, 502

        except VariableTypeError as e:
            logging.debug(str(e))
            return {"error": str(e)}, 400

        except Exception as e:
            if config.app_debug == "true":
                return {"error": "Internal Server Error --" + f'{str(e)} -- Traceback: -- {traceback.format_exc()}'}, 500
            else:
                return {"error": "Internal Server Error"}, 500

    return wrapper
