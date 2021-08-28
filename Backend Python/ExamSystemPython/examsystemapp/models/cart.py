"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class CartModel(BaseModel):
    def __init__(self, cartid=None,sessionid=None,customerid=None):
        self.cartid = cartid
        self.sessionid = sessionid
        self.customerid = customerid


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
