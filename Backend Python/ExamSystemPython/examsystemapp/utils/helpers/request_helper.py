"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
import requests
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpRequest
from examsystemapp.utils.constants.constants import HttpMethodType, DataTypes, ErrorCodes
from enum import Enum

from examsystemapp.utils.exception_handling.exception import KaroException
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.session_helper import SessionHelper, JWTManager


class RequestConfig:

    def __init__(self, from_session=False, default=None, nullable=True, datatype=DataTypes.STRING, session_key=None):
        self.from_session = from_session
        self.default = default
        self.nullable = nullable
        self.datatype = datatype
        self.session_key = session_key


class ResponseObject:
    def __init__(self, response_message, response_object, http_status=200, error_code=None):
        self.http_status = http_status
        self.response_message = response_message
        self.error_code = error_code
        self.response_object = response_object


class ParamsObject:
    def __init__(self, params_list=[], params_dict={}):
        self.params_list = params_list
        self.params_dict = params_dict

    def get_params_list(self):
        return self.params_list

    def set_params_list(self, params_list):
        self.params_list = params_list

    def get_params_dict(self):
        return self.params_dict

    def set_params_dict(self, params_dict):
        self.params_dict = params_dict


class RequestHelper:

    def __init__(self):
        self.return_params = {"list": [], "dict": {}}
        self.params_object = ParamsObject()
        self.token_payload = None

    def get_session_value(self, request, key, session_key, datatype, default_value):
        val = None
        if self.token_payload is None:
            self.token_payload = JWTManager.decode_token(
                request.META['HTTP_AUTHORIZATION'].replace("Bearer ", ''))

        if datatype == DataTypes.INT:
            if session_key != "" and session_key is not None:
                val = IntHelper.string_to_int(
                    JWTManager.get_payload_value_by_key(self.token_payload, session_key))
            else:
                val = IntHelper.string_to_int(JWTManager.get_payload_value_by_key(self.token_payload, key.lower()))
        elif datatype == DataTypes.FLOAT:

            if session_key != "" and session_key is not None:
                val = FloatHelper.string_to_float(
                    JWTManager.get_payload_value_by_key(self.token_payload, session_key))
            else:
                val = FloatHelper.string_to_float(
                    JWTManager.get_payload_value_by_key(self.token_payload, key.lower()))
        else:
            if session_key != "" and session_key is not None:
                val = JWTManager.get_payload_value_by_key(self.token_payload, session_key)
            else:
                val = JWTManager.get_payload_value_by_key(self.token_payload, key.lower())
        if val is None:
            val = default_value

        return val

    def convert_post(self, request: HttpRequest, params_config=None):
        for each_param in params_config:
            key = next(iter(each_param))
            config: RequestConfig = each_param.get(key)
            val = None
            if config.from_session:
                val = self.get_session_value(request, key, config.session_key, config.datatype, config.default)
            else:
                if config.datatype == DataTypes.INT:
                    val = request.POST.get(key, default=config.default)
                    if val == "" or val == "null" or val == "None":
                        val = config.default
                    elif val is not None:
                        val = IntHelper.string_to_int(val, config.default)
                    else:
                        val = config.default
                elif config.datatype == DataTypes.FLOAT:
                    val = request.POST.get(key, default=config.default)
                    if val == "" or val == "null" or val == "None":
                        val = config.default
                    elif val is not None:
                        val = FloatHelper.string_to_float(val, config.default)
                    else:
                        val = config.default
                else:
                    val = request.POST.get(key, default=config.default)
                    if val == "null" or val == "None" or val == "none" or val == "":
                        val = config.default

            self.return_params.get("list").append(val)
            self.return_params.get("dict")[key] = val

        self.params_object.set_params_list(self.return_params.get("list"))
        self.params_object.set_params_dict(self.return_params.get("dict"))

        return self.params_object

    def convert_get(self, request: HttpRequest, params_config=None):
        for each_param in params_config:
            key = next(iter(each_param))
            config: RequestConfig = each_param.get(key)
            val = None
            if config.from_session:
                val = self.get_session_value(request, key, config.session_key, config.datatype, config.default)
            else:
                if config.datatype == DataTypes.INT:
                    val = request.GET.get(key, default=config.default)
                    if val == "" or val == "null" or val == "None":
                        val = config.default
                    elif val is not None:
                        val = IntHelper.string_to_int(val, config.default)
                    else:
                        val = config.default
                elif config.datatype == DataTypes.FLOAT:
                    val = request.GET.get(key, default=config.default)
                    if val == "" or val == "null" or val == "None":
                        val = config.default
                    elif val is not None:
                        val = FloatHelper.string_to_float(val, config.default)
                    else:
                        val = config.default
                else:
                    val = request.GET.get(key, default=config.default)
                    if val == "null" or val == "None" or val == "none" or val == "":
                        val = config.default

            self.return_params.get("list").append(val)
            self.return_params.get("dict")[key] = val

        self.params_object.set_params_list(self.return_params.get("list"))
        self.params_object.set_params_dict(self.return_params.get("dict"))

        return self.params_object

    # def convert_put(self, request: HttpRequest, params_config=None):
    #     for each_param in params_config:
    #         key = next(iter(each_param))
    #         config: Test = each_param.get(key)
    #         val = None
    #         if config.from_session == 1:
    #             val = None
    #         else:
    #             val = request.PUT.get(key, default=config.default)
    #
    #         self.return_params.get("list").append(val)
    #         self.return_params.get("dict")[key] = val
    #
    # def convert_delete(self, request: HttpRequest, params_config=None):
    #     for each_param in params_config:
    #         key = next(iter(each_param))
    #         config: Test = each_param.get(key)
    #         val = None
    #         if config.from_session == 1:
    #             val = None
    #         else:
    #             val = request.DELETE.get(key, default=config.default)
    #
    #         self.return_params.get("list").append(val)
    #         self.return_params.get("dict")[key] = val

    def convert_request_params(self, request: HttpRequest, http_method: Enum, params_config=None):
        """
        :description: Will convert the params config to ParamsObject
        :param request: HttpRequest that is coming from the client
        :param http_method: Type of Http method
        :param params_config: List of Dictionary, contains the configuration
        :return: ParamsObject
        """
        if http_method.value == HttpMethodType.post.value:
            if params_config is None:
                return self.return_params
            else:
                return self.convert_post(request, params_config)
        else:
            # if its a get method
            if params_config is None:
                return self.return_params
            else:
                return self.convert_get(request, params_config)

    def call_ext_api(self, request: HttpRequest, host, is_token_needed=True):
        """
        :description: This to call the external API from this app.
        :param request: Request object from the client
        :param host: Host of the API
        :param is_token_needed: token (Needs to be passed True if the request needs to check the token at the other side)
        :return: JSON response from the API
        """
        try:
            response = None

            files = dict()
            data = dict()
            headers = dict()

            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'

            url = host + request.get_full_path()

            if is_token_needed:
                headers["TOKEN"] = settings.APP_SECRETE

            if 'HTTP_AUTHORIZATION' in request.META:
                headers["Authorization"] = request.META.get('HTTP_AUTHORIZATION')

            if len(request.FILES) > 0:
                for key, file in request.FILES.items():
                    file: InMemoryUploadedFile = file
                    files[file._name] = file

            if request.method == "POST":
                if len(request.POST) > 0:
                    for key, value in request.POST.items():
                        data[key] = value
                response = requests.post(url, files=files, data=data, headers=headers)
            else:
                response = requests.get(url, headers=headers)

            return response.json()
        except Exception as ex:
            raise KaroException(ErrorCodes.GENERAL_ERROR, str(ex), None)
