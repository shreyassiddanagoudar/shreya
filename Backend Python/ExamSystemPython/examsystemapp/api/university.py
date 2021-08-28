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
from examsystemapp.models.university import UniversityModel
from examsystemapp.services.university_service import UniversityService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class University(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        university_json = json.loads(request.POST.get("university_json"))

        university_object: UniversityModel = UniversityModel()
        # university_object.universityid = university_json.get("universityid")
        university_object.name = university_json.get("name")
        university_object.code = university_json.get("code")
        university_object.addr1 = university_json.get("addr1")
        university_object.addr2 = university_json.get("addr2")
        university_object.addr3 = university_json.get("addr3")
        university_object.cityid = university_json.get("cityid")
        university_object.stateid = university_json.get("stateid")
        university_object.pincode = university_json.get("pincode")
        university_object.phone = university_json.get("phone")
        university_object.email = university_json.get("email")
        university_object.logo = university_json.get("logo")
        university_object.url = university_json.get("url")

        university_service: UniversityService = UniversityService()
        university_object = university_service.add(university_object)

        return self.send_response(university_object)

    def update(self, request: HttpRequest):
        university_json = json.loads(request.POST.get("university_json"))

        university_object: UniversityModel = UniversityModel()
        university_object.universityid = university_json.get("universityid")
        university_object.name      = university_json.get("name")
        university_object.code      = university_json.get("code")
        university_object.addr1     = university_json.get("addr1")
        university_object.addr2     = university_json.get("addr2")
        university_object.addr3     = university_json.get("addr3")
        university_object.cityid    = university_json.get("cityid")
        university_object.stateid   = university_json.get("stateid")
        university_object.pincode   = university_json.get("pincode")
        university_object.phone     = university_json.get("phone")
        university_object.email     = university_json.get("email")
        university_object.logo      = university_json.get("logo")
        university_object.url       = university_json.get("url")

        university_service: UniversityService = UniversityService()
        university_object = university_service.update(university_object)

        return self.send_response(university_object)

    def delete(self, request: HttpRequest):
        university_json = json.loads(request.POST.get("university_json"))

        university_object: UniversityModel = UniversityModel()
        university_object.universityid = university_json.get("universityid")
        # university_object.name = university_json.get("name")
        # university_object.code = university_json.get("code")
        # university_object.addr1 = university_json.get("addr1")
        # university_object.addr2 = university_json.get("addr2")
        # university_object.addr3 = university_json.get("addr3")
        # university_object.cityid = university_json.get("cityid")
        # university_object.stateid = university_json.get("stateid")
        # university_object.pincode = university_json.get("pincode")
        # university_object.phone = university_json.get("phone")
        # university_object.email = university_json.get("email")
        # university_object.logo = university_json.get("logo")
        # university_object.url = university_json.get("url")

        university_service: UniversityService = UniversityService()
        university_object = university_service.delete(university_object)

        return self.send_response(university_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_service: UniversityService = UniversityService()
        data = university_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_service: UniversityService = UniversityService()
        data = university_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_service: UniversityService = UniversityService()
        data = university_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_service: UniversityService = UniversityService()
        data = university_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"UniversityName":  RequestConfig(from_session=False, nullable=True,  datatype=DataTypes.STRING, default=None)},
            {"StateID":         RequestConfig(from_session=False, nullable=True,  datatype=DataTypes.INT,    default=None)},
            {"CityID":          RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT,    default=None)},
            {"PageNum":         RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT,    default=1)},
            {"PageSize":        RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT,    default=10)},
        ]

        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_service: UniversityService = UniversityService()
        data = university_service.get_list_object_paginated(params)
        return self.send_response(data)
