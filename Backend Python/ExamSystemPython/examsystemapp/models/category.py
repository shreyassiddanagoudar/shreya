"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class CategoryModel(BaseModel):
    def __init__(self, categoryid=None,name=None,description=None,imageurl=None):
        self.categoryid = categoryid
        self.name = name
        self.description = description
        self.imageurl = imageurl


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
