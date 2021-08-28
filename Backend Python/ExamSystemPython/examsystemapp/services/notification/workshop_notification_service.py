"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.workshop import WorkshopModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService
from examsystemapp.services.invoice_header_service import InvoiceHeaderService


class WorkshopNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        workshop_object: WorkshopModel = WorkshopModel()
        return workshop_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/workshop/get?id=' + str(data.workshop_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.workshop_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):

        """ Get Workshop Detail """
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([data.workshop_id])

        workshop = self.get_direct("sNotificationWorkshopGet", _params, False)
        workshop = workshop[0]

        template = template.replace("<TYPE>", str(workshop["Type"]))
        template = template.replace("<PLACE>", str(workshop["City_Name"]))
        template = template.replace("<CREATED_BY>", str(workshop["User_Name"]))
        return template

    def _get_recipients(self, data: WorkshopModel, conf):
        user_device_list = []
        return user_device_list
