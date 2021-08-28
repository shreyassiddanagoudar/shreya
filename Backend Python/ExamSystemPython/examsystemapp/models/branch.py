"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class BranchModel(BaseModel):
    def __init__(self, branchid=None,name=None,code=None):
        self.branchid = branchid
        self.name = name
        self.code = code


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
