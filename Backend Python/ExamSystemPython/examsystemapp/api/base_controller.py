
from django.http import HttpRequest, HttpResponse

from examsystemapp.utils.helpers.request_helper import RequestHelper, ResponseObject
import json
from django.core.serializers.json import DjangoJSONEncoder
from enum import Enum


def convert_to_dict(obj):
    return obj.__dict__


class BaseController:

    def __init__(self, request):
        pass

    def send_response(self, response_object, response_message="Success", http_status=200, error_code=None):
        obj = ResponseObject(response_message, response_object, http_status, error_code)
        json_object = json.dumps(obj, default=convert_to_dict, indent=2, cls=DjangoJSONEncoder)
        return HttpResponse(json_object, content_type='application/json', status=http_status)

    def send_response_raw_json(self, response_object, http_status=200):
        json_object = json.dumps(response_object, indent=2)
        return HttpResponse(json_object, content_type='application/json', status=http_status)

    def convert_params(self, request: HttpRequest, http_method: Enum, params_config=None):
        return RequestHelper().convert_request_params(request, http_method, params_config)
