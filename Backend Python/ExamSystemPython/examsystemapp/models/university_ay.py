"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class UniversityAYModel(BaseModel):
    def __init__(self, ayid=None,universityid=None,startdate=None,enddate=None):
        self.ayid = ayid
        self.universityid = universityid
        self.startdate = startdate
        self.enddate = enddate


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
