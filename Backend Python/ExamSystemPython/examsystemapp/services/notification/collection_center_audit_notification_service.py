"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.collection_centre_audit import CollectionCentreAuditModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService


class CCAuditNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        cc_audit_object: CollectionCentreAuditModel = CollectionCentreAuditModel()
        return cc_audit_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/collection-centre-audit/get?id=' + str(data.audit_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.audit_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):

        """ Get City Name """
        city_id_params: ParamsObject = ParamsObject()
        city_id_params.set_params_list([data.collection_centre_id])
        city_name = self.get_direct("sNotificationCCCityGet", city_id_params, False)
        city_name = city_name[0]["City_Name"]

        """ Get Created By User Name """
        _params: ParamsObject = ParamsObject()
        lst = []
        lst.append(self.ext_params.get("user_id"))
        _params.set_params_list(lst)
        user_list = self.get_direct("sNotificationUserNameGet", _params, False)
        user_name = user_list[0]["User_Name"]

        template = template.replace("<CITY>", str(city_name))
        template = template.replace("<CREATED_BY>", str(user_name))
        return template

    def _get_recipients(self, data: CollectionCentreAuditModel, conf):
        user_device_list = []
        return user_device_list
