"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from django.http import HttpRequest
from examsystemapp.api.base_controller import BaseController
from examsystemapp.models.state import StateModel
from examsystemapp.services.state_service import StateService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class State(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        state_json = json.loads(request.POST.get("state_json"))

        state_object: StateModel = StateModel()
        state_object.name = state_json.get("name")
        state_object.code = state_json.get("code")

        state_service: StateService = StateService()
        state_object = state_service.add(state_object)

        return self.send_response(state_object)

    def update(self, request: HttpRequest):
        state_json = json.loads(request.POST.get("state_json"))

        state_object: StateModel = StateModel()
        state_object.stateid = state_json.get("stateid")
        state_object.name = state_json.get("name")
        state_object.code = state_json.get("code")

        state_service: StateService = StateService()
        state_object = state_service.update(state_object)

        return self.send_response(state_object)

    def delete(self, request: HttpRequest):
        state_json = json.loads(request.POST.get("state_json"))

        state_object: StateModel = StateModel()
        state_object.stateid = state_json.get("stateid")
        state_object.name = state_json.get("name")
        state_object.code = state_json.get("code")

        state_service: StateService = StateService()
        state_object = state_service.delete(state_object)

        return self.send_response(state_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        state_service: StateService = StateService()
        data = state_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        state_service: StateService = StateService()
        data = state_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        state_service: StateService = StateService()
        data = state_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        state_service: StateService = StateService()
        data = state_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"state_name": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')},
            {"code": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')},
            {"page_num": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=1)},
            {"page_size": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=10)},
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        state_service: StateService = StateService()
        data = state_service.get_list_object_paginated(params)
        return self.send_response(data)
