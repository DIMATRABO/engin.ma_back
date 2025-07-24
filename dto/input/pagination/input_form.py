''' InputForm class for handling pagination and sorting input data.'''
from flask_restx import Namespace, fields
from dto.input.validator import *


class InputForm:
    ''' InputForm class for handling pagination and sorting input data.'''
    pageIndex: int = None
    pageSize: int = None
    order: str = None
    key:str = None
    query:str = None 
    status:str = None


    def __init__(self , json_input):
        
        self.pageIndex = required('pageIndex', json_input)
        self.pageIndex = valid_int(self.pageIndex)

        self.pageSize = required('pageSize', json_input)
        self.pageSize = valid_int(self.pageSize)


        sort = required('sort', json_input)
        self.order = required('order', sort)
        self.order = valid_order(self.order)

        self.key = required('key', sort)
        self.key = valid_string(self.key)


        self.query = required('query',json_input)
        self.query = valid_string(self.query)

        filter_data = optional('filterData', json_input)
        if not filter_data is None:
            self.status = required('status', filter_data)
            self.status = valid_string(self.status)

    @staticmethod
    def api_model(namespace: Namespace):
        ''' Returns the API model for InputForm.'''
        return namespace.model('InputForm', {
                'pageIndex': fields.Integer(required=True, description='Page index for pagination'),
                'pageSize': fields.Integer(required=True, description='Number of items per page'),
                'sort': fields.Nested(namespace.model('Sort', {
                    'order': fields.String(required=True, description='Sort order (asc/desc)'),
                    'key': fields.String(required=True, description='Field to sort by')
                })),
                'query': fields.String(required=False, description='Search query'),
                'filterData': fields.Nested(namespace.model('FilterData', {
                    'status': fields.String(required=False, description='User status filter')
                }), required=False)
            })


