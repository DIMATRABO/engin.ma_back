from flask_restx import fields
from controllers.user.user_namespace import user_ns

delete_model = user_ns.model("DeleteUser", {
    "id": fields.String(required=True)
})