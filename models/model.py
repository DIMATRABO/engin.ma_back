from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
import json



@dataclass
class User:
    id: str = None
    username: str = None
    password: str = None
    full_name: str = None
    email: str = None
    birthdate: datetime = None
    address: str = None
    phone_number: str = None
    #user_status: UserStatus = None
    #bots: List[Bot] = field(default_factory=list)
    email_verified_at: str =None
    reset_password_otp: str = None 
    otp_expiration_date: datetime = None
    subscription_id: str = None


    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        self.birthdate = self.birthdate.isoformat() if self.birthdate else None
        Dstring = json.dumps(asdict(self))
        D = json.loads(Dstring)
        D["user_status"] = None if self.user_status is None else self.user_status.name
        D["password"] = None
        self.otp_expiration_date = self.otp_expiration_date.isoformat() if self.otp_expiration_date else None
        return D


@dataclass
class Admin:
    id: str = None
    username: str = None
    password: str = None
    full_name: str = None
    role: str = None

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        self.password = None
        return asdict(self)
