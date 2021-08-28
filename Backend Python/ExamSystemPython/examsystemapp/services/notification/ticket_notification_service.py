"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
import os
from string import Template

from examsystemapp.models.ticket import TicketModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService
from examsystemapp.services.invoice_header_service import InvoiceHeaderService


class TicketNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        ticket_object: TicketModel = TicketModel()
        return ticket_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/ticket/get?id=' + str(data.ticket_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.ticket_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        """ Get Event Detail """
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([data.ticket_id])

        ticket = self.get_direct("sNotificationTicketGet", _params, False)
        ticket = ticket[0]

        template = template.replace("<CREATED_BY>", str(ticket["User_Name"]) + os.linesep)
        template = template.replace("<TITLE>", str(ticket["Title"]) + os.linesep)
        template = template.replace("<DESCRIPTION>", str(ticket["Description"]) + os.linesep)
        template = template.replace("<SEVERITY>", str(ticket["Severity_Desc"]))
        return template

    def _get_recipients(self, data: TicketModel, conf):
        user_device_list = []
        return user_device_list
