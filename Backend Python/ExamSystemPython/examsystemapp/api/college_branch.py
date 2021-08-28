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
from examsystemapp.models.college_branch import CollegeBranchModel
from examsystemapp.services.college_branch_service import CollegeBranchService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class CollegeBranch(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        college_branch_json = json.loads(request.POST.get("college_branch_json"))

        college_branch_object: CollegeBranchModel = CollegeBranchModel()
        college_branch_object.collegebranchid = college_branch_json.get("collegebranchid")
        college_branch_object.branchid = college_branch_json.get("branchid")
        college_branch_object.collegeid = college_branch_json.get("collegeid")
        college_branch_object.phonenum = college_branch_json.get("phonenum")
        college_branch_object.email = college_branch_json.get("email")
        college_branch_object.url = college_branch_json.get("url")

        college_branch_service: CollegeBranchService = CollegeBranchService()
        college_branch_object = college_branch_service.add(college_branch_object)

        return self.send_response(college_branch_object)

    def update(self, request: HttpRequest):
        college_branch_json = json.loads(request.POST.get("college_branch_json"))

        college_branch_object: CollegeBranchModel = CollegeBranchModel()
        college_branch_object.collegebranchid = college_branch_json.get("collegebranchid")
        college_branch_object.branchid = college_branch_json.get("branchid")
        college_branch_object.collegeid = college_branch_json.get("collegeid")
        college_branch_object.phonenum = college_branch_json.get("phonenum")
        college_branch_object.email = college_branch_json.get("email")
        college_branch_object.url = college_branch_json.get("url")

        college_branch_service: CollegeBranchService = CollegeBranchService()
        college_branch_object = college_branch_service.update(college_branch_object)

        return self.send_response(college_branch_object)

    def delete(self, request: HttpRequest):
        college_branch_json = json.loads(request.POST.get("college_branch_json"))

        college_branch_object: CollegeBranchModel = CollegeBranchModel()
        college_branch_object.collegebranchid = college_branch_json.get("collegebranchid")
        college_branch_object.branchid = college_branch_json.get("branchid")
        college_branch_object.collegeid = college_branch_json.get("collegeid")
        college_branch_object.phonenum = college_branch_json.get("phonenum")
        college_branch_object.email = college_branch_json.get("email")
        college_branch_object.url = college_branch_json.get("url")

        college_branch_service: CollegeBranchService = CollegeBranchService()
        college_branch_object = college_branch_service.delete(college_branch_object)

        return self.send_response(college_branch_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_branch_service: CollegeBranchService = CollegeBranchService()
        data = college_branch_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_branch_service: CollegeBranchService = CollegeBranchService()
        data = college_branch_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_branch_service: CollegeBranchService = CollegeBranchService()
        data = college_branch_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_branch_service: CollegeBranchService = CollegeBranchService()
        data = college_branch_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_branch_service: CollegeBranchService = CollegeBranchService()
        data = college_branch_service.get_list_object_paginated(params)
        return self.send_response(data)
