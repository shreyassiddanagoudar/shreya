"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService
from examsystemapp.services.invoice_header_service import InvoiceHeaderService
from examsystemapp.utils.helpers.file_helper import FileHelper


class RecyclerPoeNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        return "RECYCLERPOE"

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            transaction_id = data["file_detail"]
            for i in transaction_id:
                transaction_id = i["transaction_id"]
            return '/invoice-poe/get-outward-poe?invoice_id=' + str(transaction_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            transaction_id = data["file_detail"]
            for i in transaction_id:
                transaction_id = i["transaction_id"]
            return transaction_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        document_type = ''
        transaction_id = None
        for i in data["file_detail"]:
            transaction_id = i["transaction_id"]
            for j in i["files"]:
                type = j["document_type"]
                document_type = document_type + type + ","
        # transaction_id = data["transaction_id"]
        params_object: ParamsObject = ParamsObject()
        params_object.set_params_list([transaction_id])
        get_document_name = FileHelper().get_document_list_by_type(document_type)
        document_name = get_document_name["response_object"]
        display_name = ""

        cnt = 0
        for i in document_name:
            if cnt == 0:
                display_name = display_name + i["display_name"]
                cnt = cnt + 1
            else:
                display_name = display_name + "," + i["display_name"]

        invoice_params: ParamsObject = ParamsObject()
        invoice_params.set_params_list([transaction_id])
        invoice_id = self.get_direct("sInvoiceHeaderGet", invoice_params, False)
        template = template.replace("<DOC_TYPE>", display_name)
        template = template.replace("<INV_NUM>", str(invoice_id[0]["Updated_Invoice_Number"]))
        return template

    def _get_recipients(self, data, conf):
        try:
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
        except Exception as ex:
            print("in recipient exc")
            print(ex)
