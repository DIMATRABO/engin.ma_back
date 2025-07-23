''' This module defines the UserRoleEntity class, which represents a user role in the database.'''
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserRoleEntity(Base):
    ''' UserRoleEntity class representing a user role in the database. '''
    __tablename__ = "user_roles"

    user_id = Column("user_id", String, primary_key=True)
    role = Column("role", String, primary_key=True)

    def __repr__(self):
        return f"<UserRoleEntity(user_id={self.user_id}, role='{self.role}')>"
