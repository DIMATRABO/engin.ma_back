''' Repository for user management operations.'''
import uuid
from datetime import datetime
from sqlalchemy import  exc, or_, func
from models.user import User
from models.user_status import UserStatus
from entities.user_entity import UserEntity
from gateways.log import Log

from exceptions.exception import NotFoundException

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
    