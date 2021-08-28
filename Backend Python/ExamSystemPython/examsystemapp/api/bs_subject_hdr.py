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
from examsystemapp.models.bs_subject_hdr import BSSubjectHdrModel
from examsystemapp.services.bs_subject_hdr_service import BSSubjectHdrService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class BSSubjectHdr(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        bs_subject_hdr_json = json.loads(request.POST.get("bs_subject_hdr_json"))

        bs_subject_hdr_object: BSSubjectHdrModel = BSSubjectHdrModel()
        bs_subject_hdr_object.branchsubjectid = bs_subject_hdr_json.get("branchsubjectid")
        bs_subject_hdr_object.branchid = bs_subject_hdr_json.get("branchid")
        bs_subject_hdr_object.semesterid = bs_subject_hdr_json.get("semesterid")

        bs_subject_hdr_service: BSSubjectHdrService = BSSubjectHdrService()
        bs_subject_hdr_object = bs_subject_hdr_service.add(bs_subject_hdr_object)

        return self.send_response(bs_subject_hdr_object)

    def update(self, request: HttpRequest):
        bs_subject_hdr_json = json.loads(request.POST.get("bs_subject_hdr_json"))

        bs_subject_hdr_object: BSSubjectHdrModel = BSSubjectHdrModel()
        bs_subject_hdr_object.branchsubjectid = bs_subject_hdr_json.get("branchsubjectid")
        bs_subject_hdr_object.branchid = bs_subject_hdr_json.get("branchid")
        bs_subject_hdr_object.semesterid = bs_subject_hdr_json.get("semesterid")

        bs_subject_hdr_service: BSSubjectHdrService = BSSubjectHdrService()
        bs_subject_hdr_object = bs_subject_hdr_service.update(bs_subject_hdr_object)

        return self.send_response(bs_subject_hdr_object)

    def delete(self, request: HttpRequest):
        bs_subject_hdr_json = json.loads(request.POST.get("bs_subject_hdr_json"))

        bs_subject_hdr_object: BSSubjectHdrModel = BSSubjectHdrModel()
        bs_subject_hdr_object.branchsubjectid = bs_subject_hdr_json.get("branchsubjectid")
        bs_subject_hdr_object.branchid = bs_subject_hdr_json.get("branchid")
        bs_subject_hdr_object.semesterid = bs_subject_hdr_json.get("semesterid")

        bs_subject_hdr_service: BSSubjectHdrService = BSSubjectHdrService()
        bs_subject_hdr_object = bs_subject_hdr_service.delete(bs_subject_hdr_object)

        return self.send_response(bs_subject_hdr_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        bs_subject_hdr_service: BSSubjectHdrService = BSSubjectHdrService()
        data = bs_subject_hdr_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        bs_subject_hdr_service: BSSubjectHdrService = BSSubjectHdrService()
        data = bs_subject_hdr_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        bs_subject_hdr_service: BSSubjectHdrService = BSSubjectHdrService()
        data = bs_subject_hdr_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        bs_subject_hdr_service: BSSubjectHdrService = BSSubjectHdrService()
        data = bs_subject_hdr_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        bs_subject_hdr_service: BSSubjectHdrService = BSSubjectHdrService()
        data = bs_subject_hdr_service.get_list_object_paginated(params)
        return self.send_response(data)
