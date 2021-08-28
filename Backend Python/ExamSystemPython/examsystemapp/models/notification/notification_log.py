"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class NotificationLogModel(BaseModel):
    def __init__(self, log_id=None,notification_id=None,sent_on=None,title=None,description=None,image=None,payload=None,url=None,object_id=None,recipients=None):
        self.log_id = log_id
        self.notification_id = notification_id
        self.sent_on = sent_on
        self.title = title
        self.description = description
        self.image = image
        self.payload = payload
        self.url = url
        self.object_id = object_id
        self.recipients = recipients


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
