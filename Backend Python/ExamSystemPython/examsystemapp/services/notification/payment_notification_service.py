"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.payment_header import PaymentHeaderModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService


# from examsystemapp.services.invoice_header_service import InvoiceHeaderService


class PaymentNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        payment_object: PaymentHeaderModel = PaymentHeaderModel()
        return payment_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/payment/get?id=' + str(data.payment_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.payment_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        """ Get Payment Detail """
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([data.payment_id])

        payment = self.get_direct("sNotificationPaymentGet", _params, False)
        payment = payment[0]

        self.ext_params["send_to"] = payment["Advised_By"]

        template = template.replace("<PAYMENT>", str(payment["Payments"]))
        return template

    def _get_recipients(self, data: PaymentHeaderModel, conf):
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
