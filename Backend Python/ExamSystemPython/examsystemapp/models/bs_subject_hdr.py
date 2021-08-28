"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class BSSubjectHdrModel(BaseModel):
    def __init__(self, branchsubjectid=None,branchid=None,semesterid=None):
        self.branchsubjectid = branchsubjectid
        self.branchid = branchid
        self.semesterid = semesterid


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
