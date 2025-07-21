'''This module defines the UserEntity  which represent the user entities in the database.'''
from sqlalchemy import Column, String
from entities.declarative_base_factory import Base
from models.user import User
from models.user_status import UserStatus


class UserEntity(Base):
    '''UserEntity class representing a user in the database.'''
    __tablename__ = "users"
    id = Column("id",String , primary_key=True)
    username= Column("username",String, unique=True )
    password=Column("password",String)
    full_name= Column("full_name",String)
    email=Column("email",String, unique=True )
    birthdate=Column("birthdate",DateTime)
    address=Column("address",String)
    phone_number = Column("phone_number",String)
    user_status=Column("user_status",String)
    email_verified_at = Column("email_verified_at",String)
    reset_password_otp = Column("reset_password_otp",String)
    otp_expiration_date = Column("otp_expiration_date",DateTime)
    created_at = Column("created_at", DateTime)


    def __init__(self,id=None , username=None , password=None, full_name =None,email = None,  birthdate =None,address=None, phone_number=None, user_status=None):
        '''Initialize a UserEntity instance.'''
        self.id=id
        self.username=username
        self.password=password
        self.full_name=full_name
        self.email = email
        self.birthdate=birthdate
        self.address=address
        self.phone_number=phone_number
        self.user_status=user_status

    def __repr__(self):
        '''Return a string representation of the UserEntity instance.'''
        return "<UserEntity(id='%s', full_name='%s')>" % (
            self.id,
            self.full_name
        )
    
    def from_domain(self,model : User):
        '''Populate the UserEntity instance from a User domain model.'''
        self.id=model.id
        self.username=model.username
        self.password=model.password
        self.full_name=model.full_name
        self.email= model.email
        self.birthdate=model.birthdate
        self.phone_number=model.phone_number
        self.address=model.address
        self.user_status=model.user_status.value
        self.email_verified_at=model.email_verified_at
        self.reset_password_otp=model.reset_password_otp
        self.otp_expiration_date=model.otp_expiration_date
        self.created_at = model.created_at


    def update_non_null_fields_from_model(self, model: User):
        '''Update non-null fields of the UserEntity instance from a User domain model.'''
        attributes = [attr for attr in dir(model) if not callable(getattr(model, attr)) and not attr.startswith("__")]
        for attr in attributes:
            value = getattr(model, attr)
            if value is not None:
                setattr(self, attr, value)

    def to_domain(self):
        '''Convert the UserEntity instance to a User domain model.'''
        return User(
            id=self.id,
            username =self.username,
            password=self.password,
            full_name = self.full_name,
            email=self.email,
            birthdate = self.birthdate,
            address= self.address,
            phone_number=self.phone_number,
            user_status= UserStatus(self.user_status),
            email_verified_at=self.email_verified_at,
            reset_password_otp=self.reset_password_otp,
            otp_expiration_date=self.otp_expiration_date,
            created_at=self.created_at
            )
