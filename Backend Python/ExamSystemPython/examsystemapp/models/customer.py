"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class CustomerModel(BaseModel):
    def __init__(self, customerid=None,email=None,phone=None,name=None,password=None):
        self.customerid = customerid
        self.email = email
        self.phone = phone
        self.name = name
        self.password = password


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
