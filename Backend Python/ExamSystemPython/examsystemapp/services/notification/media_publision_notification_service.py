"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.media_publication import MediaPublicationModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService


class MediaPublicationNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        media_publication_object: MediaPublicationModel = MediaPublicationModel()
        return media_publication_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/media-publication/get?id=' + str(data.media_publication_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.media_publication_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        """ Get Exercise Detail """
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([data.media_publication_id])

        media = self.get_direct("sNotificationMediaGet", _params, False)
        media = media[0]

        template = template.replace("<TYPE>", str(media["Type_Name"]))
        template = template.replace("<DESCRIPTION>", str(media["Description"]))
        template = template.replace("<CREATED_BY>", str(media["User_Name"]))
        return template

    def _get_recipients(self, data: MediaPublicationModel, conf):
        user_device_list = []
        return user_device_list
