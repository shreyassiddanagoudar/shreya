"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.calendar_event import CalendarEventModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService
from examsystemapp.services.invoice_header_service import InvoiceHeaderService


class CalendarEventNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        calendar_event_object: CalendarEventModel = CalendarEventModel()
        return calendar_event_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/calendar-event/get?id=' + str(data.event_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.event_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        """ Get Event Detail """
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([data.event_id])

        event = self.get_direct("sNotificationCalendarGet", _params, False)
        event = event[0]

        template = template.replace("<TITLE>", str(event["Title"]))
        template = template.replace("<DESCRIPTION>", str(event["Description"]))
        template = template.replace("<CREATED_BY>", str(event["User_Name"]))
        return template

    def _get_recipients(self, data: CalendarEventModel, conf):
        user_device_list = []
        return user_device_list
