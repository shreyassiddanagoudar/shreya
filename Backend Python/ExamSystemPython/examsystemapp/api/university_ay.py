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
from examsystemapp.models.university_ay import UniversityAYModel
from examsystemapp.services.university_ay_service import UniversityAYService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class UniversityAY(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        university_ay_json = json.loads(request.POST.get("university_ay_json"))

        university_ay_object: UniversityAYModel = UniversityAYModel()
        university_ay_object.ayid = university_ay_json.get("ayid")
        university_ay_object.universityid = university_ay_json.get("universityid")
        university_ay_object.startdate = university_ay_json.get("startdate")
        university_ay_object.enddate = university_ay_json.get("enddate")

        university_ay_service: UniversityAYService = UniversityAYService()
        university_ay_object = university_ay_service.add(university_ay_object)

        return self.send_response(university_ay_object)

    def update(self, request: HttpRequest):
        university_ay_json = json.loads(request.POST.get("university_ay_json"))

        university_ay_object: UniversityAYModel = UniversityAYModel()
        university_ay_object.ayid = university_ay_json.get("ayid")
        university_ay_object.universityid = university_ay_json.get("universityid")
        university_ay_object.startdate = university_ay_json.get("startdate")
        university_ay_object.enddate = university_ay_json.get("enddate")

        university_ay_service: UniversityAYService = UniversityAYService()
        university_ay_object = university_ay_service.update(university_ay_object)

        return self.send_response(university_ay_object)

    def delete(self, request: HttpRequest):
        university_ay_json = json.loads(request.POST.get("university_ay_json"))

        university_ay_object: UniversityAYModel = UniversityAYModel()
        university_ay_object.ayid = university_ay_json.get("ayid")
        university_ay_object.universityid = university_ay_json.get("universityid")
        university_ay_object.startdate = university_ay_json.get("startdate")
        university_ay_object.enddate = university_ay_json.get("enddate")

        university_ay_service: UniversityAYService = UniversityAYService()
        university_ay_object = university_ay_service.delete(university_ay_object)

        return self.send_response(university_ay_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_ay_service: UniversityAYService = UniversityAYService()
        data = university_ay_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_ay_service: UniversityAYService = UniversityAYService()
        data = university_ay_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_ay_service: UniversityAYService = UniversityAYService()
        data = university_ay_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_ay_service: UniversityAYService = UniversityAYService()
        data = university_ay_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        university_ay_service: UniversityAYService = UniversityAYService()
        data = university_ay_service.get_list_object_paginated(params)
        return self.send_response(data)
