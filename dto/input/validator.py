
import re 
import json
from datetime import datetime
from exceptions.exception import ValidationException
from models.user_status import UserStatus
from models.fields_of_activity import FieldsOfActivity

def required(field_name , json):
            if(  not  field_name in  json):
                raise ValidationException(f'{field_name} required')
            else:
                return json[field_name]

def optional(field_name , json):
            if(  not  field_name in  json):
                return None
            else:
                return json[field_name]
          


def AZaz09(input_data):
    # Remove any characters that are not A-Z, a-z, or 0-9
    sanitized_data = re.sub(r'[^A-Za-z0-9]', '', input_data)
    return sanitized_data


def sanitize_input(input_data):
    # Remove any characters that might cause SQL injection
    sanitized_data = re.sub(r'[;\'"]', '', input_data)
    return sanitized_data

  
def valid_email_format(email):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            raise ValidationException("invalid email format")
        return email

def valid_phone_format(phone):
    phone_pattern = r'^0[567]\d{8}$'
    if not re.match(phone_pattern, phone):
        raise ValidationException("invalid phone format")
    return phone

        
def valid_password(password):
          if(  len(password) <8 ):
                raise ValidationException("password must have more than 8 characters")
          return password         


def valid_string(value):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValidationException("Invalid string format")
    # Check if the string is empty
    if not value.strip():
        return value
    # Define a regex pattern for allowed characters (alphanumeric and some safe special characters)
    pattern = r'^[a-zA-Z0-9\-_\+\.\s@,:()?\U0001F600-\U0001F64F\U00002702-\U000027B0\U000024C2-\U0001F251\U0001F680-\U0001F6FF\U000000A9-\U0001F636]*$'

    if not re.match(pattern, value):
        raise ValidationException("Invalid string format")
    return value

def valid_json(value):
    if value is None:
        return None
    try:
        # If input is already a string, try to parse it
        if isinstance(value, str):
            return json.loads(value)
        # If input is dict/list, verify it can be serialized to JSON
        else:
            json.dumps(value)  # Just checking serializability
            return value

    except (json.JSONDecodeError, TypeError) as e:
        raise ValidationException(f"Invalid JSON format: {str(e)}")


def valid_int(value):
    if value is None:
            return None
    if not isinstance(value, int):
        raise ValidationException("Invalid integer format")
    return value

def valid_float(value):
    if value is None:
            return None
    try:
         value = float(value)
    except:
        raise ValidationException("Invalid float format")
    return value


def valid_datetime(value, format):
        if value is None:
            return None
        try:
            return datetime.strptime(value ,format)
        except ValueError:
            raise ValidationException(f'{value} should be {format}')


def valid_boolean(value):
    if value is None:
        return None
    if not isinstance(value, bool):
        raise ValidationException("Invalid boolean format")
    return value

        
def valid_non_empty_list(value):
    if value is None:
        return None
    if not isinstance(value, list):
        raise ValidationException("Invalid list format")
    if len(value) == 0:
        raise ValidationException("List must not be empty")
    return value


def valid_order(value: str):
    ''' Validates the sorting order for pagination.'''
    if value not in ["asc", "desc", ""]:
        raise ValidationException("Invalid sorting Order")
    return value
    
def valid_webhook_payload(value):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValidationException("Invalid string format")
    # Check if the string is empty
    if not value.strip():
        return value

    # Define a regex pattern for the payload
    pattern = r'^([a-zA-Z0-9]+:[a-zA-Z0-9]+)(,([a-zA-Z0-9]+:[a-zA-Z0-9]+))*$'

    if not re.match(pattern, value):
        raise ValidationException("Invalid webhook payload format")
    
    return value

def valid_status(value):
    ''' Validates the user status by checking if it is a valid UserStatus.'''
    try:
        UserStatus(value.upper())
        return value.upper()
    except Exception as exception:
        raise ValidationException(f"Invalid user status: {value}. Error: {str(exception)}")
    
def valid_field_of_activity(value):
    ''' Validates the field of activity by checking if it is a valid FieldOfActivity.'''
    try:
        FieldsOfActivity(value.upper())
        return value.upper()
    except Exception as exception:
        raise ValidationException(f"Invalid field of activity: {value}. Error: {str(exception)}")