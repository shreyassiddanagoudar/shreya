"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
import json
import threading

from django.core.serializers.json import DjangoJSONEncoder

from examsystemapp.models.notification.notification_config import NotificationConfigModel
from examsystemapp.models.notification.notification_log import NotificationLogModel
from examsystemapp.models.notification.notification_payload import NotificationPayload
from examsystemapp.models.notification.notification_recipient_group import NotificationRecipientGroupModel
from examsystemapp.repository.notification.notification_config_repository import NotificationConfigRepo
from examsystemapp.repository.notification.notification_log_repository import NotificationLogRepo
from examsystemapp.services.base_service import BaseService
from examsystemapp.utils.helpers.general_helper import StringHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject
from pyfcm import FCMNotification


def convert_to_dict(obj):
    return obj.__dict__


class BaseNotificationService(BaseService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseService.__init__(self, ext_params, is_transaction_owner, event_type)
        self.config = None
        self.data = None
        self.ext_data = {}

    def _convert_to_dict(self, obj):
        return obj.__dict__

    def __get_conf(self, action):
        """
        This method is used to get the notification configuration
        Object type can be read from object_type method which overridden in the child class
        :param action: The action on the Object like ADD, UPDATE, DELETE etc.
        :return: NotificationConfiguration Object
        """
        params: ParamsObject = ParamsObject()
        params.set_params_list([self._object_type(), action])

        self.config = NotificationConfigRepo(self.ext_params).get_data_list_object(params)
        return self.config

    def __get_group_users(self, notification_recipient_group_list):
        """
        This method is used to get the users for the group if defined any
        :param notification_id:
        :return: List of User Device object
        """
        user_device_list = []
        if notification_recipient_group_list != "" and notification_recipient_group_list is not None:
            for each_group in notification_recipient_group_list:
                notification_recipient_group: NotificationRecipientGroupModel = each_group
                params: ParamsObject = ParamsObject()

                params.set_params_list([notification_recipient_group.recipient_id, notification_recipient_group.type])
                device_list = self.get_direct("sUserDeviceGetByNotificationGroup", params, False)
                if device_list != "" and device_list is not None:
                    user_device_list.append(device_list)
            return user_device_list
        else:
            return user_device_list

    def __add_log(self, notification_id, title, description, image, payload, url, object_id, recipients):
        """
        This method is used to add the log before sending notification
        :return: NotificationLog Object
        """
        notification_log: NotificationLogModel = NotificationLogModel()
        notification_log.notification_id = notification_id
        notification_log.title = title
        notification_log.description = description
        notification_log.image = image
        notification_log.payload = StringHelper.cast_string(payload)
        notification_log.url = url
        notification_log.object_id = StringHelper.cast_string(object_id)
        notification_log.recipients = str(recipients)
        return NotificationLogRepo(self.ext_params).add_data(notification_log)

    def __update_log(self, log_id, payload):
        notification_log: NotificationLogModel = NotificationLogModel()
        notification_log.log_id = log_id
        notification_log.payload = StringHelper.cast_string(payload)
        return NotificationLogRepo(self.ext_params).update_data(notification_log)

    def __build_payload(self, object_type, action, title, description, notification_id, log_id, object_id, url, data):
        obj = NotificationPayload(object_type, action, title, description, notification_id, log_id, object_id, url,
                                  data)
        json_object = json.dumps(obj, default=convert_to_dict, indent=2, cls=DjangoJSONEncoder)
        print(json_object)
        return json_object

    def _object_type(self):
        """
        This method needs to be overridden in child class to get the object type
        :return: Object Type as string
        """
        pass

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        return None

    def _get_object_id(self, action, data):
        return None

    def _build_title(self, action, data, template, conf):
        """
        This method is used to build title for the notification
        This method should be overridden in the child class to build title
        :param action: Action on the Object
        :param data: Data sent by the callee (Who initiated the notification)
        :param template: Template for the title
        :param conf: Configuration for the title template
        :return: Title as String
        """
        return None

    def _build_description(self, action, data, template, conf):
        """
        This method is used to build description for the notification
        This method should be overridden in the child class to build description
        :param action: Action on the Object
        :param data: Data sent by the callee (Who initiated the notification)
        :param template: Template for the description
        :param conf: Configuration for the description template
        :return: Description as String
        """
        return None

    def _get_recipients(self, data, conf):
        """
        This method is used to get the recipients for the notification
        This method needs to be overridden in the child class to get the recipients
        :param data: Data sent by the callee (Who initiated the notification)
        :param conf: Recipient configuration
        :return: List of User devices
        """
        pass

    def __send_to_android(self, devices, payload):
        if len(devices) > 0:
            push_service = FCMNotification("AIzaSyC8klPf-BGfx1xYcF3SLi7IRC8l_t3KVy4")
            # result = push_service.notify_multiple_devices(registration_ids=devices, message_title=payload["title"],
            #                                               message_body=payload["description"],
            #                                               data_message=payload)

            result = push_service.notify_multiple_devices(registration_ids=devices, data_message=payload)
        return True

    def __send_to_ios(self, devices, payload):
        if len(devices) > 0:
            push_service = FCMNotification("api-key")
            # result = push_service.notify_multiple_devices(registration_ids=devices, message_title=payload["title"],
            #                                               message_body=payload["description"],
            #                                               data_message=payload)

            result = push_service.notify_multiple_devices(registration_ids=devices, data_message=payload)
        return True

    def __send_to_desktop(self, devices, payload):
        if len(devices) > 0:
            push_service = FCMNotification("api-key")
            # result = push_service.notify_multiple_devices(registration_ids=devices, message_title=payload["title"],
            #                                               message_body=payload["description"],
            #                                               data_message=payload)
            result = push_service.notify_multiple_devices(registration_ids=devices, data_message=payload)
        return True

    def __send_notification(self, devices, payload):
        """
        This sends the actual notification
        :param devices: list of user_device object. Needs to take out the device ids from this
        :param payload: actual payload to the notification. data key should have this payload as value
        :return:
        """
        android_device_ids = set()
        ios_device_ids = set()
        desktop_ids = set()
        payload = json.loads(payload)
        for each_device in devices:
            for i in each_device:
                if i["Device_Type"] == "ANDROID":
                    android_device_ids.add(i["Device_ID"])
                elif i["Device_Type"] == "IPHONE":
                    ios_device_ids.add(i["Device_ID"])
                else:
                    desktop_ids.add(i["Device_ID"])

        self.__send_to_android(list(android_device_ids), payload)
        self.__send_to_ios(list(ios_device_ids), payload)
        self.__send_to_desktop(list(desktop_ids), payload)

        return True

    def send_notification_thread(self, action, data):
        """
        This public method is called by the any who wants to send the notification
        This method is responsible to get Configuration, Build Title, Build Description, Get Recipients, get group recipients and to send the actual notification to clients
        :param action:
        :param data:
        :return:
        """
        try:
            """
            1. Get Configuration -- Base
            2. Build Title -- Child
            3. Build Description -- Child
            4. Get Device IDs for default users -- Child
            5. Get Device IDs for Group Users -- Base
            6. Add to Notification Log -- Base
            7. Send Actual Notification -- Base
            """

            """ Get Config """
            config_list = self.__get_conf(action)

            for config in config_list:
                if config is not None:
                    """ Build Title """
                    """
                    Configuration 
                    Ex : <Seller_Name> raised invoice <Invoice_Number> - <Total_Quantity>
                    [{"property": "<Seller_Name>", "from": "NameByID"}, {"property": "<Invoice_Number>", "from": "data.seller_bill.updated_bill_number"}]
                    """
                    title = self._build_title(action, data, config.title, config.title_config)

                    """ Build Description """
                    description = self._build_description(action, data, config.description, config.description_config)

                    """ Get Default Recipients """
                    """
                    Configuration 
                    [{"property": "user_id", "from": "session"}, {"property": "check_by", "from": "data"}, {"property": "bill_id", "from": "data.seller_bill.bill_id"}]
                    """
                    recipients = self._get_recipients(data, config.notification_default_recipients)
                    """ Group Recipients """
                    group_recipients = []
                    if config.notification_recipient_group != "" and config.notification_recipient_group is not None:
                        group_recipients = self.__get_group_users(config.notification_recipient_group)
                    if recipients != "" and recipients is not None:
                        if isinstance(recipients, list):
                            if len(group_recipients) > 0:
                                recipients.extend(group_recipients)

                            log_rec = set()
                            for each_rec in recipients:
                                for device in each_rec:
                                    log_rec.add(device.get("User_ID"))

                            log_rec = list(log_rec)
                            """ Add to Notification Log """
                            notification_log = self.__add_log(config.notification_id, title, description, None,
                                                              self._get_payload(action, data),
                                                              self._get_url(action, data),
                                                              self._get_payload(action, data), log_rec)
                            """ Build Payload """
                            _payload = self.__build_payload(self._object_type(), action, title, description,
                                                            config.notification_id,
                                                            notification_log.log_id,
                                                            self._get_object_id(action, data),
                                                            self._get_url(action, data),
                                                            self._get_payload(action, data))

                            """ Update Log for Payload """
                            self.__update_log(notification_log.log_id, _payload)

                            """ Send Actual Notification """
                            self.__send_notification(recipients, _payload)
            return True
        except Exception as ex:
            print(ex)

    def send_notification(self, action, data):
        try:
            # return True
            notification_thread = threading.Thread(target=self.send_notification_thread,
                                                   args=(action, data))
            notification_thread.start()
            return True
        except Exception as ex:
            return False

    def send_generic_notification(self, users, title, description, type):
        pass
