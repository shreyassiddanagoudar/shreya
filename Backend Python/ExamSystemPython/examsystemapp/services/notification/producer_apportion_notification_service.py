"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.producer_apportion import ProducerApportionModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService


class ProducerApportionNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        producer_apportion_object_type:ProducerApportionModel = ProducerApportionModel()
        return producer_apportion_object_type.OBJECT_TYPE

    def _get_payload(self, action, data):
        return data

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/apportion/get?id=' + str(data._id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data._id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        template = template.replace("APPORTION", "PRODUCERAPPORTION")
        return template

    def _build_description(self, action, data, template, conf):
        invoce_number = data.invoice_id
        quantity = data.quantity

        # ext_params = self.get_entity_user_ext_params()
        # entity_id = self.ext_params['entity_id']
        params_object:ParamsObject = ParamsObject()
        params_object.set_params_list([self.ext_params.get('entity_id')])
        entity_service: EntityService = EntityService()
        get_producer_name = entity_service.get_data(params_object)
        producer_name = get_producer_name.entity_name

        category_params:ParamsObject = ParamsObject()
        category_params.set_params_list([data.category_id])
        category_name = self.get_direct("_sGetCategory",category_params,False)

        template = template.replace("<item>", category_name[0]["Option_Text"])
        template = template.replace("<target>",producer_name)
        template = template.replace("<allocated>",str(quantity))
        # template = "<html><b>" + template + "<b></html>"
        #Total allocation for producer <item>-<target>-<allocated>
        return template

    def _get_recipients(self, data: ProducerApportionModel, conf):
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
