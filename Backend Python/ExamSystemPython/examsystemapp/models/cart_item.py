"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class CartItemModel(BaseModel):
    def __init__(self, cartitemid=None,cartid=None,date=None,productid=None,qty=None,price=None):
        self.cartitemid = cartitemid
        self.cartid = cartid
        self.date = date
        self.productid = productid
        self.qty = qty
        self.price = price


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
