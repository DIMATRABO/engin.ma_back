''' Repository for user roles management operations.'''

from typing import List
from models.user_role import UserRole
from entities.user_role_entity import UserRoleEntity


class Repository:
    '''Repository class for managing user data operations.'''
    def __init__(self ):
        '''Initialize the repository.'''
        pass

    def get_user_roles_by_user_id(self, session, user_id) -> List[UserRole]:
        '''Retrieve roles associated with a user by user ID.'''
        return session.query(UserRoleEntity).filter_by(user_id=user_id).all()
        