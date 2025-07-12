from functools import wraps
from exceptions.exception import *
from json import loads
from gateways.log import Log
from gateways.config_handler import Config_handler 
import traceback

config = Config_handler()
logging = Log(config.app_debug)

def handle_exceptions(endpoint_function):
    @wraps(endpoint_function)
    def wrapper(*args, **kwargs):
        try:
            result = endpoint_function(*args, **kwargs)
            return result,200
   
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
        
        except PaymentRequiredException as e:    
            return {"error": str(e)}, 402
        
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
        
        except InvalidBotException as e:
            logging.debug(str(e))
            return loads(str(e)), 400
        
        except VariableTypeError as e:
            logging.debug(str(e))
            return {"error": str(e)}, 400
        
        except ExchangeIntegrationError as e:
            logging.error(f"Exchange integration error: {e}")
            return {"error": "Exchange Integration Error", "details": str(e)}, 422
        except InvalidJsonException as e:
            logging.debug(str(e))
            return {"error": str(e)}, 502
        
        except Exception as e:
            if config.app_debug == "true":
                return {"error": "Internal Server Error --" + f'{str(e)} -- Traceback: -- {traceback.format_exc()}'}, 500
            else:
                return {"error": "Internal Server Error"}, 500
       
        
        
       

    return wrapper
