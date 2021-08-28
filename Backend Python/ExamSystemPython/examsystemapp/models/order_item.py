"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class OrderItemModel(BaseModel):
    def __init__(self, orderitemid=None,orderid=None,productid=None,qty=None,price=None,status=None):
        self.orderitemid = orderitemid
        self.orderid = orderid
        self.productid = productid
        self.qty = qty
        self.price = price
        self.status = status


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
