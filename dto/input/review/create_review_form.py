''' form to create a review '''
from flask_restx import Namespace, fields
from models.review import Review
from dto.input.validator import required, valid_string, optional, valid_int

class CreateReviewForm:
    ''' Form to create a review '''
    def __init__(self , json_review=None):
        if not json_review is None:
            self.client_id = required("client_id" , json_review)
            self.client_id = valid_string(self.client_id)

            self.pilot_id = optional("pilot_id" , json_review)
            self.pilot_id = valid_string(self.pilot_id)

            self.equipment_id = optional("equipment_id" , json_review)
            self.equipment_id = valid_string(self.equipment_id)

            self.rating = required("rating" , json_review)
            self.rating = valid_int(self.rating)

            self.comment = optional("comment" , json_review)
            self.comment = valid_string(self.comment)


    def to_domain(self):
        """Converts the form data to a Review domain model."""
        return Review(
            id=None,
            client_id=self.client_id,
            pilot_id=self.pilot_id,
            equipment_id=self.equipment_id,
            rating=self.rating,
            comment=self.comment,
            created_at=None
            )
    
    @staticmethod
    def api_model(name_enspace: Namespace):
        """Returns the API model for the review creation form."""
        return name_enspace.model("CreateReview", {
            "client_id": fields.String(required=True, description="ID of the client"),
            "pilot_id": fields.String(required=False, description="ID of the pilot"),
            "equipment_id": fields.String(required=False, description="ID of the equipment"),
            "rating": fields.Integer(required=True, description="Rating given in the review"),
            "comment": fields.String(required=False, description="Comment in the review")
            })