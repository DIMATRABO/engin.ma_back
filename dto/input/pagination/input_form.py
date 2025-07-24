''' InputForm class for handling pagination and sorting input data.'''
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


