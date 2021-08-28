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
from examsystemapp.models.student_ay import StudentAYModel
from examsystemapp.services.student_ay_service import StudentAYService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class StudentAY(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        student_ay_json = json.loads(request.POST.get("student_ay_json"))

        student_ay_object: StudentAYModel = StudentAYModel()

        student_ay_object.studentid = student_ay_json.get("studentid")
        student_ay_object.ayid = student_ay_json.get("ayid")
        student_ay_object.semesterid = student_ay_json.get("semesterid")
        student_ay_object.startdate = student_ay_json.get("startdate")
        student_ay_object.enddate = student_ay_json.get("enddate")

        student_ay_service: StudentAYService = StudentAYService()
        student_ay_object = student_ay_service.add(student_ay_object)

        return self.send_response(student_ay_object)

    def update(self, request: HttpRequest):
        student_ay_json = json.loads(request.POST.get("student_ay_json"))

        student_ay_object: StudentAYModel = StudentAYModel()
        student_ay_object.studentayid = student_ay_json.get("studentayid")
        student_ay_object.studentid = student_ay_json.get("studentid")
        student_ay_object.ayid = student_ay_json.get("ayid")
        student_ay_object.semesterid = student_ay_json.get("semesterid")
        student_ay_object.startdate = student_ay_json.get("startdate")
        student_ay_object.enddate = student_ay_json.get("enddate")

        student_ay_service: StudentAYService = StudentAYService()
        student_ay_object = student_ay_service.update(student_ay_object)

        return self.send_response(student_ay_object)

    def delete(self, request: HttpRequest):
        student_ay_json = json.loads(request.POST.get("student_ay_json"))

        student_ay_object: StudentAYModel = StudentAYModel()
        student_ay_object.studentayid = student_ay_json.get("studentayid")
        
        student_ay_service: StudentAYService = StudentAYService()
        student_ay_object = student_ay_service.delete(student_ay_object)

        return self.send_response(student_ay_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_ay_service: StudentAYService = StudentAYService()
        data = student_ay_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_ay_service: StudentAYService = StudentAYService()
        data = student_ay_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_ay_service: StudentAYService = StudentAYService()
        data = student_ay_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_ay_service: StudentAYService = StudentAYService()
        data = student_ay_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_ay_service: StudentAYService = StudentAYService()
        data = student_ay_service.get_list_object_paginated(params)
        return self.send_response(data)
