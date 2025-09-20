''' Repository for user management operations.'''
import uuid
from typing import List
from entities.review_entity import ReviewEntity
from models.review import Review
from gateways.log import Log


logger = Log()
class Repository:
    '''Repository class for managing user data operations.'''
    def __init__(self ):
        '''Initialize the repository.'''
        logger.debug("Repository initialized")

    
    def save(self, session , review: Review) -> Review:
        '''Save a review entity to the database.'''
        logger.debug(f"Saving review: {review}")
        review_entity = ReviewEntity()
        review_entity.from_domain(model=review)
        review_entity.id = str(uuid.uuid4())
        session.add(review_entity)
        logger.debug("Review saved successfully")
        return review_entity.to_domain()
    
    def get_all(self, session)->List[Review]:
        '''Retrieve all review entities from the database.'''
        reviews = session.query(ReviewEntity).all()
        return [review.to_domain() for review in reviews]
    
    def get_by_id(self, session, id_: str) -> Review:
        '''Retrieve a review entity by its ID from the database.'''
        logger.debug(f"Retrieving review with ID: {id_}")
        review_entity = session.query(ReviewEntity).filter_by(id=id_).first()
        if not review_entity:
            logger.error(f"Review with ID {id_} not found")
            return None
        return review_entity.to_domain()
    
    def get_by_client_id(self, session, client_id: str) -> List[Review]:
        '''Retrieve review entities by client ID from the database.'''
        logger.debug(f"Retrieving reviews for user ID: {client_id}")
        review_entities = session.query(ReviewEntity).filter_by(client_id=client_id).all()
        if not review_entities:
            logger.error(f"No reviews found for user ID {client_id}")
            return []
        return [review.to_domain() for review in review_entities]
    
    def get_by_pilot_id(self, session, pilot_id: str) -> List[Review]:
        '''Retrieve review entities by pilot ID from the database.'''
        logger.debug(f"Retrieving reviews for pilot ID: {pilot_id}")
        review_entities = session.query(ReviewEntity).filter_by(pilot_id=pilot_id).all()
        if not review_entities:
            logger.error(f"No reviews found for pilot ID {pilot_id}")
            return []
        return [review.to_domain() for review in review_entities]
    
    def get_by_equipment_id(self, session, equipment_id: str) -> List[Review]:
        '''Retrieve review entities by equipment ID from the database.'''
        logger.debug(f"Retrieving reviews for equipment ID: {equipment_id}")
        review_entities = session.query(ReviewEntity).filter_by(equipment_id=equipment_id).all()
        if not review_entities:
            logger.error(f"No reviews found for equipment ID {equipment_id}")
            return []
        return [review.to_domain() for review in review_entities]
    