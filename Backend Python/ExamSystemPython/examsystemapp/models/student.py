"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class StudentModel(BaseModel):
    def __init__(self, studentid=None,collegeid=None,branchid=None,currentsemester=None,name=None,rollno=None,add1=None,add2=None,add3=None,cityid=None,stateid=None,pin=None,phonenum=None,email=None,profilepic=None,loginid=None,passwd=None):
        self.studentid = studentid
        self.collegeid = collegeid
        self.branchid = branchid
        self.currentsemester = currentsemester
        self.name = name
        self.rollno = rollno
        self.add1 = add1
        self.add2 = add2
        self.add3 = add3
        self.cityid = cityid
        self.stateid = stateid
        self.pin = pin
        self.phonenum = phonenum
        self.email = email
        self.profilepic = profilepic
        self.loginid = loginid
        self.passwd = passwd


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
