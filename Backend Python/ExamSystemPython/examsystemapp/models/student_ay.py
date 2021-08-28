"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class StudentAYModel(BaseModel):
    def __init__(self, studentayid=None,studentid=None,ayid=None,semesterid=None,startdate=None,enddate=None):
        self.studentayid = studentayid
        self.studentid = studentid
        self.ayid = ayid
        self.semesterid = semesterid
        self.startdate = startdate
        self.enddate = enddate


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
