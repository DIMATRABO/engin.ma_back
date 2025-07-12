from sqlalchemy import Column, String , DateTime
from sqlalchemy.orm import declarative_base
from models.model import *

from gateways.log import Log
Base = declarative_base()


logger = Log()


class UserEntity(Base):
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
    subscription_id = Column("subscription_id",String)
    creation_date = Column("creation_date", DateTime) 


    def __init__(self,id=None , username=None , password=None, full_name =None,email = None,  birthdate =None,address=None, phone_number=None, user_status=None):
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
        return "<UserEntity(id='%s', full_name='%s')>" % (
            self.id,
            self.full_name
        )
        
    def from_domain(self,model : User):
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
        self.subscription_id = model.subscription_id


    def update_non_null_fields_from_model(self, model: User):
        attributes = [attr for attr in dir(model) if not callable(getattr(model, attr)) and not attr.startswith("__")]
        for attr in attributes:
            value = getattr(model, attr)
            if value is not None:
                setattr(self, attr, value)
                
 
    def to_domain(self):
        return User(
            id=self.id,
            username =self.username,
            password=self.password,
            full_name = self.full_name,
            email=self.email,
            birthdate = self.birthdate ,
            address= self.address,
            #user_status= UserStatus(self.user_status),
            email_verified_at=self.email_verified_at,
            reset_password_otp=self.reset_password_otp,
            otp_expiration_date=self.otp_expiration_date,
            subscription_id=self.subscription_id
            )
       
    

class AdminEntity(Base):
    __tablename__ = "admins"
    id = Column("id",String , primary_key=True)
    username= Column("username",String, unique=True )
    password=Column("password",String)
    full_name= Column("full_name",String)
    role=Column("role",String)
   

    def __init__(self,id=None , username=None , password=None, full_name =None, role =None):
        self.id=id
        self.username=username
        self.password=password
        self.full_name=full_name
        self.role=role

        
    def __repr__(self):
        return "<UserEntity(id='%s', full_name='%s')>" % (
            self.id,
            self.full_name
        )
        
    def from_domain(self,model : Admin):
        self.id=model.id
        self.username=model.username
        self.password=model.password
        self.full_name=model.full_name
        self.role=model.role
 
    def to_domain(self):
        return Admin(
            id=self.id,
            username =self.username,
            password=self.password,
            full_name = self.full_name,
            role = self.role
            )
    