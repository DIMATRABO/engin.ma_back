''' Repository for user management operations.'''
import uuid
from typing import List
from datetime import datetime
from sqlalchemy import  func , exc, desc , or_
from models.user import User
from models.user_status import UserStatus
from models.user_role import UserRole
from entities.user_entity import UserEntity
from entities.user_role_entity import UserRoleEntity
from gateways.log import Log
from exceptions.exception import NotFoundException
from exceptions.exception import InvalidRequestException
from dto.input.pagination.input_form import InputForm
from dto.output.user.user_response_form import UserResponseForm
from dto.output.user.users_paginated import UsersPaginated
from dto.output.user.user_simple import UserSimple

logger = Log()
class Repository:
    '''Repository class for managing user data operations.'''
    def __init__(self ):
        '''Initialize the repository.'''
        logger.debug("Repository initialized")

    def save(self, session , user:User)-> User:
        '''Save a user to the database.'''
        user_entity = UserEntity()
        user_entity.from_domain(model=user)
        user_entity.id=str(uuid.uuid4())
        user_entity.created_at = datetime.now()
        session.add(user_entity)
        return user_entity.to_domain()
    
    def get_user_by_id(self, session , id_:str) -> User:
        '''Retrieve a user by id from the database.'''
        user = session.query(UserEntity).filter(UserEntity.id == id_).first()
        if user is None:
            return None
        return user.to_domain()
          
    def get_user_by_username(self, session , username:str) -> User:
        '''Retrieve a user by username from the database.'''
        user = session.query(UserEntity).filter(UserEntity.username == username).first()
        if user is None:
            return None
        return user.to_domain()
    
    def get_user_by_email(self, session , email:str) -> User:
        '''Retrieve a user by email from the database.'''
        user = session.query(UserEntity).filter(UserEntity.email == email).first()
        if user is None:
            return None
        return user.to_domain()
    
    def get_user_by_username_or_email(self, session , username_or_email:str) -> User:
        '''Retrieve a user by username or email from the database.'''
        username_or_email_lower = username_or_email.lower()
        user = session.query(UserEntity).filter(
            or_(UserEntity.username == username_or_email,
                func.lower(UserEntity.email) == username_or_email_lower)
            ).first()
        if user is None:
            return None  
        return user.to_domain()
    
    def get_all_simple_by_role(self, session, role: UserRole) -> List[UserSimple]:
        '''Retrieve all users with a specific role in a simplified format.'''
        users = (
            session.query(UserEntity)
            .join(UserRoleEntity, UserEntity.id == UserRoleEntity.user_id)
            .filter(UserRoleEntity.role == role.value)
            .all()
        )
        return [UserSimple(user=user.to_domain()) for user in users] if users else []
    
        
    def delete(self, session , id:str):
        '''Delete a user by ID from the database.'''
        existing_user_entity = session.query(UserEntity).filter(UserEntity.id == id).first()

        # Check if the user exists
        if existing_user_entity:
            existing_user_entity.user_status = UserStatus.DELETED.value
            try:
                session.commit()
            except exc.SQLAlchemyError as e:
                logger.log(e)
                session.rollback()
                raise Exception("User not deleted")
            return {"msg":"deleted"}
        raise NotFoundException("User not found")
    

    def get_roles_by_user_id(self, session, user_id: str) -> List[UserRole]:
        '''Retrieve all roles for a user by user_id.'''
        roles = (
            session.query(UserRoleEntity.role)
            .filter(UserRoleEntity.user_id == user_id)
            .all()
        )
        return [UserRole(role[0]) for role in roles] if roles else []
    
    def set_roles_by_user_id(self, session, user:User, new_roles: List[UserRole]) ->User:
        '''Set roles for a user by user_id.'''
        # Delete existing roles
        session.query(UserRoleEntity).filter(UserRoleEntity.user_id == user.id).delete()

        # Add new roles
        for role in new_roles:
            user_role_entity = UserRoleEntity(user_id=user.id, role=role.value)
            session.add(user_role_entity)
        user.role = new_roles
        return user
      
    
    def get_all_paginated(self, session, input_form: InputForm) -> UsersPaginated:
        '''Retrieve all users with pagination, filtering, and sorting.'''
        allowed_sort_keys = ['username', 'full_name', 'email', 'created_at']

        query = session.query(UserEntity)

        # Filter by status
        if input_form.status:
            query = query.filter(UserEntity.user_status == input_form.status.upper())

        # Filter by search query
        if input_form.query:
            search_criteria = or_(
                UserEntity.username.ilike(f'%{input_form.query}%'),
                UserEntity.full_name.ilike(f'%{input_form.query}%'),
                UserEntity.email.ilike(f'%{input_form.query}%')
            )
            query = query.filter(search_criteria)

        # Sorting
        if input_form.key and input_form.order:
            sort_key = input_form.key.lower()
            if sort_key in allowed_sort_keys:
                sort_column = getattr(UserEntity, sort_key, None)
                if sort_column is None:
                    raise InvalidRequestException(f"Invalid sort key: {sort_key}")
                query = query.order_by(desc(sort_column) if input_form.order.lower() == 'desc' else sort_column)
            else:
                raise InvalidRequestException(f"Invalid sort key: {sort_key}")
        else:
            # Default sorting
            query = query.order_by(desc(UserEntity.creation_date))

        # Pagination
        total_records = query.count()
        starting_index = (input_form.pageIndex - 1) * input_form.pageSize
        users = query.offset(starting_index).limit(input_form.pageSize).all()

        return UsersPaginated(
            total=total_records,
            data=[UserResponseForm(user=user.to_domain()) for user in users]
        )

        
    def change_status(self, session, user: User) -> User:
        '''Change the status of a user.'''
        user_entity = session.query(UserEntity).filter(UserEntity.id == user.id).first()
        if not user_entity:
            raise NotFoundException("User not found")

        # Update the status
        user_entity.user_status = user.user_status.value
        return UserResponseForm(user_entity.to_domain())