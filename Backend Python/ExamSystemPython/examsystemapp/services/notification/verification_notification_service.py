"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.verification import VerificationModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject


class VerificationNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        verification_object: VerificationModel = VerificationModel()
        return verification_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return data

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/verification/get?id=' + str(data.verification_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.verification_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):

        _params: ParamsObject = ParamsObject()
        if action == "UPDATE":
            _verification_get_params: ParamsObject = ParamsObject()
            _verification_get_params.set_params_list([data.verification_id])
            verification = self.get_direct("sVerificationGet", _verification_get_params, False)
            verification = verification[0]
            _params.set_params_list([verification["Transaction_ID"], verification["Transaction_Type"]])
        else:
            _params.set_params_list([data.transaction_id, data.transaction_type])

        """ Get Verification Object """
        verification_detail = self.get_direct("sNotificationVerificationObjectGet", _params, False)

        verification_detail = verification_detail[0]

        self.ext_params["current_assignee"] = verification_detail["Current_Assignee"]

        template = template.replace("<INV_NUM>", str(verification_detail["Inv_Number"]) + "(" + str(
            verification_detail["Entity_Name"]) + ")")
        template = template.replace("<STATUS>", str(verification_detail["Status"]))

        return template

    def _get_recipients(self, data: VerificationModel, conf):
        user_device_list = []
        params: ParamsObject = ParamsObject()
        params_list = []
        params_list.append(self.ext_params.get("current_assignee"))
        params.set_params_list(params_list)

        device_list = self.get_direct("sUserDeviceByIDGet", params, False)
        if device_list != "" and device_list is not None:
            if len(device_list) != 0:
                user_device_list.append(device_list)
        return user_device_list
