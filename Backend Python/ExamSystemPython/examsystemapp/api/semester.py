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
from examsystemapp.models.semester import SemesterModel
from examsystemapp.services.semester_service import SemesterService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Semester(BaseController):

    def _init_(self, request):
        BaseController._init_(self, request)

    def add(self, request: HttpRequest):
        semester_json = json.loads(request.POST.get("semester_json"))

        semester_object: SemesterModel = SemesterModel()

       # semester_object.semesterid = semester_json.get("semesterid")
        semester_object.name = semester_json.get("name")
        semester_object.code = semester_json.get("code")

        semester_service: SemesterService = SemesterService()
        semester_object = semester_service.add(semester_object)

        return self.send_response(semester_object)

    def update(self, request: HttpRequest):
        semester_json = json.loads(request.POST.get("semester_json"))

        semester_object: SemesterModel = SemesterModel()
        semester_object.semesterid = semester_json.get("semesterid")
        semester_object.name = semester_json.get("name")
        semester_object.code = semester_json.get("code")

        semester_service: SemesterService = SemesterService()
        semester_object = semester_service.update(semester_object)

        return self.send_response(semester_object)

    def delete(self, request: HttpRequest):
        semester_json = json.loads(request.POST.get("semester_json"))

        semester_object: SemesterModel = SemesterModel()
        semester_object.semesterid = semester_json.get("semesterid")

        semester_service: SemesterService = SemesterService()
        semester_object = semester_service.delete(semester_object)

        return self.send_response(semester_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        semester_service: SemesterService = SemesterService()
        data = semester_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [ {"ids": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')}]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        semester_service: SemesterService = SemesterService()
        data = semester_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        semester_service: SemesterService = SemesterService()
        data = semester_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        semester_service: SemesterService = SemesterService()
        data = semester_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"SemesterName": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')},
            {"SemesterCode": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')},
            {"pageNum": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=0)},
            {"pageSize": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=10)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        semester_service: SemesterService = SemesterService()
        data = semester_service.get_list_object_paginated(params)
        return self.send_response(data)