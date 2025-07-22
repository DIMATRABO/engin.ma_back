''' Utility functions for authentication and JWT claims. '''
from models.user import User


def create_additional_claims_from_user(user:User):
        '''Create additional claims for JWT from user object.'''
        additional_claims ={
                "name": user.full_name,
                "sub": user.username,
                "authority": "user",
                "email": user.email,
                "userId": user.id
                }
        return additional_claims


def refresh_additional_claims(old_claims):
        '''Refresh additional claims from old JWT claims.'''
        additional_claims = {}
        role = old_claims['authority']
        if role == "user":
                additional_claims = {
                        "name": old_claims['name'],
                        "sub": old_claims['sub'],
                        "authority": old_claims['authority'],
                        "email": old_claims['email'],
                        "userId": old_claims['userId']
                }

        elif role == "admin":
                additional_claims = {
                        "name": old_claims['name'],
                        "sub": old_claims['sub'],
                        "authority": old_claims['authority'],
                        "email": old_claims['email'],
                        "userId": old_claims['userId']
                }
        
        return additional_claims