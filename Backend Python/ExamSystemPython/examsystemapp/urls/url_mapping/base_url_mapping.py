"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

from examsystemapp.utils.helpers.request_helper import ResponseObject
import json


def convert_to_dict_error(obj):
    return obj.__dict__


def send_response(response_object, response_message, http_status=200, error_code=None):
    obj = ResponseObject(response_message, response_object, http_status, error_code)
    json_object = json.dumps(obj, default=convert_to_dict_error, indent=2, cls=DjangoJSONEncoder)
    return HttpResponse(json_object, content_type='application/json', status=http_status)
