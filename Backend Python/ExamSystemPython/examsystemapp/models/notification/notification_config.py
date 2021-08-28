"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class NotificationConfigModel(BaseModel):
    OBJECT_TYPE = 'NOTIFICATION_CONFIG'

    def __init__(self,
                 notification_id=None,
                 created_on=None,
                 created_by=None,
                 object_type=None,
                 action=None,
                 context=None,
                 is_active=None,
                 notification_type=None,
                 title=None,
                 title_config=None,
                 description=None,
                 description_config=None,
                 image_config=None, notification_default_recipients=None, notification_recipient_group=None):
        self.notification_id = notification_id
        self.created_on = created_on
        self.created_by = created_by
        self.object_type = object_type
        self.action = action
        self.context = context
        self.is_active = is_active
        self.notification_type = notification_type
        self.title = title
        self.title_config = title_config
        self.description = description
        self.description_config = description_config
        self.image_config = image_config

        self.notification_default_recipients = notification_default_recipients
        self.notification_recipient_group = notification_recipient_group

    def get_id(self):
        pass

    def is_valid(self, type, event_type=None):
        return Validation()
