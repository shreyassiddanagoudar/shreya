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
from examsystemapp.models.branch import BranchModel
from examsystemapp.services.branch_service import BranchService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Branch(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        branch_json = json.loads(request.POST.get("branch_json"))

        branch_object: BranchModel = BranchModel()
        # branch_object.branchid = branch_json.get("branchid")
        branch_object.name = branch_json.get("name")
        branch_object.code = branch_json.get("code")

        branch_service: BranchService = BranchService()
        branch_object = branch_service.add(branch_object)

        return self.send_response(branch_object)

    def update(self, request: HttpRequest):
        branch_json = json.loads(request.POST.get("branch_json"))

        branch_object: BranchModel = BranchModel()
        branch_object.branchid = branch_json.get("branchid")
        branch_object.name = branch_json.get("name")
        branch_object.code = branch_json.get("code")

        branch_service: BranchService = BranchService()
        branch_object = branch_service.update(branch_object)

        return self.send_response(branch_object)

    def delete(self, request: HttpRequest):
        branch_json = json.loads(request.POST.get("branch_json"))

        branch_object: BranchModel = BranchModel()
        branch_object.branchid = branch_json.get("branchid")
        # branch_object.name = branch_json.get("name")
        # branch_object.code = branch_json.get("code")

        branch_service: BranchService = BranchService()
        branch_object = branch_service.delete(branch_object)

        return self.send_response(branch_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        branch_service: BranchService = BranchService()
        data = branch_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        branch_service: BranchService = BranchService()
        data = branch_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        branch_service: BranchService = BranchService()
        data = branch_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        branch_service: BranchService = BranchService()
        data = branch_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"BranchName": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')},
            {"Code": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')},
            {"pageNum": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=0)},
            {"pageSize": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=10)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        branch_service: BranchService = BranchService()
        data = branch_service.get_list_object_paginated(params)
        return self.send_response(data)
