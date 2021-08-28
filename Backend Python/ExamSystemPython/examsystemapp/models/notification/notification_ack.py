"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class NotificationACKModel(BaseModel):
    def __init__(self, log_id=None,user_id=None,ack_on=None):
        self.log_id = log_id
        self.user_id = user_id
        self.ack_on = ack_on


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
