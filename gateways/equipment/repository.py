''' Repository for equipment management operations.'''
import uuid
from datetime import datetime
from sqlalchemy import desc
from models.equipment import Equipment
from entities.equipment_entity import EquipmentEntity
from gateways.log import Log
from exceptions.exception import NotFoundException
from exceptions.exception import InvalidRequestException
from dto.input.pagination.equipment_filter_form import EquipmentFilterForm
from dto.output.equipment.equipments_paginated import EquipmentsPaginated
from dto.output.equipment.equipment_response_form import EquipmentResponseForm

logger = Log()
class Repository:
    '''Repository class for managing equipment data operations.'''
    def __init__(self ):
        '''Initialize the repository.'''
        logger.debug("Repository initialized")

    def save(self, session , equipment:Equipment)-> Equipment:
        '''Save a equipment to the database.'''
        equipment_entity = EquipmentEntity()
        equipment_entity.from_domain(model=equipment)
        equipment_entity.id=str(uuid.uuid4())
        equipment_entity.created_at = datetime.now()
        session.add(equipment_entity)
        return equipment_entity.to_domain()
    
    def delete(self, session , equipment_id:str) -> None:
        '''Delete a equipment by ID from the database.'''
        equipment = session.query(EquipmentEntity).filter(EquipmentEntity.id == equipment_id).first()
        if equipment is None:
            raise NotFoundException(f"Equipment with id {equipment_id} not found.")
        session.delete(equipment)
          
    def get_equipment_by_id(self, session , equipment_id:str) -> Equipment:
        '''Retrieve a equipment by equipment_id from the database.'''
        equipment = session.query(EquipmentEntity).filter(EquipmentEntity.id == equipment_id).first()
        if equipment is None:
            raise NotFoundException(f"Equipment with id {equipment_id} not found.")
        return equipment.to_domain()

    def get_all_paginated(self, session, input_form: EquipmentFilterForm) -> EquipmentsPaginated:
        '''Retrieve all equipments with pagination, filtering, and sorting.'''
        allowed_sort_keys = [
            'model_year', 'construction_year', 'date_of_customs_clearance',
            'title', 'price_per_day', 'rating_average', 'created_at'
        ]

        query = session.query(EquipmentEntity)

        # Apply filters from filterData
        if input_form.owner_id:
            query = query.filter(EquipmentEntity.owner_id == input_form.owner_id)
        if input_form.pilot_id:
            query = query.filter(EquipmentEntity.pilot_id == input_form.pilot_id)
        if input_form.city_ids:
            query = query.filter(EquipmentEntity.city_id.in_(input_form.city_ids))
        if input_form.fields_of_activity:
            query = query.filter(EquipmentEntity.fields_of_activity.in_(input_form.fields_of_activity))
        if input_form.category_ids:
            query = query.filter(EquipmentEntity.category_id.in_(input_form.category_ids))

        if input_form.model_year_range:
            query = query.filter(
                EquipmentEntity.model_year >= input_form.model_year_range[0],
                EquipmentEntity.model_year <= input_form.model_year_range[1]
            )
        if input_form.construction_year_range:
            query = query.filter(
                EquipmentEntity.construction_year >= input_form.construction_year_range[0],
                EquipmentEntity.construction_year <= input_form.construction_year_range[1]
            )
        if input_form.customs_clearance_range:
            query = query.filter(
                EquipmentEntity.date_of_customs_clearance >= input_form.customs_clearance_range[0],
                EquipmentEntity.date_of_customs_clearance <= input_form.customs_clearance_range[1]
            )
        if input_form.price_range:
            query = query.filter(
                EquipmentEntity.price_per_day >= input_form.price_range[0],
                EquipmentEntity.price_per_day <= input_form.price_range[1]
            )
        if input_form.rating_range:
            query = query.filter(
                EquipmentEntity.rating_average >= input_form.rating_range[0],
                EquipmentEntity.rating_average <= input_form.rating_range[1]
            )

        # Sorting
        if input_form.key and input_form.order:
            sort_key = input_form.key.lower()
            if sort_key in allowed_sort_keys:
                sort_column = getattr(EquipmentEntity, sort_key)
                query = query.order_by(desc(sort_column) if input_form.order.lower() == 'desc' else sort_column)
            else:
                raise InvalidRequestException(f"Invalid sort key: {sort_key}")
        else:
            query = query.order_by(desc(EquipmentEntity.created_at))

        # Pagination
        total_records = query.count()
        starting_index = (input_form.pageIndex - 1) * input_form.pageSize
        equipments = query.offset(starting_index).limit(input_form.pageSize).all()

        return EquipmentsPaginated(
            total=total_records,
            data=[EquipmentResponseForm(equipment=equipment.to_domain()) for equipment in equipments]
        )

    def update(self, session, equipment: Equipment):
        '''Update an existing equipment in the database.'''
        entity = session.query(EquipmentEntity).filter_by(id=equipment.id).first()
        if not entity:
            raise Exception("Equipment not found")

        # Update only non-null fields
        entity.update_non_null_fields_from_model(model=equipment)

        session.add(entity)
        return entity.to_domain()
