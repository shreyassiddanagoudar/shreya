"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class SubCategoryModel(BaseModel):
    def __init__(self, subcategoryid=None,name=None,parentcategoryid=None,parentsubcategoryid=None,description=None,imageurl=None):
        self.subcategoryid = subcategoryid
        self.name = name
        self.parentcategoryid = parentcategoryid
        self.parentsubcategoryid = parentsubcategoryid
        self.description = description
        self.imageurl = imageurl


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
