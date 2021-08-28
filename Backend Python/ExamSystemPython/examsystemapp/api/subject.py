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
from examsystemapp.models.subject import SubjectModel
from examsystemapp.services.subject_service import SubjectService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Subject(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        subject_json = json.loads(request.POST.get("subject_json"))

        subject_object: SubjectModel = SubjectModel()
        # subject_object.subjectid = subject_json.get("subjectid")
        subject_object.name = subject_json.get("name")
        subject_object.code = subject_json.get("code")

        subject_service: SubjectService = SubjectService()
        subject_object = subject_service.add(subject_object)

        return self.send_response(subject_object)

    def update(self, request: HttpRequest):
        subject_json = json.loads(request.POST.get("subject_json"))

        subject_object: SubjectModel = SubjectModel()
        subject_object.subjectid = subject_json.get("subjectid")
        subject_object.name = subject_json.get("name")
        subject_object.code = subject_json.get("code")

        subject_service: SubjectService = SubjectService()
        subject_object = subject_service.update(subject_object)

        return self.send_response(subject_object)

    def delete(self, request: HttpRequest):
        subject_json = json.loads(request.POST.get("subject_json"))

        subject_object: SubjectModel = SubjectModel()
        subject_object.subjectid = subject_json.get("subjectid")
        # subject_object.name = subject_json.get("name")
        # subject_object.code = subject_json.get("code")

        subject_service: SubjectService = SubjectService()
        subject_object = subject_service.delete(subject_object)

        return self.send_response(subject_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        subject_service: SubjectService = SubjectService()
        data = subject_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        subject_service: SubjectService = SubjectService()
        data = subject_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        subject_service: SubjectService = SubjectService()
        data = subject_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        subject_service: SubjectService = SubjectService()
        data = subject_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"SubjectName": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')},
            {"Code": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')},
            {"PageNum": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=1)},
            {"PageSize": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=25)},
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        subject_service: SubjectService = SubjectService()
        data = subject_service.get_list_object_paginated(params)
        return self.send_response(data)
