from flask_restx import Namespace, fields
from dto.input.validator import required, optional, valid_string, valid_int, valid_order
from exceptions.exception import InvalidRequestException

class BookingFilterForm:
    ''' Form for filtering and paginating booking data. '''
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
            'client_id': str,
            'equipment_id': str,
            'pilot_id': str,
            'start_date_range': list,
            'end_date_range': list,
            'number_of_days_range': list,
            'unit_price_range': list,
            'total_price_range': list,
            'status': str
        }

        for key in filter_data.keys():
            if key not in allowed_filter_keys:
                raise InvalidRequestException(self._filter_data_error_example())
            expected_type = allowed_filter_keys[key]
            if not isinstance(filter_data[key], expected_type):
                raise InvalidRequestException(self._filter_data_error_example())

        # Assign filters
        self.client_id = filter_data.get('client_id')
        self.equipment_id = filter_data.get('equipment_id')
        self.pilot_id = filter_data.get('pilot_id')
        self.start_date_range = filter_data.get('start_date_range')
        self.end_date_range = filter_data.get('end_date_range')
        self.number_of_days_range = filter_data.get('number_of_days_range')
        self.unit_price_range = filter_data.get('unit_price_range')
        self.total_price_range = filter_data.get('total_price_range')
        self.status = filter_data.get('status')

    @staticmethod
    def _filter_data_error_example():
        return (
            "Invalid 'filterData' structure. Example: \n"
            "{\n"
            "  'client_id': 'string',\n"
            "  'equipment_id': 'string',\n"
            "  'pilot_id': 'string',\n"
            "  'start_date_range': ['2023-01-01', '2023-12-31'],\n"
            "  'end_date_range': ['2023-01-01', '2023-12-31'],\n"
            "  'number_of_days_range': [1, 10],\n"
            "  'unit_price_range': [100.00, 500.00],\n"
            "  'total_price_range': [500.00, 5000.00],\n"
            "  'status': 'CONFIRMED'\n"
            "}"
        )

    @staticmethod
    def api_model(namespace: Namespace):
        ''' Returns the API model for BookingFilterForm. '''
        return namespace.model('BookingFilterForm', {
            'pageIndex': fields.Integer(required=True, description='Page index'),
            'pageSize': fields.Integer(required=True, description='Items per page'),
            'sort': fields.Nested(namespace.model('Sort', {
                'order': fields.String(required=True, description='asc or desc'),
                'key': fields.String(required=True, description='Sort key')
            })),
            'query': fields.String(required=False, description='Search query'),
            'filterData': fields.Raw(description='Filter object as described in the API docs')
        })