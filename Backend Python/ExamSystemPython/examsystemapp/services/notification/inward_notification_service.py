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

from examsystemapp.models.inward_draft import InwardDraftModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService


class InwardNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        return "INWARD"

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/inward-draft/get?id=' + str(data._id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data._id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        total_quantity = 0
        total_price = 0
        seller_inv = data.seller_invoice_number
        data_dict = data.__dict__
        cart_item = data_dict["cart_item"]

        params_object: ParamsObject = ParamsObject()
        params_object.set_params_list([data.entity_id])
        get_entity_name = UserService().get_entity_name(params_object)

        user_name_params: ParamsObject = ParamsObject()
        user_name_params.set_params_list([self.ext_params["user_id"]])
        user_name = self.get_direct("sNotificationUserNameGet", user_name_params, False)
        user_name = user_name[0]["User_Name"]

        entity_name = get_entity_name[0]["Entity_Name"]

        for i in range(len(cart_item)):
            detail_cart_item = cart_item[i]
            cart_quantity = detail_cart_item.quantity
            cart_price = detail_cart_item.price
            total_quantity += cart_quantity
            total_price += (cart_price * cart_quantity)

        karo_inv = data.karo_invoice_number
        if data.is_draft == 0:
            template = template.replace("<VENDOR_NAME>", str(entity_name))
            template = template.replace("<TOTAL_QTY>", str(total_quantity))
            template = template.replace("<TOTAL_PRICE>", str(total_price))
            template = template.replace("<INV_NUM>", str(seller_inv))
            template = template.replace("<CREATED_BY>", user_name)
            template = template.replace("draft", "")
        else:
            template = template.replace("Purchase draft", "Purchase")
            template = template.replace("<VENDOR_NAME>", str(entity_name))
            template = template.replace("<TOTAL_QTY>", str(total_quantity))
            template = template.replace("<TOTAL_PRICE>", str(total_price))
            template = template.replace("<INV_NUM>", str(seller_inv) + os.linesep)
            template = template.replace("<CREATED_BY>", user_name + ". Please check and commit")
        return template

    def _get_recipients(self, data: InwardDraftModel, conf):
        user_device_list = []
        params: ParamsObject = ParamsObject()
        params_list = []
        for each_rec in conf:
            notification_default_recipients: NotificationDefaultRecipientsModel = each_rec
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

        params1: ParamsObject = ParamsObject()
        params1.set_params_list([data.state_id])
        zone = self.get_direct("sGetZoneByStateID", params1, False)
        zone = zone[0]
        zone_id = zone["Zone_ID"]
        params_manager_id = ParamsObject()
        params_manager_id.set_params_list([zone_id])
        zone_manager = self.get_direct("sGetZoneManagerByID", params_manager_id, False)
        manager_id = zone_manager[0]["Manager_ID"]
        params_list.append(manager_id)

        params.set_params_list(params_list)

        recipient_list = params.get_params_list()
        for id in recipient_list:
            params_obj = ParamsObject()
            params_obj.set_params_list([id])

            device_list = self.get_direct("sUserDeviceByIDGet", params_obj, False)
            if device_list != "" and device_list is not None:
                if isinstance(device_list, list):
                    if len(device_list) > 0:
                        user_device_list.append(device_list)

        return user_device_list
