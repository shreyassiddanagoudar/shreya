"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class OrderModel(BaseModel):
    def __init__(self, orderid=None,customerid=None,orderdate=None,status=None,addressid=None,paymenttype=None,paymentstatus=None,totalprice=None):
        self.orderid = orderid
        self.customerid = customerid
        self.orderdate = orderdate
        self.status = status
        self.addressid = addressid
        self.paymenttype = paymenttype
        self.paymentstatus = paymentstatus
        self.totalprice = totalprice


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
