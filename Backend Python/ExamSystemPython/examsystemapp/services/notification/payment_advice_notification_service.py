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

from examsystemapp.models.payment_advice_header import PaymentAdviceHeaderModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService


# from examsystemapp.services.invoice_header_service import InvoiceHeaderService


class PaymentAdviceNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        payment_advice_object: PaymentAdviceHeaderModel = PaymentAdviceHeaderModel()
        return payment_advice_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/payment-request/get?id=' + str(data.advice_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.advice_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        """ Get Payment Advice Detail """
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([data.advice_id])

        payment = self.get_direct("sNotificationPaymentAdviceGet", _params, False)
        payment = payment[0]

        self.ext_params["send_to"] = payment["Requested_By"]

        template = template.replace("<CREATED_BY>", str(payment["User_Name"]) + os.linesep)
        template = template.replace("<INV_NUM>", str(payment["Bills"]) + os.linesep)
        template = template.replace("<VENDORS>", str(payment["Vendors"]) + os.linesep)
        template = template.replace("<AMOUNT>", str(payment["Total"]))
        return template

    def _get_recipients(self, data: PaymentAdviceHeaderModel, conf):
        user_device_list = []
        params: ParamsObject = ParamsObject()
        params_list = []
        params_list.append(self.ext_params.get("send_to"))
        params.set_params_list(params_list)

        device_list = self.get_direct("sUserDeviceByIDGet", params, False)
        if device_list != "" and device_list is not None:
            if len(device_list) != 0:
                user_device_list.append(device_list)

        return user_device_list
