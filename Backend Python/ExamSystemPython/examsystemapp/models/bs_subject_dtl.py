"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class BSSubjectDtlModel(BaseModel):
    def __init__(self, bssubjectdtlid=None,bssid=None,name=None,subjectid=None):
        self.bssubjectdtlid = bssubjectdtlid
        self.bssid = bssid
        self.name = name
        self.subjectid = subjectid


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
