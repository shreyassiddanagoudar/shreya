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
from examsystemapp.models.college import CollegeModel
from examsystemapp.services.college_service import CollegeService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class College(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        college_json = json.loads(request.POST.get("college_json"))

        college_object: CollegeModel = CollegeModel()
        # college_object.collegeid = college_json.get("collegeid")
        college_object.universityid = college_json.get("universityid")
        college_object.name = college_json.get("name")
        college_object.code = college_json.get("code")
        college_object.addr1 = college_json.get("addr1")
        college_object.addr2 = college_json.get("addr2")
        college_object.addr3 = college_json.get("addr3")
        college_object.cityid = college_json.get("cityid")
        college_object.stateid = college_json.get("stateid")
        college_object.pincode = college_json.get("pincode")
        college_object.phone = college_json.get("phone")
        college_object.email = college_json.get("email")
        college_object.logo = college_json.get("logo")
        college_object.url = college_json.get("url")

        college_service: CollegeService = CollegeService()
        college_object = college_service.add(college_object)

        return self.send_response(college_object)

    def update(self, request: HttpRequest):
        college_json = json.loads(request.POST.get("college_json"))

        college_object: CollegeModel = CollegeModel()
        college_object.collegeid = college_json.get("collegeid")
        college_object.universityid = college_json.get("universityid")
        college_object.name = college_json.get("name")
        college_object.code = college_json.get("code")
        college_object.addr1 = college_json.get("addr1")
        college_object.addr2 = college_json.get("addr2")
        college_object.addr3 = college_json.get("addr3")
        college_object.cityid = college_json.get("cityid")
        college_object.stateid = college_json.get("stateid")
        college_object.pincode = college_json.get("pincode")
        college_object.phone = college_json.get("phone")
        college_object.email = college_json.get("email")
        college_object.logo = college_json.get("logo")
        college_object.url = college_json.get("url")

        college_service: CollegeService = CollegeService()
        college_object = college_service.update(college_object)

        return self.send_response(college_object)

    def delete(self, request: HttpRequest):
        college_json = json.loads(request.POST.get("college_json"))

        college_object: CollegeModel = CollegeModel()
        college_object.collegeid = college_json.get("collegeid")
    

        college_service: CollegeService = CollegeService()
        college_object = college_service.delete(college_object)

        return self.send_response(college_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_service: CollegeService = CollegeService()
        data = college_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_service: CollegeService = CollegeService()
        data = college_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_service: CollegeService = CollegeService()
        data = college_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_service: CollegeService = CollegeService()
        data = college_service.get_list_object(params)
        return self.send_response(data)


    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"CollegeName  ": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default=None)},
            {"Code": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=None)},
            {"UniversityID   ": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=None)},
            {"StateID": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=None)},
            {"CityID ": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=None)},
            {"page_num": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=1)},
            {"page_size": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=10)},
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        college_service: CollegeService = CollegeService()
        data = college_service.get_list_object_paginated(params)
        return self.send_response(data)