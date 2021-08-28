"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
import os
import math
from string import Template

from examsystemapp.models.invoice_header import InvoiceHeaderModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.repository.invoice_header_repository import InvoiceHeaderRepo
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService


class InvoiceNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        invoice_object_type: InvoiceHeaderModel = InvoiceHeaderModel()
        return invoice_object_type.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/invoice/get?id=' + str(data.invoice_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.invoice_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):

        invoice_repo: InvoiceHeaderRepo = InvoiceHeaderRepo()
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([data.invoice_id])
        invoice_object: InvoiceHeaderModel = invoice_repo.get_data(_params)

        recycler_params: ParamsObject = ParamsObject()
        recycler_params.set_params_list([invoice_object.recycler_id])
        recycler_name_list = UserService().get_entity_name(recycler_params)
        recycler_name = recycler_name_list[0]["Entity_Name"]

        total: float = 0
        for detail in invoice_object.invoice_detail:
            total += detail.quantity

        invoice_amount: float = invoice_object.invoice_total_amount
        invoice_amount = round(invoice_amount, 2)
        total = round(total, 2)
        template = template.replace("<INV_NUM>", invoice_object.updated_invoice_number + os.linesep)
        template = template.replace("<RECYCLER>", recycler_name + os.linesep)
        template = template.replace("<TOTALAMOUNT>", str(invoice_amount) + os.linesep)
        template = template.replace("<QUANTITY>", str(total))

        return template

    def _get_recipients(self, data: InvoiceHeaderModel, conf):
        user_device_list = []
        for each_rec in conf:
            notification_default_recipients: NotificationDefaultRecipientsModel = each_rec

            params: ParamsObject = ParamsObject()
            params_list = []

            if notification_default_recipients.procedure_config == None or notification_default_recipients.procedure_config == "":
                pass
            else:
                procedure_config_str = notification_default_recipients.procedure_config
                procedure_config_lst = []
                if procedure_config_str != "" and procedure_config_str is not None:
                    procedure_config_lst = json.loads(procedure_config_str)

                for each_config in procedure_config_lst:
                    _property = each_config["property"]
                    _from = each_config["from"]

                    if _from == "session":
                        params_list.append(self.ext_params.get(_property))
                    else:
                        params_list.append(data.__getattribute__(_property))

            params.set_params_list(params_list)

            device_list = self.get_direct(notification_default_recipients.procedure_name, params, False)
            if device_list != "" and device_list is not None:
                if len(device_list) != 0:
                    user_device_list.append(device_list)

        return user_device_list
