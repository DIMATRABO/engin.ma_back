# namespaces/user_namespace.py
from flask_restx import Namespace

user_ns = Namespace("user", description="User management operations")
