''' This module defines the UserRoleEntity class, which represents a user role in the database.'''
from sqlalchemy import Column, String
from entities.declarative_base_factory import Base
from models.user_role import UserRole

class UserRoleEntity(Base):
    ''' UserRoleEntity class representing a user role in the database. '''
    __tablename__ = "user_roles"

    user_id = Column("user_id", String, primary_key=True)
    role = Column("role", String, primary_key=True)

    def __repr__(self):
        return f"<UserRoleEntity(user_id={self.user_id}, role='{self.role}')>"
    
    def to_domain(self) -> UserRole:
        '''Convert entity to domain enum.'''
        return UserRole(self.role)