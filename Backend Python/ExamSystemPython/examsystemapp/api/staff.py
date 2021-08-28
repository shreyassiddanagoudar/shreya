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
from examsystemapp.models.staff import StaffModel
from examsystemapp.services.staff_service import StaffService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Staff(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        staff_json = json.loads(request.POST.get("staff_json"))

        staff_object: StaffModel = StaffModel()
        #staff_object.staffid = staff_json.get("staffid")
        staff_object.ownerid = staff_json.get("ownerid")
        staff_object.role = staff_json.get("role")
        staff_object.name = staff_json.get("name")
        staff_object.staffnum = staff_json.get("staffnum")
        staff_object.addr1 = staff_json.get("addr1")
        staff_object.addr2 = staff_json.get("addr2")
        staff_object.cityid = staff_json.get("cityid")
        staff_object.stateid = staff_json.get("stateid")
        staff_object.pin = staff_json.get("pin")
        staff_object.phonenum = staff_json.get("phonenum")
        staff_object.email = staff_json.get("email")
        staff_object.profilepic = staff_json.get("profilepic")
        staff_object.loginid = staff_json.get("loginid")
        staff_object.password = staff_json.get("password")

        staff_service: StaffService = StaffService()
        staff_object = staff_service.add(staff_object)

        return self.send_response(staff_object)

    def update(self, request: HttpRequest):
        staff_json = json.loads(request.POST.get("staff_json"))

        staff_object: StaffModel = StaffModel()
        staff_object.staffid = staff_json.get("staffid")
        staff_object.ownerid = staff_json.get("ownerid")
        staff_object.role = staff_json.get("role")
        staff_object.name = staff_json.get("name")
        staff_object.staffnum = staff_json.get("staffnum")
        staff_object.addr1 = staff_json.get("addr1")
        staff_object.addr2 = staff_json.get("addr2")
        staff_object.cityid = staff_json.get("cityid")
        staff_object.stateid = staff_json.get("stateid")
        staff_object.pin = staff_json.get("pin")
        staff_object.phonenum = staff_json.get("phonenum")
        staff_object.email = staff_json.get("email")
        staff_object.profilepic = staff_json.get("profilepic")
        staff_object.loginid = staff_json.get("loginid")
        staff_object.password = staff_json.get("password")

        staff_service: StaffService = StaffService()
        staff_object = staff_service.update(staff_object)

        return self.send_response(staff_object)

    def delete(self, request: HttpRequest):
        staff_json = json.loads(request.POST.get("staff_json"))

        staff_object: StaffModel = StaffModel()
        staff_object.staffid = staff_json.get("staffid")
        

        staff_service: StaffService = StaffService()
        staff_object = staff_service.delete(staff_object)

        return self.send_response(staff_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        staff_service: StaffService = StaffService()
        data = staff_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        staff_service: StaffService = StaffService()
        data = staff_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        staff_service: StaffService = StaffService()
        data = staff_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        staff_service: StaffService = StaffService()
        data = staff_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"Name": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')},
            {"StaffNum": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=0)},
            {"Role": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default='')},
            {"StateID": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=0)},
            {"CityID": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=0)},
            {"pageNum": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=1)},
            {"pageSize": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=10)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        staff_service: StaffService = StaffService()
        data = staff_service.get_list_object_paginated(params)
        return self.send_response(data)
