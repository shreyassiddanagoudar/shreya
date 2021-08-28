"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class NotificationRecipientGroupModel(BaseModel):
    OBJECT_TYPE = 'NOTIFICATION_RECIPIENT_GROUP'

    def __init__(self,
                 notification_id=None,
                 recipient_id=None,
                 type=None):
        self.notification_id = notification_id
        self.recipient_id = recipient_id
        self.type = type

    def get_id(self):
        pass

    def is_valid(self, type, event_type=None):
        return Validation()
