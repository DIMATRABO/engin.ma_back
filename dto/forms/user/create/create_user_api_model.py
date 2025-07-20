



user_response_model = user_ns.model("UserResponse", {
    "id": fields.String(),
    "username": fields.String(),
    "email": fields.String(),
    "full_name": fields.String()
})