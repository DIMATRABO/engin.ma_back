class InvalidRequestException(Exception):
    def __init__(self, message="Invalid request"):
        super().__init__(message)

class UnauthorizedException(Exception):
    def __init__(self, message="Unauthorized"):
        super().__init__(message)

class NotFoundException(Exception):
    def __init__(self, message="Not found"):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message="Input validation failed"):
        super().__init__(message)

class BadGatewayException(Exception):
    def __init__(self, message="Bad Gateway Exception"):
        super().__init__(message)

class UsernameAlreadyExists(Exception):
    def __init__(self, message="username already exists"):
        super().__init__(message)

class EmailAlreadyExists(Exception):
    def __init__(self, message="Email already exists"):
        super().__init__(message)

class EmailNotVerifiedException(Exception):
    def __init__(self, message="Email not verified"):
        super().__init__(message)

class UserBlockedException(Exception):
    def __init__(self, message="User blocked"):
        super().__init__(message)

class VariableTypeError(Exception):
    """Exception raised in variable type error."""
    def __init__(self, message="Variable type error"):
        super().__init__(message)

class InvalidJsonException(Exception):
    """Exception raised in invalid json error."""
    def __init__(self, message="Invalid json"):
        super().__init__(message)

