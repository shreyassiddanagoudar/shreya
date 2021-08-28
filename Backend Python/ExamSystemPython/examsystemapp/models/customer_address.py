"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class CustomerAddressModel(BaseModel):
    def __init__(self, customeraddressid=None,customerid=None,add1=None,add2=None,add3=None,cityid=None,stateid=None,pincode=None):
        self.customeraddressid = customeraddressid
        self.customerid = customerid
        self.add1 = add1
        self.add2 = add2
        self.add3 = add3
        self.cityid = cityid
        self.stateid = stateid
        self.pincode = pincode


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
