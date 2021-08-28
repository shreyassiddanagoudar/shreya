"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class NotificationDefaultRecipientsModel(BaseModel):
    OBJECT_TYPE = 'NOTIFICATION_DEFAULT_RECIPIENTS'

    def __init__(self,
                 notification_id=None,
                 procedure_name=None,
                 procedure_config=None):
        self.notification_id = notification_id
        self.procedure_name = procedure_name
        self.procedure_config = procedure_config

    def get_id(self):
        pass

    def is_valid(self, type, event_type=None):
        return Validation()
