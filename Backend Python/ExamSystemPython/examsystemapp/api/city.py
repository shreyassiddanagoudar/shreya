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
from examsystemapp.models.city import CityModel
from examsystemapp.services.city_service import CityService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class City(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        city_json = json.loads(request.POST.get("city_json"))

        city_object: CityModel = CityModel()
        city_object.stateid = city_json.get("stateid")
        city_object.name = city_json.get("name")
        city_object.code = city_json.get("code")

        city_service: CityService = CityService()
        city_object = city_service.add(city_object)

        return self.send_response(city_object)

    def update(self, request: HttpRequest):
        city_json = json.loads(request.POST.get("city_json"))

        city_object: CityModel = CityModel()
        city_object.cityid = city_json.get("cityid")
        city_object.stateid = city_json.get("stateid")
        city_object.name = city_json.get("name")
        city_object.code = city_json.get("code")

        city_service: CityService = CityService()
        city_object = city_service.update(city_object)

        return self.send_response(city_object)

    def delete(self, request: HttpRequest):
        city_json = json.loads(request.POST.get("city_json"))

        city_object: CityModel = CityModel()
        city_object.cityid = city_json.get("cityid")

        city_service: CityService = CityService()
        city_object = city_service.delete(city_object)

        return self.send_response(city_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        city_service: CityService = CityService()
        data = city_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        city_service: CityService = CityService()
        data = city_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        city_service: CityService = CityService()
        data = city_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        city_service: CityService = CityService()
        data = city_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"state_id": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=None)},
            {"city_name": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default=None)},
            {"code": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default=None)},
            {"page_num": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=1)},
            {"page_size": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=10)},
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        city_service: CityService = CityService()
        data = city_service.get_list_object_paginated(params)
        return self.send_response(data)
