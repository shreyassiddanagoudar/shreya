"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.visit import VisitModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService
from examsystemapp.services.invoice_header_service import InvoiceHeaderService


class VisitNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        visit_object: VisitModel = VisitModel()
        return visit_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/visit/get?id=' + str(data.visit_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.visit_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        visit_id = data.visit_id
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([visit_id])
        _visit_detail = self.get_direct("sNotificationVisitGet", _params, False)
        template = template.replace("<CREATED_BY>", str(_visit_detail[0]["User_Name"]))
        template = template.replace("<PLACE>", str(_visit_detail[0]["City_Name"]))
        template = template.replace("<REASON>", str(_visit_detail[0]["Purpose"]))
        return template

    def _get_recipients(self, data: VisitModel, conf):
        user_device_list = []
        return user_device_list
