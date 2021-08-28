"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.vault import VaultModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService
from examsystemapp.services.invoice_header_service import InvoiceHeaderService


class VaultNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        vault_object:VaultModel = VaultModel()
        return vault_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return data

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/vault/get?id=' + str(data.vault_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.vault_id
        else:
            return None

    def _build_title(self, action, data, template1, conf):
        template = template1.replace("vault", "VAULT")
        return template

    def _build_description(self, action, data, template, conf):
        if data.type == 'FILE':
            template = template.replace("<_>","File")
        else:
            template = template.replace("<_>","FOLDER")
        # template = "<html><b>" + template + "<b></html>"
        return template

    def _get_recipients(self, data: VaultModel, conf):
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
            print(device_list)
            if device_list != "" and device_list is not None:
                if len(device_list) != 0:
                    user_device_list.append(device_list)

        return user_device_list
