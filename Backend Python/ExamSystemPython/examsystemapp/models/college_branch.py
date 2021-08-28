"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class CollegeBranchModel(BaseModel):
    def __init__(self, collegebranchid=None,branchid=None,collegeid=None,phonenum=None,email=None,url=None):
        self.collegebranchid = collegebranchid
        self.branchid = branchid
        self.collegeid = collegeid
        self.phonenum = phonenum
        self.email = email
        self.url = url


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
