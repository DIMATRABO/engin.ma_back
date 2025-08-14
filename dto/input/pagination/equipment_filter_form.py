from flask_restx import Namespace, fields
from dto.input.validator import required, optional, valid_string, valid_int, valid_order
from exceptions.exception import InvalidRequestException

class EquipmentFilterForm:
    ''' Form for filtering and paginating equipment data. '''
    def __init__(self, json_input):
        # Pagination
        self.pageIndex = required('pageIndex', json_input)
        self.pageIndex = valid_int(self.pageIndex)
        if self.pageIndex < 1:
            raise InvalidRequestException("pageIndex must be >= 1")

        self.pageSize = required('pageSize', json_input)
        self.pageSize = valid_int(self.pageSize)

        # Sorting
        sort = required('sort', json_input)
        self.order = required('order', sort)
        self.order = valid_order(self.order)
        self.key = required('key', sort)
        self.key = valid_string(self.key)

        self.query = required('query',json_input)
        self.query = valid_string(self.query)

        # Filter data validation
        filter_data = optional('filterData', json_input)
        if filter_data is None:
            filter_data = {}

        if not isinstance(filter_data, dict):
            raise InvalidRequestException(self._filter_data_error_example())

        allowed_filter_keys = {
            'owner_id': str,
            'pilot_id': str,
            'city_ids': list,
            'fields_of_activity': list,
            'model_year_range': list,
            'construction_year_range': list,
            'date_of_customs_clearance_range': list,
            'price_range': list,
            'rating_range': list
        }

        for key in filter_data.keys():
            if key not in allowed_filter_keys:
                raise InvalidRequestException(self._filter_data_error_example())
            expected_type = allowed_filter_keys[key]
            if not isinstance(filter_data[key], expected_type):
                raise InvalidRequestException(self._filter_data_error_example())

        # Assign filters
        self.owner_id = filter_data.get('owner_id')
        self.pilot_id = filter_data.get('pilot_id')
        self.city_ids = filter_data.get('city_ids')
        self.fields_of_activity = filter_data.get('fields_of_activity')
        self.model_year_range = filter_data.get('model_year_range')
        self.construction_year_range = filter_data.get('construction_year_range')
        self.customs_clearance_range = filter_data.get('date_of_customs_clearance_range')
        self.price_range = filter_data.get('price_range')
        self.rating_range = filter_data.get('rating_range')

    @staticmethod
    def _filter_data_error_example():
        return (
            "Invalid 'filterData' structure. Example: \n"
            "{\n"
            "  'filterData': {\n"
            "    'owner_id': 'uuid',\n"
            "    'pilot_id': 'uuid',\n"
            "    'city_ids': ['city1', 'city2'],\n"
            "    'fields_of_activity': ['TRANSPORT', 'CHANTIER'],\n"
            "    'model_year_range': [2010, 2020],\n"
            "    'construction_year_range': [2005, 2022],\n"
            "    'date_of_customs_clearance_range': [2015, 2020],\n"
            "    'price_range': [100, 500],\n"
            "    'rating_range': [3.0, 5.0]\n"
            "  }\n"
            "}"
        )

    @staticmethod
    def api_model(namespace: Namespace):
        ''' Returns the API model for EquipmentFilterForm. '''
        return namespace.model('EquipmentFilterForm', {
            'pageIndex': fields.Integer(required=True, description='Page index'),
            'pageSize': fields.Integer(required=True, description='Items per page'),
            'sort': fields.Nested(namespace.model('Sort', {
                'order': fields.String(required=True, description='asc or desc'),
                'key': fields.String(required=True, description='Sort key')
            })),
            'query': fields.String(required=False, description='Search query'),
            'filterData': fields.Raw(description='Filter object as described in the API docs')
        })
