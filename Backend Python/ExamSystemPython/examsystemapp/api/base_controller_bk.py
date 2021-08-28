import hashlib
import pickle
import threading
from datetime import datetime, timezone

from django.http import HttpRequest, HttpResponse

from examsystemapp.utils.helpers.logging_helper import LoggingHelper
from examsystemapp.utils.helpers.request_helper import RequestHelper, ResponseObject
from examsystemapp.utils.helpers.session_helper import SessionHelper, JWTManager
import json
from django.core.serializers.json import DjangoJSONEncoder
from enum import Enum

from django.conf import settings

from examsystemapp.utils.exception_handling.exception import PermissionDeniedException
from examsystemapp.utils.constants.constants import ErrorCodes, AppConstants


def convert_to_dict(obj):
    return obj.__dict__


class BaseController:

    def __init__(self, request):
        self.token_payload = None
        # self.check_session(request)

    def build_response_object(self, response_object, response_message, http_status, error_code):
        pass

    def send_response(self, response_object, response_message="Success", http_status=200, error_code=None):
        obj = ResponseObject(response_message, response_object, http_status, error_code)
        json_object = json.dumps(obj, default=convert_to_dict, indent=2, cls=DjangoJSONEncoder)
        return HttpResponse(json_object, content_type='application/json', status=http_status)

    def send_response_raw_json(self, response_object, http_status=200):
        json_object = json.dumps(response_object, indent=2)
        return HttpResponse(json_object, content_type='application/json', status=http_status)

    def check_session(self, request: HttpRequest):
        try:
            if request.method != "OPTIONS":
                if 'HTTP_AUTHORIZATION' in request.META:
                    self.token_payload = JWTManager.decode_token(
                        request.META['HTTP_AUTHORIZATION'].replace("Bearer ", ''))

                    # Check the checksum
                    cp_token_val = dict(self.token_payload)
                    cp_token_val.pop("cs")

                    cs = JWTManager.get_checksum(cp_token_val)

                    if self.token_payload.get("cs") != cs:
                        raise PermissionDeniedException(ErrorCodes.MALFUNCTIONED_TOKEN, 'Malfunctioned Token', None)

                    # Check whether the token is expired
                    expire_str = self.token_payload.get("expires_on")
                    cur = datetime.now(tz=timezone.utc).strftime(AppConstants.TOKEN_EXPIRY_DATETIME_FORMAT)

                    datetime_obj = datetime.strptime(expire_str, AppConstants.TOKEN_EXPIRY_DATETIME_FORMAT)

                    if datetime.strptime(cur, AppConstants.TOKEN_EXPIRY_DATETIME_FORMAT) > datetime_obj:
                        raise PermissionDeniedException(ErrorCodes.TOKEN_EXPIRED, 'Token Expired', None)
                else:
                    raise PermissionDeniedException(ErrorCodes.PERMISSION_DENIED, 'Permission Denied', None)
        except PermissionDeniedException as ex:
            if settings.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, str(ex), request.META.keys())
            raise PermissionDeniedException(ex.error_code, ex.error_message, None)
        except Exception as ex:
            if settings.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, str(ex), request.META.keys())
            raise PermissionDeniedException(ErrorCodes.PERMISSION_DENIED, 'Permission Denied', None)

    def convert_params(self, request: HttpRequest, http_method: Enum, params_config=None):
        return RequestHelper().convert_request_params(request, http_method, params_config)

    def get_entity_id(self):
        return JWTManager.get_payload_value_by_key(self.token_payload, 'entity_id')

    def get_user_id(self):
        return JWTManager.get_payload_value_by_key(self.token_payload, 'user_id')

    def get_entity_user_ext_params(self):
        ext_params = {
            "entity_id": self.get_entity_id(),
            "user_id": self.get_user_id()
        }
        return ext_params

    def get_roles(self):
        return JWTManager.get_payload_value_by_key(self.token_payload, 'roles')