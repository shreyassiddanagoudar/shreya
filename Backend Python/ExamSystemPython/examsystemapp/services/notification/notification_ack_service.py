"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from examsystemapp.repository.notification.notification_ack_repository import NotificationACKRepo
from examsystemapp.services.base_service import BaseService
from examsystemapp.utils.helpers.request_helper import ParamsObject


class NotificationACKService(BaseService):

    def __init__(self, ext_params={}, is_transaction_owner=True):
        BaseService.__init__(self, ext_params, is_transaction_owner)

    def pre_add(self, object):
        pass

    def add_data(self, object):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.add_data(object)

    def post_add(self, object):
        return object

    def pre_update(self, object):
        pass

    def update_data(self, object):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.update_data(object)

    def post_update(self, object):
        return object

    def pre_delete(self, object):
        pass

    def delete_data(self, object):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.delete_data(object)

    def post_delete(self, object):
        return object

    def pre_get(self, params):
        pass

    def get_data(self, params):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.get_data(params)

    def post_get(self, object):
        return object

    def pre_get_list(self, params):
        pass

    def get_data_list(self, params):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.get_data_list(params)

    def post_get_list(self, object):
        return object

    def pre_get_object(self, params):
        pass

    def get_data_object(self, params):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.get_data_object(params)

    def post_get_object(self, object):
        return object

    def pre_get_list_object(self, params):
        pass

    def get_data_list_object(self, params):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.get_data_list_object(params)

    def post_get_list_object(self, object):
        return object

    def pre_get_list_object_paginated(self, params):
        pass

    def get_data_list_object_paginated(self, params):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.get_data_list_object_paginated(params)

    def post_get_list_object_paginated(self, object):
        return object

    def get_data_list_object_any(self, sp_name, params: ParamsObject):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.get_data_list_object_any(sp_name, params)

    def get_data_list_object_any_paginated(self, sp_name, params: ParamsObject):
        notification_ack_repo: NotificationACKRepo = NotificationACKRepo()
        return notification_ack_repo.get_data_list_object_any_paginated(sp_name, params)
