"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""


class NotificationPayload:

    def __init__(self, object_type=None, action=None, title=None, description=None, notification_id=None, log_id=None,
                 object_id=None, url=None,
                 data_object=None):
        self.object_type = object_type
        self.action = action
        self.title = title
        self.description = description
        self.notification_id = notification_id
        self.log_id = log_id
        self.object_id = object_id
        self.url = url
        self.data_object = data_object
