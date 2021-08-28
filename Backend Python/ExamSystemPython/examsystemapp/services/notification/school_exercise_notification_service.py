"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.school_excercise import SchoolExcerciseModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
from examsystemapp.services.entity_service import EntityService


class SchoolExerciseNotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        school_exercise_object: SchoolExcerciseModel = SchoolExcerciseModel()
        return school_exercise_object.OBJECT_TYPE

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return '/exercise/get?id=' + str(data.school_excercise_id)
        else:
            return None

    def _get_object_id(self, action, data):
        if action == "ADD" or action == "UPDATE":
            return data.school_excercise_id
        else:
            return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        """ Get Exercise Detail """
        _params: ParamsObject = ParamsObject()
        _params.set_params_list([data.school_excercise_id])

        exc = self.get_direct("sNotificationExerciseGet", _params, False)
        exc = exc[0]

        template = template.replace("<EXERCISE>", str(exc["Exercise"]))
        template = template.replace("<SCHOOL_NAME>", str(exc["Entity_Name"]))
        template = template.replace("<CREATED_BY>", str(exc["User_Name"]))
        return template

    def _get_recipients(self, data: SchoolExcerciseModel, conf):
        user_device_list = []
        return user_device_list
