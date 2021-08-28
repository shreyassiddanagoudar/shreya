"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class StaffModel(BaseModel):
    def __init__(self, staffid=None,ownerid=None,role=None,name=None,staffnum=None,addr1=None,addr2=None,cityid=None,stateid=None,pin=None,phonenum=None,email=None,profilepic=None,loginid=None,password=None):
        self.staffid = staffid
        self.ownerid = ownerid
        self.role = role
        self.name = name
        self.staffnum = staffnum
        self.addr1 = addr1
        self.addr2 = addr2
        self.cityid = cityid
        self.stateid = stateid
        self.pin = pin
        self.phonenum = phonenum
        self.email = email
        self.profilepic = profilepic
        self.loginid = loginid
        self.password = password


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
