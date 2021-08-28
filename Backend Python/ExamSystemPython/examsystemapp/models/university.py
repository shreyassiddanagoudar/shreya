"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class UniversityModel(BaseModel):
    def __init__(self, universityid=None,name=None,code=None,addr1=None,addr2=None,addr3=None,cityid=None,stateid=None,pincode=None,phone=None,email=None,logo=None,url=None):
        self.universityid = universityid
        self.name = name
        self.code = code
        self.addr1 = addr1
        self.addr2 = addr2
        self.addr3 = addr3
        self.cityid = cityid
        self.stateid = stateid
        self.pincode = pincode
        self.phone = phone
        self.email = email
        self.logo = logo
        self.url = url


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
